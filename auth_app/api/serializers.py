import re
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for the registration."""


    confirmed_password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "confirmed_password"]


    def validate_username(self, value):
        """Validate the username length and raise a error, if the given username is to short."""
                
        
        if len(value) < 3:
            raise serializers.ValidationError(detail="The name must have at least 3 characters.")
        return value
    

    def validate_email(self, value):
        """Validate the email and raise a error, if the given email already exist."""


        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(detail="A user with this email already exist.")
        return value


    def validate_password(self, value):
        """Validate the password and raise a error, if the given password is to short."""


        if len(value) < 6 or not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$", value):
            raise serializers.ValidationError(detail="Minimum 6 characters, 1 x A-Z, 1 x a-z and 1 x 0-9")
        return value


    def validate(self, data):
        """Validate the provided attributes."""


        password = data["password"]
        confirmed_password = data["confirmed_password"]
        if password != confirmed_password:
            raise serializers.ValidationError("The passwords do not match.")
        return data
        

    def create(self, validated_data):
        """Create and returns a new model instance using the validated data."""


        validated_data.pop("confirmed_password", None)
        return User.objects.create_user(**validated_data)
    

class UserInfoSerializer(serializers.ModelSerializer):
    """Serializer for the user infos."""


    class Meta:
        model = User
        fields = ["id", "username", "email"] 