from rest_framework import serializers
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
        user = CalendloUser.objects.get(identifier=data['identifier'])
        passed = user.check_password(data['password'])
        token = user.access_token if user.access_token else ""
        return {'logged_in': passed, 'token': token}
