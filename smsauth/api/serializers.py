from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class EntrySerializer(serializers.Serializer):
    phone_number = PhoneNumberField()


class AuthSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()
    code = serializers.IntegerField()
