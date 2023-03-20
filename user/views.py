from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def authUser(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username or password is incorrect")
    else:
        return redirect('/')
    return render(request, 'user/authorization.html')

def regUser(request):
    return render(request, 'user/registration.html')
