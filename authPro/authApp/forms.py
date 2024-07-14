from django import forms
from authApp import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#create the forms for the models here
class RegisterForm (UserCreationForm):
    class Meta:
        model = models.UserAccount
        fields = '__all__'

# form for login
class LoginForm (AuthenticationForm):
    class Meta:
        model = models.UserAccount
        fields = ['user_name', 'password']

# form for posts
class PostForm (forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'