from django.shortcuts import render


from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError

from .serializers import CreateUserSerializer, LoginSerializer
from .models import CalendloUser
from libs.constants import SUCCESSFUL_SIGNUP



class CalendloUserViewSet(GenericViewSet):

    serializers = {
        "create": CreateUserSerializer,
        "login": LoginSerializer,
    }

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(SUCCESSFUL_SIGNUP, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path='login', detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data)
