from rest_framework import serializers

from django.utils import timezone
from django.conf import settings

import datetime

from .models import Appointment
from accounts.models import CalendloUser

class CreateAppointmentSerializer(serializers.ModelSerializer):
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
        appointer = CalendloUser.objects.get(identifier=appointer)
        return appointer

    def validate(self, data):
        duration = data['end_time'].hour - data['start_time'].hour

        if duration > 1:
            return "only for 1 hour error"
        elif duration < 1:
            return "end_time cannot be less than start_time"
        else:
            slot_on_date = data['appointer'].slots.filter(date=data['date'])
            if slot_on_date.exists():
                slot = slot_on_date.get(start_time=data['start_time'])
                data['slot'] = slot
        return data

    def create(self, data):
        """
        Here data is coming after validation
        """
        appointment = Appointment.objects.create(**data)
        return appointment
