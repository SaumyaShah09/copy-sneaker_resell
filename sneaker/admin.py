from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','email','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']

@admin.register(NGO)
class NGOModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'requirement' ,'name', 'locality', 'city', 'address', 'contact_number']