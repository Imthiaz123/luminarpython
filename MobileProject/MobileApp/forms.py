from django.forms import ModelForm
from MobileApp.models import *
from django import forms


class UserForm(ModelForm):
    class Meta:
        model=users
        fields=['name','address','mobilenum','emailid','username','password']
        widgets={
            'password': forms.PasswordInput,
        }

class LoginForm(ModelForm):
    class Meta:
        model=users
        fields=['username','password']
        widgets={
            'password': forms.PasswordInput,
        }

