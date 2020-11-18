from rest_framework import serializers
from .models import Organisation
from users.serializers import CustomUserSerializer

class OrganisationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.ReadOnlyField(required=False)
    organisation = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=300)
    logo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    website = serializers.CharField(max_length=300)
    owner = serializers.ReadOnlyField(source="owner.username")

    def create(self, validated_data):
        return Organisation.objects.create(**validated_data)

class OrganisationDetailSerializer(OrganisationSerializer):
    users = CustomUserSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.organisation = validated_data.get("organisation", instance.organisation)
        instance.description = validated_data.get("description", instance.description)
        instance.logo = validated_data.get("logo", instance.logo)
        instance.website = validated_data.get("website", instance.website)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.slug = validated_data.get("slug", instance.slug)

        instance.save()
        return instance

