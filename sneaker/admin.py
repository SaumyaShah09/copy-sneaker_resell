from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(Prodcut)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','email','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']