from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import AppointmentSerializer
from .models import Appointment
from libs.paginators import CalendloLimitOffsetPagination
from libs.constants import INVALID_QUERY_PARAMS, SUCCESSFUL_APPOINTMENT

# Create your views here.


class AppointmentViewSet(GenericViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializers = {
        "create": AppointmentSerializer,
        "list": AppointmentSerializer,
    }

    calendlo_msg = None

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
        qs = self.request.user.appointments.all()
        query_params = self.request.query_params
        if len(query_params) == 0:
            pass
        else:
            for param, value in query_params.items():
                # allowing filtering only on date and email
                if 'date' or 'appointee_email' in param:
                    try:
                        qs = eval("qs.filter({}={})".format(param, value))
                    except Exception:
                        self.calendlo_msg = INVALID_QUERY_PARAMS
        return qs

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() is False:
            raise ParseError(dict(serializer.errors))
        else:
            serializer.save()
            return Response(SUCCESSFUL_APPOINTMENT, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        appointments = self.get_serializer(self.get_queryset(), many=True).data
        response_dict = {'appointments': appointments}
        if self.calendlo_msg:
            response_dict['message'] = self.calendlo_msg
        return Response(response_dict)
