from rest_framework import serializers
from .models import Listing, Type, Location, Level, Audience

class ListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)

class LocationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)
    
class LevelSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)

class AudienceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)

class Location(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Audience(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField()
    start_date = models.DateTimeField()
    apply_by_date = models.DateTimeField()
    image = models.URLField()
    date_created = models.DateTimeField()
    typeList = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.CASCADE)
    audience = models.ForeignKey(Audience, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_listing'
    )

    def __str__(self):
        return self.title