from django.db import models
from django.contrib.auth.models import User

# create models
class Post (models.Model):
    user = models.OneToOneField (User, on_delete = models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField (auto_now_add = True)
    date_updated = models.DateTimeField (auto_now = True)