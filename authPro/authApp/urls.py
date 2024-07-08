from django.urls import path
from authApp import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('sign-up/', views.sign_up_view, name = 'signup'),
]
