from django.contrib import admin
from profile_app import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)

# Register your models here.
