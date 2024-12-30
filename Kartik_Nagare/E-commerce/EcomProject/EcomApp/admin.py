from django.contrib import admin

# Register your models here.
from . models import product , Category , Sub_category , cartItem

admin.site.register(product)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(cartItem)