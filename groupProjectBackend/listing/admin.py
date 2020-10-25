from django.contrib import admin

from .models import Listing, Type, Location, Level, Audience

admin.site.register(Listing)
admin.site.register(Type)
admin.site.register(Location)
admin.site.register(Level)
admin.site.register(Audience)
