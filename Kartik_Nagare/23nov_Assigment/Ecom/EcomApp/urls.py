from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('login' , views.login),
    path('signup' , views.SignUp)
]