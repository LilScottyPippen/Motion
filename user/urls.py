from django.urls import path
from .views import authUser, regUser

urlpatterns = [
    path('authorization/', authUser, name='auth'),
    path('registration/', regUser, name='reg')
]