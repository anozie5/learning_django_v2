from django.db import models
from django.forms import PasswordInput

# create models
class UserAccount (models.Model):
    id = models.UUIDField (unique = True, null = False)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    email = models.EmailField(max_length=254)
    password = PasswordInput()
    date_joined = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.username


# for posts
class Post (models.Model):
    user = models.ForeignKey (UserAccount, on_delete = models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField (auto_now_add = True)
    date_updated = models.DateTimeField (auto_now = True)



