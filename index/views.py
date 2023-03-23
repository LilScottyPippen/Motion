from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from user.models import CustomUser
from .forms import NoteForm
from .models import Note
# Create your views here.

def indexPage(request):
    if request.user.is_authenticated:
        return redirect('note/')
    return render(request, 'index/index.html')

@login_required(login_url='auth')
def notePage(request):
    email = request.user.email
    username = request.user.username
    context = {
        'email': email,
        'username': username,
    }
    return render(request, 'index/note.html', context)

