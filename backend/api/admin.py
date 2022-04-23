from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Vote)
admin.site.register(models.Tag)
admin.site.register(models.Post)
