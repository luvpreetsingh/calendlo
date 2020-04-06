# rest framework level imports
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# project level imports
from .serializers import AppointmentSerializer, AppointmentListSerializer
from .models import Appointment
from libs.constants import (
    INVALID_QUERY_PARAMS,
    SUCCESSFUL_APPOINTMENT,
)
from libs.utils import apply_query_params


class AppointmentViewSet(GenericViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializers = {
        "create": AppointmentSerializer,
        "list": AppointmentListSerializer,
    }

    def get_authenticators(self):
        if self.request.method == 'GET':
            return super().get_authenticators()
        else:
            return []

    def get_permissions(self):
        if self.request.method == 'GET':
            return super().get_permissions()
        else:
            return []

    def get_queryset(self):
        qs = self.request.user.get_appointments()
        query_params = dict(self.request.query_params)
        qs, self.calendlo_msg = apply_query_params(
            qs,
            query_params,
            ['date', 'appointee_email']
        )
        return qs

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(SUCCESSFUL_APPOINTMENT, status=status.HTTP_201_CREATED)

    # TODO: Fix list api
    def list(self, request, *args, **kwargs):
        appointments = self.get_serializer(self.get_queryset(), many=True).data
        response_dict = {'appointments': appointments}
        if self.calendlo_msg:
            response_dict['message'] = self.calendlo_msg
        return Response(response_dict)
