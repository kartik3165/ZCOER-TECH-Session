from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name= " home"),
    path('add' , views.add , name = "add"),
    path('sub' , views.sub , name = "sub"),
    path('div' , views.div , name = "div"),
    path('multi' , views.multi , name = "multi"),
    path('addnumber' , views.addnumber , name="addNumber"),
    path('subnumber' , views.subnumber , name="subNumber"),
    path('divnumber' , views.divnumber , name="divNumber"),
    path('multinumber' , views.multinumber , name="multiNumber")
]