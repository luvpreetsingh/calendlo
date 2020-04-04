from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import CreateAvailabilitySlotSerializer

# Create your views here.


class AvailabilitySlotViewSet(GenericViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializers = {
        "create": CreateAvailabilitySlotSerializer,
    }

    def get_queryset(self):
        return AvailabilitySlot.objects.all()

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid() is False:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({'msg': 'Slot created successfully'}, status=status.HTTP_201_CREATED)
