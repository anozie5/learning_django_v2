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

    def __init__(self, first_name, last_name, username, email, password, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.date_joined = date_joined
    
    def __str__(self,):
        return self.username

# for posts
class Post (models.Model):
    user = models.ForeignKey (Account, on_delete = models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField (auto_now_add = True)
    date_updated = models.DateTimeField (auto_now = True)

    def __init__(self, user, text, date_created, date_updated):
        self.user = user
        self.text = text
        self.date_created = date_created
        self.date_updated = date_updated

    def __str__(self,):
        return self.user

