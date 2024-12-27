from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import logout , login , authenticate

# Create your views here.
def home(request):
    return render(request,'index.html')

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def furniture(request):
    return render(request, 'furniture.html')

def auth(request):
    return render(request, 'auth.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_pass = request.POST['password2']

        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]

        if password == c_pass:
            user = User.objects.create_user(
                first_name=first_name , 
                last_name = last_name ,
                email = email ,
                username = username ,
                password = password
            )

            user.save()
            return redirect('/')

def login(request):
    username = request.POST['Username']
    password = request.POST['password']

    user = authenticate(
        request , 
        Username = username ,
        password = password
    )

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        print("Invalid Credentials!!")
        return redirect('/auth')


def user_logout(request):
    logout(request)
    return redirect('/')