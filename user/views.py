from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateUserForm
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
import requests
from .models import CustomUser
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
                messages.info(request, "Username or password is incorrect")
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

def github_login(request):
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
    user_id = json_response['id']
    username = json_response['login']
    github_user, created = CustomUser.objects.get_or_create(github_id=user_id)
    github_user.username = username
    github_user.save()

    user = authenticate(request, username=username, password=None)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('Authentication failed')
    return redirect('/')