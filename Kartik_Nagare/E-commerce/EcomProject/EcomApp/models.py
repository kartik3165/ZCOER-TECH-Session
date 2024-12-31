from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
class Sub_category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
    

class product(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100, default='indian')
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, default=0)
    sub_category = models.ForeignKey(Sub_category, related_name='category', on_delete=models.CASCADE, default=0)
    price = models.IntegerField()
    tags = models.CharField(max_length=100 , default="none")
    offer = models.BooleanField(default=False)
    img = models.ImageField(upload_to='EcomProject/media')

    def __str__(self):
        return self.name

class cartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} x {self.user}'
    
class Order(models.Model):
    order_id = models.CharField(max_length=50)
    user = models.ForeignKey(User , related_name='order' , on_delete=models.CASCADE)
    product = models.ForeignKey(product , related_name='order_item' , on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    mobile_no = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())
    STATUS_CH = [('pending','pending'),('delivered','delivered'),('on_the_Way','on_the_Way')]
    status = models.CharField(max_length=100 , choices=STATUS_CH , default='pending')
    order_value = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.order_id} {self.user} {self.product}'