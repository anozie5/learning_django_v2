from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

# Create your models here.

# for users
class UserAccount (models.Model):
    first_name = models.CharField (max_length = 20)
    last_name = models.CharField (max_length = 20)
    user_name = models.TextField(max_length = 20)
    email = models.EmailField()
    password = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    USERNAME_FIELD = user_name

# for posts
class Post (models.Model):
    user = models.ForeignKey (UserAccount, on_delete = models.CASCADE, related_name = 'user_names')
    post = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

