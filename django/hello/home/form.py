from dataclasses import field
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    password1= forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label="Password Again",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True ,label="email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=('username','email')
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
