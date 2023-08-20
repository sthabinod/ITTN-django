from django.urls import path
from .views import login_user, register, logout_user

urlpatterns = [
  path('login',login_user,name="login_user"),
  path('register',register,name="register"),
  path('logout',logout_user,name="logout_user"),
]
