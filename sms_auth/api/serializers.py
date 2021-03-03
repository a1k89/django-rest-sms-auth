from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class EntrySerializer(serializers.Serializer):
    phone_number = PhoneNumberField()


class AuthSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()
    code = serializers.IntegerField()


class ChangePhoneNumberSerializer(serializers.Serializer):
    new_phone_number = PhoneNumberField()



class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'first_name',
            'last_name'
        ]