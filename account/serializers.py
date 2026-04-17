from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import AuthUser


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = AuthUser.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginResponseSerializer(serializers.Serializer):

    @staticmethod
    def get_token(user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def to_representation(self, instance):
        token_data = self.get_token(instance)
        return {
            "access_token": token_data["access"],
            "refresh_token": token_data["refresh"],
            "email": instance.email,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "full_name": instance.full_name,
        }

