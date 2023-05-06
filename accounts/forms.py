from django import forms
from django.contrib.auth.models import User




#used a basic form to register user because creating model form from
#inbuilt User model had few issues. But user will still be registered
#into that model
class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=200)
    last_name = forms.CharField(label="Last Name", max_length=200)
    username = forms.CharField(label="Userame", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    password= forms.CharField(label="Password", max_length=200)
    confirm_password = forms.CharField(label="Confirm Password", max_length=200)


class LoginForm(forms.Form):
    username = forms.CharField(label="Userame", max_length=200)
    password= forms.CharField(label="Password", max_length=200)