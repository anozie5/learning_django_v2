from django.db import models
from django.contrib.auth.models import User

# create models
# for posts
class Post (models.Model):
    id = models.UUIDField (unique = True, null = False, primary_key = True)
    user = models.ForeignKey (User, on_delete = models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField (auto_now_add = True)
    date_updated = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.user



