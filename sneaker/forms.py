from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

from .models import Customer,Product


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : 'True',
                                                           'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
                                                                 'class' : 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput
    (attrs={'autocomplete' : 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput
    (attrs={'autocomplete' : 'current-password' , 'class' : 'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True',
     'class': 'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
        old_password = forms.CharField(label='Old password' , widget=forms.PasswordInput
        (attrs={'autofocus':'true','autocomplete':'current-password','class':'form-control'}))
        new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput
        (attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
        new_password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput
        (attrs={'autocomplete': 'confirm-password', 'class': 'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model =  Customer
        fields = ['id','name', 'locality', 'city', 'state', 'zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class' : 'form-control'}),
            'locality':forms.TextInput(attrs={'class' : 'form-control'}),
            'city':forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile':forms.NumberInput(attrs={'class' : 'form-control'}),
            'state':forms.Select(attrs={'class' : 'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class' : 'form-control'}),
        }



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NGO

from django.contrib.auth.forms import UserCreationForm
from .models import NGO

from django.shortcuts import render, redirect
from django.views import View


class NGORegistrationView(View):
    def get(self, request):
        ngo_form = NGORegistrationForm()
        user_form = UserForm()
        return render(request, 'registration/ngo_registration.html', {'ngo_form': ngo_form, 'user_form': user_form})

    def post(self, request):
        ngo_form = NGORegistrationForm(request.POST)
        user_form = UserForm(request.POST)
        if ngo_form.is_valid() and user_form.is_valid():
            user = user_form.save()  # Save the user
            ngo = ngo_form.save(commit=False)
            ngo.user = user
            ngo.set_password(user_form.cleaned_data['password'])  # Set the password
            ngo.save()
            return redirect('login')  # Redirect to login page after successful registration
        return render(request, 'registration/ngo_registration.html', {'ngo_form': ngo_form, 'user_form': user_form})

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'email', 'prodapp', 'category', 'product_image']


from django import forms
from .models import NGO
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NGORegistrationForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name', 'requirement', 'locality', 'city', 'address', 'contact_number']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
