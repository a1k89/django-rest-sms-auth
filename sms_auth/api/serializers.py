from django.contrib.auth import get_user_model
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

    def validate_new_phone_number(self, phone_number):
        if User.objects.filter(username=phone_number).exists():
            raise serializers.ValidationError(f'User with phone number {phone_number} already exist')

        return phone_number


class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'first_name',
            'last_name'
        ]