from django.shortcuts import render

# Create your views here.

def authUser(request):
    return render(request, 'user/authorization.html')

def regUser(request):
    return render(request, 'user/registration.html')
