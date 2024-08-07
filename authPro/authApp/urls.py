from django.urls import path
from authApp import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('login/', views.log_in_view, name = 'login'),
    path('signup/', views.sign_up_view, name = 'signup'),
    path('logout/', views.logout_view, name = 'logout'),
    path('users/', views.users_view, name = 'users'),
    path('create/', views.create_post, name = 'create'),
    path('delete/<int:ui>/', views.delete_post, name = 'delete')
]
