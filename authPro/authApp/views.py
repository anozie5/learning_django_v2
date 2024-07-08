from django.shortcuts import render, redirect
from authApp import forms, models

# Create your views here.

# home view
def home_view(request):
    return render (request, 'authApp/home.html')

# Sign up view
def sign_up_view(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    return render (request, 'registration/sign_up', {'form' : form})

# login view
def log_in_view(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm (request.POST)
        if form.is_valid():
            return redirect ('home')
    return render (request, 'registration/log-in.html', {'form' : form})



