from django.db import models
# Create your models here.

# for users
class UserAccount (models.Model):
    first_name = models.CharField (max_length = 20)
    last_name = models.CharField (max_length = 20)
    email = models.EmailField()
    password = models.TextField()
    date_created = models.DateTimeField (auto_now_add = True)
 
# for posts
class Post (models.Model):
    user = models.ForeignKey (UserAccount, on_delete = models.CASCADE, related_name = 'user_names')
    post = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

