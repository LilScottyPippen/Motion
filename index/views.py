from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Note
import string
import random
# Create your views here.

def indexPage(request):
    if request.user.is_authenticated:
        return redirect('note/')
    return render(request, 'index/index.html')

@login_required(login_url='auth')
def notePage(request, url):
    try:
        note = Note.objects.get(url=url)
        if request.user == note.user_id or note.isPublic == True:
            email = request.user.email
            username = request.user.username
            notes = Note.objects.filter(user_id=request.user)
            if request.method == 'POST':
                note.title = request.POST.get('title')
                note.text = request.POST.get('text')
                note.save()
        else:
            return redirect('note')
    except:
        return redirect('note')
    context = {
        'email': email,
        'username': username,
        'note': note,
        'notes': notes
    }
    return render(request, 'index/note.html', context)

@login_required(login_url='auth')
def createOrOpenNote(request):
    notes = Note.objects.filter(user_id=request.user)
    if notes.count() == 0:
        characters = string.ascii_letters + string.digits
        url = ''.join(random.choice(characters) for i in range(10))
        note = Note(user_id=request.user, title='Get started', text='', url=url)
        note.save()
    else:
        last_note = notes.last()
        url = last_note.url
    return redirect('notePage', url=url)

@login_required(login_url='auth')
def createNote(request):
    characters = string.ascii_letters + string.digits
    url = ''.join(random.choice(characters) for i in range(10))
    note = Note(user_id=request.user, title='Title', text='', url=url)
    note.save()
    return redirect('notePage', url=url)
@login_required(login_url='auth')
def deleteNote(request, url):
    note = Note.objects.get(url=url)
    note.delete()
    return redirect('note')

@login_required(login_url='auth')
def noteShare(request, url, isPublic):
    note = Note.objects.get(url=url)
    print(isPublic)
    if isPublic == 1:
        note.isPublic = True
        note.save()
    if isPublic == 0:
        note.isPublic = False
        note.save()
    return redirect('notePage', url=url)