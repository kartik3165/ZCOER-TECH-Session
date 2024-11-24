from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def SignUp(request):
    if request.method == 'POST':
        username =  request.POST['email']
        password = request.POST['pass']
        name = request.POST['name']

        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]

        users = User.objects.create_user(username=username, password=password, email=username, first_name=first_name, last_name=last_name)

        print("User created Successfully !!!", users)

        return redirect('/')
    else:
        return render(request , 'signUp.html')
