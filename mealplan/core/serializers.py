from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class TagField(serializers.Field):
    """
    Tags are converted between a list and a comma-joined string
    """

    def to_representation(self, value):
        ''' data: comma-joined string or the empty string '''
        if type(value) != str:
            raise serializers.ValidationError("Tags must be saved as strings")
        if value and len(value) > 0:
            return value.split(',')
        else:
            return []

    def to_internal_value(self, data):
        ''' data: list(str) or comma-joined string '''
        if type(data) == str:
            return data
        if type(data) == list:
            return ",".join([x.strip() for x in data])
        raise serializers.ValidationError("Tags must be sent as a list")
