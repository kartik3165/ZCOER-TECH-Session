from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate , login
from . models import product , cartItem

# Create your views here.

def home(request):
    product_data = product.objects.all()[:4]
    return render(request , 'index.html' , {'Product' : product_data })

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request ,'contact.html')

def allproduct(request):
    product_data = product.objects.all()
    return render(request , 'allproduct.html' , {'Product' : product_data })

def auth(request):
    return render(request , 'auth.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = email , 
            password = password 
            )
        user.save()
        return redirect('/')

def signin(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username = username , password = password)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        return redirect('/auth')
    
def log(request):
    # logout function
    logout(request)
    return redirect('/')

def single_product(request , id ):
    product_data = product.objects.get(id = id)
    all_product = product.objects.all() 
    return render(request , 'single_product.html' , {'Product' : product_data , 'all_product' : all_product})

def cart(request):
    cart_items = cartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request , 'cart.html' , {'cart_items' : cart_items , 'total_price' : total_price})


def add_to_cart(request , id):
    Product = product.objects.get(id = id)
    cart_item , created = cartItem.objects.get_or_create(product = Product , user = request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def remove_from_cart(request, id):
    cart_item = cartItem.objects.get(id=id)
    cart_item.delete()
    return redirect('cart')


