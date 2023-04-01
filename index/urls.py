from django.urls import path
from .views import indexPage, notePage, createOrOpenNote, createNote, deleteNote, noteShare

urlpatterns = [
    path('', indexPage, name='index'),
    path('note/', createOrOpenNote, name='note'),
    path('note/<str:url>', notePage, name='notePage'),
    path('note/<str:url>/<int:isPublic>', noteShare, name='noteShare'),
    path('createNote/', createNote, name='createNote'),
    path('deleteNote/<str:url>', deleteNote, name='deleteNote')
]