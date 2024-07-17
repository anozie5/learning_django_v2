from django import forms
from authApp import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#create the forms for the models here
class RegisterForm (UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

# form for login
class LoginForm (AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

# form for posts
class PostForm (forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'