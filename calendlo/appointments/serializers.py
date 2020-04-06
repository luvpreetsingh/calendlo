# rest_framework level imports
from rest_framework import serializers
from rest_framework.exceptions import (
    NotFound,
    ValidationError,
)

# project level imports
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
    start_time = serializers.TimeField()
    date = serializers.DateField()

    class Meta:
        model = Appointment
        fields = (
            'date',
            'start_time',
            'appointer',
            'title',
            'appointee_name',
            'appointee_email',
            'description',
            )

    def validate_appointer(self, appointer):
        """
        This function validates the appointer field.
        """
        try:
            return CalendloUser.objects.get(identifier=appointer)
        except CalendloUser.DoesNotExist:
            raise NotFound(ERR_USER_DOES_NOT_EXIST)

    def validate(self, data):
        """
        This function validates all of the serializer data and returns 
        a dict of the validated data.
        """
        try:
            slot = data['appointer'].slots.get(
                is_active=True,
                date=data['date'],
                start_time=data['start_time']
            )
            if slot.is_booked:
                raise ValidationError(ERR_USER_NOT_AVAILABLE)
            data["slot"] = slot
        except AvailabilitySlot.DoesNotExist:
            raise ValidationError(ERR_USER_NOT_AVAILABLE)

        # removing fields not related to appointment model
        data.pop('date')
        data.pop('start_time')
        data.pop('appointer')

        return data

    def create(self, data):
        """
        This function runs when serializer.save() is called.
        Here data is coming after validation.
        """
        appointment = Appointment.objects.create(**data)
        return appointment
