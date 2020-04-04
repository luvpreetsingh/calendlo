from django.shortcuts import render


from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


from .serializers import CreateUserSerializer, LoginSerializer
from .models import CalendloUser

# Create your views here.


class CalendloUserViewSet(GenericViewSet):

    serializers = {
        "create": CreateUserSerializer,
        "login": LoginSerializer,
    }

    def get_queryset(self):
        return CalendloUser.objects.all()

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() is False:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({'msg': 'Sign up Successful'}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path='login', detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() is False:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.validated_data['logged_in'] is False:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            if serializer.validated_data['logged_in'] is True:
                serializer.validated_data.pop('logged_in')
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
