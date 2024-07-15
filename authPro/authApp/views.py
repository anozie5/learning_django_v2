from django.shortcuts import render, redirect
from authApp import forms, models
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# home view
def home_view(request):
    return render (request, 'authApp/home.html')

# login view
def log_in_view(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm (request.POST)
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

# Logout view
def logout_view(request):
    return render (request, 'registration/login.html')

# creating post
@login_required
def create_post(request, ui):
    post = models.UserAccount.Object.get(id = ui)
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance = post)
        return redirect ('post')
    return render (request, 'authApp/create.html', {'form': form})

# updating a post
def update_post(request, ui):
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

# listing all users
@permission_required
def users_view (request):
    users = models.UserAccount.object.all()
    return render (request, 'authApp/users.html', {'user': users})

# banning a user
@permission_required
def ban_user_view (request, ui):
    user = models.UserAccount.object.get(id = ui)
    if request.method == 'post':
        user = user(request.post)
        user.delete()
        return redirect ('users')
    return render (request, 'authApp/delete_user', {'user': user})

