from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from organisations.models import Organisation


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    is_invited = serializers.ReadOnlyField()
    organisation = serializers.SlugRelatedField('organisation', queryset=Organisation.objects.all())

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.organisation = validated_data.get("organisation", instance.organisation)
        instance.save()
        return instance