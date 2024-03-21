from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.views import View
from .models import *
from .forms import CustomerProfileForm ,CustomerRegistrationForm , NGORegistrationForm
from django.contrib import messages
from django import forms

# Create your views here.
def home(request):
    return render(request, "sneaker/home.html")

def about(request):
    return render(request, "sneaker/about.html")

def contact(request):
    return render(request, "sneaker/contact.html")

class Categoryview(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'sneaker/category.html',locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"sneaker/productdetail.html", {'product' : product})

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'sneaker/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User successfully created")
        #else:
            #messages.error(request,"Invalid Input Data")
        return render(request,'sneaker/customerregistration.html',locals())


class Profileview(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'sneaker/profile.html', locals())

    def post(self, request):
        print(request.POST)  # Print out the POST data for debugging
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile,
                           state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile saved successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'sneaker/profile.html', locals())


def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'sneaker/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        form=CustomerProfileForm()
        return render(request, 'sneaker/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        return render(request, 'sneaker/updateAddress.html', locals())


class NGORegistrationView(View):
    def get(self, request):
        form = NGORegistrationForm()
        return render(request, 'sneaker/ngoregistration.html', {'form': form})

    def post(self, request):
        form = NGORegistrationForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            requirment = form.cleaned_data['requirment']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            contact_number = form.cleaned_data['contact_number']

            ngo = NGO(user=user, name=name,requirment=requirment, locality=locality, city=city, address=address, contact_number=contact_number)
            ngo.save()
            messages.success(request, "Congratulations! NGO registration successful")
            return redirect('home')  # Redirect to wherever you want
        else:
            messages.error(request, "Invalid input data")
            return render(request, 'sneaker/ngoregistration.html', {'form': form})




def ngo_information(request):
    ngos = NGO.objects.all()
    return render(request, 'sneaker/ngo_information.html', {'ngos': ngos})

# views.py
def ngo_detail(request, pk):
    ngo = NGO.objects.get(pk=pk)
    return render(request, 'sneaker/ngo_detail.html', {'ngo': ngo})


def home(request):
    return render(request, "sneaker/home.html")

# views.py
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming 'home' is the name of your homepage URL pattern
    else:
        form = ProductForm()
    return render(request, 'sneaker/add_product.html', {'form': form})
