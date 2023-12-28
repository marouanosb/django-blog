from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  #django predefined user creation form

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #specify what model will affected and what fields in order whill be shown in the form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
