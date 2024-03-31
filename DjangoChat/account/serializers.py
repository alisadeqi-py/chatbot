from rest_framework import serializers
from .models import CustomeUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class signUpSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomeUser
        fields = ('email', 'password', 'password1')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password']:
            raise serializers.ValidationError({"message": "password not match"})
        try:
            validate_password(attrs['password1'])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(({'password': list(e.messages)}))
        return super().validate(attrs)

    def create(self, validate_data):
        validate_data.pop('password1', None)
        return CustomeUser.objects.create(**validate_data)
