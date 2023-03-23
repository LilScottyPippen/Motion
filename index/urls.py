from django.urls import path
from .views import indexPage, notePage

urlpatterns = [
    path('', indexPage, name='index'),
    path('note/', notePage, name='note'),
]