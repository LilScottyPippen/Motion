from django.urls import path
from .views import authUser, regUser, google_auth, github_auth, google_callback, github_callback

urlpatterns = [
    path('authorization/', authUser, name='auth'),
    path('registration/', regUser, name='reg'),
    path('google/auth/', google_auth, name='google_auth'),
    path('google/callback/', google_callback, name='google_callback'),
    path('github/login/', github_auth, name='github_login'),
    path('github/callback/', github_callback, name='github_callback'),
]