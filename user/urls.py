from django.urls import path
from .views import authUser, regUser, github_login, github_callback

urlpatterns = [
    path('authorization/', authUser, name='auth'),
    path('registration/', regUser, name='reg'),
    path('github/login/', github_login, name='github_login'),
    path('github/callback/', github_callback, name='github_callback'),
]