from django.shortcuts import render, redirect, reverse
from user.models import CustomUser
# Create your views here.

def indexPage(request):
    if request.user.is_authenticated:
        return redirect('note/')
    return render(request, 'index/index.html')

def notePage(request):
    email = request.user.email
    username = request.user.username

    context = {
        'email': email,
        'username': username
    }
    return render(request, 'index/note.html', context)
