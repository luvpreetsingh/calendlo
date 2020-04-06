from rest_framework import serializers
from rest_framework.exceptions import ParseError

from django.utils import timezone
from django.conf import settings

from .models import Appointment
from availability.models import AvailabilitySlot
from accounts.models import CalendloUser
from libs.constants import (
    ERR_USER_DOES_NOT_EXIST,
    ERR_INVALID_TIME_DURATION,
    ERR_INVALID_TIME_INTERVAL,
    ERR_USER_NOT_AVAILABLE,
)


class AppointmentSerializer(serializers.ModelSerializer):
    """
    """
    appointer = serializers.CharField(max_length=32)

    class Meta:
        model = Appointment
        fields = (
            'date',
            'start_time',
            'end_time',
            'appointer',
            'title',
            'appointee_name',
            'appointee_email',
            'description',
            )

    def validate_appointer(self, appointer):
        """
        This function validates the appointer field
        """
        try:
            return CalendloUser.objects.get(identifier=appointer)
        except CalendloUser.DoesNotExist:
            raise ParseError(ERR_USER_DOES_NOT_EXIST)

    def validate(self, data):
        duration = data['end_time'].hour - data['start_time'].hour

        if duration > 1:
            raise ParseError(ERR_INVALID_TIME_DURATION)
        elif duration < 1:
            raise ParseError(ERR_INVALID_TIME_INTERVAL)
        else:
            try:
                slot = data['appointer'].slots.get(
                    date=data['date'],
                    start_time=data['start_time']
                )
                if slot.is_booked:
                    raise ParseError(ERR_USER_NOT_AVAILABLE)
                data["slot"] = slot
            except AvailabilitySlot.DoesNotExist:
                raise ParseError(ERR_USER_NOT_AVAILABLE)
        return data

    def create(self, data):
        """
        Here data is coming after validation
        """
        appointment = Appointment.objects.create(**data)
        return appointment
