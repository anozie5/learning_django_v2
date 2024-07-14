from django import forms
from authApp import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create the forms for the models here
class RegisterForm (UserCreationForm):
    email = forms.EmailField (required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# form for posts
class PostForm (forms.ModelForm):
    class Meta:
        model = models.Post
        fields = {
            'user': 'user',
            'post': 'post'
        }