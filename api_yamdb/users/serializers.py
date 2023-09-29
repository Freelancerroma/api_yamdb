from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from users.models import User


def userandauthvalidate(data):
    if data['username'] == 'me':
        raise serializers.ValidationError(
            'me - недопустимое имя пользователя!'
        )
    if User.objects.filter(username=data['username']).exists():
        raise serializers.ValidationError(
            'Username уже существует!'
        )
    if User.objects.filter(email=data['email']).exists():
        raise serializers.ValidationError(
            'Email уже используется!'
        )


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        max_length=256,
        required=True
    )

    def validate(self, data):
        userandauthvalidate(data)
        return data

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )
        model = User


class UserDetailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        max_length=256,
        required=True
    )

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )
        model = User


class UserMeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        max_length=256,
        required=True
    )
    role = serializers.CharField(
        required=False,
        read_only=True
    )

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )
        model = User


class AuthSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        max_length=256,
        required=True
    )

    def validate(self, data):
        userandauthvalidate(data)
        return data

    class Meta:
        fields = ('email', 'username',)
        model = User


class AuthTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=256,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=20,
        required=True
    )

    def validate(self, data):
        user = get_object_or_404(
            User,
            username=data['username']
        )
        if user.confirmation_code != data['confirmation_code']:
            raise serializers.ValidationError(
                'Неверный код подтверждения!'
            )
        return data

    class Meta:
        fields = ('username', 'confirmation_code',)
        model = User
