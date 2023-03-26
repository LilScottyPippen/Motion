from django.urls import path
from .views import authUser, regUser, resetUser, logoutUser, google_auth, github_auth, google_callback, github_callback, verifyEmail, changePassword

urlpatterns = [
    path('authorization/', authUser, name='auth'),
    path('registration/', regUser, name='reg'),
    path('resetPassword/', resetUser, name='reset'),
    path('logout/', logoutUser, name='logout'),
    path('verif/<str:email>/<str:token>', verifyEmail, name='verif'),
    path('changePassword/<str:email>/<str:token>', changePassword, name='changePassword'),
    path('google/auth/', google_auth, name='google_auth'),
    path('google/callback/', google_callback, name='google_callback'),
    path('github/login/', github_auth, name='github_login'),
    path('github/callback/', github_callback, name='github_callback'),
]