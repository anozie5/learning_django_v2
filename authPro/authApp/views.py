from django.shortcuts import render, redirect


# Create your views here.

# home view
def home_view(request):
    return render (request, 'authApp/home.html')

