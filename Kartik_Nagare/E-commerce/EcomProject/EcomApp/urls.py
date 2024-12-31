from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = "home"),
    path('about', views.about , name = "about"),
    path('contact', views.contact , name = "contact"),
    path('allproduct', views.allproduct , name = "allproduct"),
    path('auth', views.auth , name = "auth"),
    path('login', views.signin , name = "login"),
    path('signup', views.signup , name = "signup"),
    path('logout', views.log , name = "logout"),
    path('single_product/<int:id>', views.single_product , name = "single_product"),
    path('cart', views.cart , name = "cart"),
    path('add/<int:id>/', views.add_to_cart , name = 'add_to_cart'),
    path('remove/<int:id>/' , views.remove_from_cart , name= 'remove_from_cart'),
    path('checkout' , views.checkout , name= 'checkout'),
    path('placed_order' , views.order_now , name='order-now'),
    path('order_history' , views.order_history , name='order_history')
]