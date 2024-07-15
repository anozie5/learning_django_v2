from django.contrib import admin
from authApp import models

# Register your models here.
admin.site.register (models.Post, models.UserAccount)
