from django.contrib import admin

from .models import Profile, CustomUser


admin.site.register(Profile)
admin.site.register(CustomUser)

