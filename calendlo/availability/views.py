# rest framework leve imports
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, NotFound

# project level imports
from libs.constants import SUCCESSFUL_SLOT_CREATION
from accounts.models import CalendloUser
from .serializers import CreateAvailabilitySlotSerializer, ListAvailabilitySlotSerializer
from libs.utils import apply_query_params
from libs.constants import (
    ERR_USER_DOES_NOT_EXIST,
    ERR_USERNAME_NOT_PROVIDED,
)


class AvailabilitySlotViewSet(GenericViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializers = {
        "create": CreateAvailabilitySlotSerializer,
        "list": ListAvailabilitySlotSerializer,
    }

    def get_authenticators(self):
        if self.request.method == 'POST':
            return super().get_authenticators()
        else:
            return []

    def get_permissions(self):
        if self.request.method == 'POST':
            return super().get_permissions()
        else:
            return []

    def get_queryset(self):
        query_params = dict(self.request.query_params)
        try:
            identifier = query_params.pop('user')[0]
            user = CalendloUser.objects.get(identifier=identifier)
        except KeyError:
            raise ParseError(ERR_USERNAME_NOT_PROVIDED)
        except CalendloUser.DoesNotExist:
            raise NotFound(ERR_USER_DOES_NOT_EXIST)

        qs = user.slots.filter(
            appointment__isnull=True,
            is_active=True
        )

        qs, self.calendlo_msg = apply_query_params(
            qs,
            query_params,
            ['date'] # query param filtering will only work for date field
        )
        return qs

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(SUCCESSFUL_SLOT_CREATION, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        slots = self.get_serializer(self.get_queryset(), many=True).data
        response_dict = {'slots': slots}
        if self.calendlo_msg:
            response_dict['msg'] = self.calendlo_msg
        return Response(response_dict)
