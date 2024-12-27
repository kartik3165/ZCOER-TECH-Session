from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('shop/' , views.shop , name="shop"),
    path('about/' , views.about , name="about"),
    path('contact/' , views.contact , name="contact"),
    path('furniture/' , views.furniture , name="furniture"),
    path('auth/' , views.auth ,  name="auth"),
    path('signup' , views.signup ,  name="signup"),
    path('login' , views.login ,  name="login"),
    path('logout/' , views.user_logout ,  name="logout")
]