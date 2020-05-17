from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    email = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class UpdateUserprofile_Form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['contact', 'image']


class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class AddProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description']

