from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']