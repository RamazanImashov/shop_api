from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model, authenticate
from .utils import send_activation_code


User = get_user_model()


class RegisterSerializer(ModelSerializer):
    password_confirm = CharField(min_length=4, required=True)

    class Meta:
        model = User
        fields = 'email', 'password', 'password_confirm'

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise ValidationError(
                'Password not confirm'
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


class LoginSerializer(ModelSerializer):
    email = CharField(required=True)
    password = CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise ValidationError(
                'User not found'
            )
        return email

    def validate(self, attrs):
        request = self.context.get('request')
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password, request=request)

            if not user:
                raise ValidationError(
                    'Error email or password'
                )

        else:
            raise ValidationError(
                'Email and password obazatelno'
            )

        attrs['user'] = user
        return attrs
