from django.db import models
from django.contrib.auth.models import User
from django.forms import PasswordInput

# create models
# for accounts
class Account (models.Model):
    first_name = models.CharField (max_length = 20)
    last_name = models.CharField (max_length = 20)
    username = models.TextField()
    email = models.EmailField()
    password = PasswordInput()
    date_joined = models.DateTimeField(auto_now_add = True)
# for posts
class Post (models.Model):
    user = models.ForeignKey (Account, on_delete = models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField (auto_now_add = True)
    date_updated = models.DateTimeField (auto_now = True)

