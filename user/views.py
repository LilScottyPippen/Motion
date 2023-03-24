from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.conf import settings
from django.http import HttpResponseBadRequest
from .models import CustomUser, GoogleCredentials, GitHubCredentials
from django.urls import reverse
import urllib.parse
import json
from django.http import HttpResponseRedirect, HttpResponse
import requests
# Create your views here.

def authUser(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Email or password is incorrect")
    else:
        return redirect('/')
    return render(request, 'user/authorization.html')

def regUser(request):
    if request.user.is_anonymous:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('auth')
    else:
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'user/registration.html', context)

def resetUser(request):
    return render(request, 'user/resetPassword.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def google_auth(request):
    redirect_uri = request.build_absolute_uri(reverse('google_callback'))
    print(redirect_uri)
    params = {
        'response_type': 'code',
        'scope': 'email profile',
        'redirect_uri': redirect_uri,
        'client_id': settings.GOOGLE_CLIENT_ID,
    }
    url = 'https://accounts.google.com/o/oauth2/auth?' + urllib.parse.urlencode(params)
    return redirect(url)

def google_callback(request):
    if 'error' in request.GET:
        return HttpResponseBadRequest(request.GET['error_description'])
    else:
        code = request.GET.get('code', None)
        if code is None:
            return HttpResponseBadRequest('No code provided')
        else:
            redirect_uri = request.build_absolute_uri(reverse('google_callback'))
            data = {
                'code': code,
                'redirect_uri': redirect_uri,
                'client_id': settings.GOOGLE_CLIENT_ID,
                'client_secret': settings.GOOGLE_CLIENT_SECRET,
                'grant_type': 'authorization_code',
            }
            response = requests.post('https://accounts.google.com/o/oauth2/token', data=data)
            if response.status_code != 200:
                return HttpResponseBadRequest(response.text)
            else:
                tokens = json.loads(response.text)
                access_token = tokens['access_token']
                id_token = tokens['id_token']
                user_info = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?access_token=' + access_token)
                user_info = json.loads(user_info.text)
                if GoogleCredentials.objects.filter(email=user_info['email']):
                    user, created = CustomUser.objects.get_or_create(email=user_info['email'])
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        return HttpResponse('Authentication failed')
                else:
                    user, created = CustomUser.objects.get_or_create(email=user_info['email'])
                    credentials = GoogleCredentials.objects.create(user=user, access_token=access_token, id_token=id_token, email=user_info['email'])
                    credentials.save()
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        return HttpResponse('Authentication failed')
                return redirect('/')

def github_auth(request):
    authorize_url = f"{settings.GITHUB_AUTHORIZE_URL}?client_id={settings.GITHUB_CLIENT_ID}"
    return HttpResponseRedirect(authorize_url)

def github_callback(request):
    code = request.GET.get('code')
    access_token_url = settings.GITHUB_ACCESS_TOKEN_URL
    headers = {'accept': 'application/json'}
    data = {
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_CLIENT_SECRET,
        'code': code
    }
    response = requests.post(access_token_url, headers=headers, data=data)
    json_response = response.json()
    access_token = json_response['access_token']
    user_url = f"{settings.GITHUB_API_URL}/user"
    headers = {
        'Authorization': f'token {access_token}',
        'accept': 'application/json'
    }
    response = requests.get(user_url, headers=headers)
    json_response = response.json()
    if GitHubCredentials.objects.filter(_id=json_response['id']):
        user, created = CustomUser.objects.get_or_create(username=json_response['login'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Authentication failed')
    else:
        user, created = CustomUser.objects.get_or_create(username=json_response['login'])
        credentials = GitHubCredentials.objects.create(user=user, _id=json_response['id'], login=json_response['login'])
        credentials.save()
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Authentication failed')
    return redirect('/')
