from django.shortcuts import render, redirect
from authApp import forms, models

# Create your views here.

# home view
def home_view(request):
    return render (request, 'authApp/home.html')

# login view
def log_in_view(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm (request.POST)
        if form.is_valid():
            return redirect ('home')
    return render (request, 'registration/login.html', {'form' : form})

# Sign up view
def sign_up_view(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    return render (request, 'registration/signup', {'form' : form})

# creating post
def create_post(request, ui):
    post = models.Post.Object.get(id = ui)
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance = post)
        return redirect ('post')
    return render (request, 'authApp/create.html', {'form': form})

# deleting a post
def delete_post (request, ui):
    post = models.Post.object.get(id = ui)
    if request.method == 'POST':
        post = post(request.POST)
        post.delete()
        return redirect ('post')
    return render (request, 'authApp/delete_post.html', {'post': post})

