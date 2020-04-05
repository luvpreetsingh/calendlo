from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status


from .serializers import CreateAppointmentSerializer
from .models import Appointment
# Create your views here.


class AppointmentViewSet(GenericViewSet):

    serializers = {
        "create": CreateAppointmentSerializer,
    }

    def get_queryset(self):
        return Appointment.objects.all()

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() is False:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({'msg': 'Appointment created successfully'}, status=status.HTTP_201_CREATED)
