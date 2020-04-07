from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, NotFound

from libs.constants import ERR_USER_DOES_NOT_EXIST, ERR_INVALID_PASSWORD
from .models import CalendloUser


class CreateUserSerializer(serializers.ModelSerializer):
    """
    """
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CalendloUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = CalendloUser
        fields = ('identifier', 'email', 'role', 'first_name', 'last_name', 'password')
        write_only_fields = ('password',)


class LoginSerializer(serializers.Serializer):

    identifier = serializers.CharField(max_length=32, write_only=True)
    password = serializers.CharField(max_length=32, write_only=True)

    def validate(self, data):
        try:
            user = CalendloUser.objects.get(identifier=data['identifier'])
        except CalendloUser.DoesNotExist:
            raise NotFound(ERR_USER_DOES_NOT_EXIST)

        is_password_correct = user.check_password(data['password'])

        if is_password_correct:
            token = user.access_token
            return {'token': token}
        else:
            raise AuthenticationFailed(ERR_INVALID_PASSWORD)
