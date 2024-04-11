from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Product, Customer, NGO
from .forms import CustomerProfileForm, CustomerRegistrationForm, NGORegistrationForm, ProductForm

# Home page view
def home(request):
    return render(request, "sneaker/home.html")

# About page view
def about(request):
    return render(request, "sneaker/about.html")

# Contact page view
def contact(request):
    return render(request, "sneaker/contact.html")

# View for displaying products by category
class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        return render(request, 'sneaker/category.html', {'products': products})

# View for displaying product details
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "sneaker/productdetail.html", {'product': product})

# View for customer registration
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'sneaker/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User successfully created")
            return redirect('home')
        else:
            messages.error(request, "Invalid Input Data")
            return render(request, 'sneaker/customerregistration.html', {'form': form})

# View for customer profile
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'sneaker/profile.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            profile_data = form.cleaned_data
            profile_data['user'] = user
            Customer.objects.create(**profile_data)
            messages.success(request, "Congratulations! Profile saved successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('home')

# View for displaying and updating customer addresses
def address(request):
    addresses = Customer.objects.filter(user=request.user)
    return render(request, 'sneaker/address.html', {'addresses': addresses})

class UpdateAddress(View):
    def get(self, request, pk):
        form = CustomerProfileForm()
        return render(request, 'sneaker/updateAddress.html', {'form': form})

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            # Update customer address logic here
            messages.success(request, "Address updated successfully")
            return redirect('address')
        else:
            messages.error(request, "Invalid Input Data")
            return render(request, 'sneaker/updateAddress.html', {'form': form})

# View for NGO registration
class NGORegistrationView(View):
    def get(self, request):
        form = NGORegistrationForm()
        return render(request, 'sneaker/ngoregistration.html', {'form': form})

    def post(self, request):
        form = NGORegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! NGO registration successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid input data")
            return render(request, 'sneaker/ngoregistration.html', {'form': form})

# View for displaying NGO information
def ngo_information(request):
    ngos = NGO.objects.all()
    return render(request, 'sneaker/ngo_information.html', {'ngos': ngos})

# View for displaying NGO details
def ngo_detail(request, pk):
    ngo = NGO.objects.get(pk=pk)
    return render(request, 'sneaker/ngo_detail.html', {'ngo': ngo})

# View for adding a product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'sneaker/add_product.html', {'form': form})

