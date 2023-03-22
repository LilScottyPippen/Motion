from django.urls import path
from .views import authUser, regUser, google_auth, google_callback

urlpatterns = [
    path('authorization/', authUser, name='auth'),
    path('registration/', regUser, name='reg'),
    path('google/auth/', google_auth, name='google_auth'),
    path('google/callback/', google_callback, name='google_callback'),
]