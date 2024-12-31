from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate , login
from . models import product , cartItem , Order , Category , Sub_category 
from time import time
from datetime import datetime

def gen_order_id():
    date_part = datetime.now().strftime("%d%m%y") 
    time_part = str(int(time() * 1000))[-4:]       
    return (date_part + time_part)


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

def checkout(request):
    item = cartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in item)
    return render(request , 'checkout.html' , {'item' : item , 'total_price' : total_price} )

def order_now(request):
    item = cartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in item)
    if request.method == 'POST':
        full_name = request.POST['full_name']
        mobile_number = request.POST['ph_no']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        pay_mode = request.POST['mode']

    order_id = gen_order_id()

    for i in item:  
        Order.objects.create(
            user = request.user,
            product = i.product ,
            order_id = order_id,
            address  = address ,
            mobile_no = mobile_number ,
            order_value = i.product.price * i.quantity
        )
    item.delete()
    order_info = Order.objects.filter(user = request.user )
    return render(request , 'checkout.html' , {'order_info' : order_info})

def order_history(request):
    order_info = Order.objects.filter(user = request.user )
    return render(request , 'order_history.html' , {'order_info' : order_info})




    

        


