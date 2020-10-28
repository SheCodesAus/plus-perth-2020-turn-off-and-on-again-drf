from rest_framework import serializers
from .models import Listing, Type, Location, Level, Audience

class TypeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)
    slug = serializers.ReadOnlyField(required=False)

    def create(self, validated_data):
        return Type.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance

class LocationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)
    slug = serializers.ReadOnlyField(required=False)

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance
    
class LevelSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)
    slug = serializers.ReadOnlyField(required=False)

    def create(self, validated_data):
        return Level.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance

class AudienceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=32)
    slug = serializers.ReadOnlyField(required=False)

    def create(self, validated_data):
        return Audience.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance

class ListingSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    date_created = serializers.DateTimeField()
    start_date = serializers.DateTimeField()
    apply_by_date = serializers.DateTimeField()
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    link = serializers.URLField()
    eligibility = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source="owner.username")
    typeList = serializers.SlugRelatedField('name', queryset=Type.objects.all())
    location = serializers.SlugRelatedField('name', queryset=Location.objects.all())
    level = serializers.SlugRelatedField('name', queryset=Level.objects.all())
    audience = serializers.SlugRelatedField('name', queryset=Audience.objects.all())

    def create(self, validated_data):
        return Listing.objects.create(**validated_data)

class ListingDetailSerializer(ListingSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.date_created = validated_data.get("date_created", instance.date_created)
        instance.start_date = validated_data.get("start_date", instance.start_date)
        instance.apply_by_date = validated_data.get("apply_by_date", instance.apply_by_date)
        instance.image = validated_data.get("image", instance.image)
        instance.link = validated_data.get("link", instance.link)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.typeList = validated_data.get("typeList", instance.typeList)
        instance.location = validated_data.get("location", instance.location)
        instance.level = validated_data.get("level", instance.level)
        instance.audience = validated_data.get("audience", instance.audience)

        instance.save()
        return instance