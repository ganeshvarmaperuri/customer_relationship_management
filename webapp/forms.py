from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    email = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class mail_sending(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=80)
    subject = forms.CharField(max_length=80)
    message = forms.CharField(required=False)

