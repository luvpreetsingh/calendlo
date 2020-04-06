# python imports
import datetime

# django level imports
from django.utils import timezone
from django.conf import settings

# rest framework level imports
from rest_framework import serializers
from rest_framework.exceptions import ValidationError as RValidationError

# third party level imports
from marshmallow import ValidationError

# project level imports
from .models import AvailabilitySlot
from libs.constants import (
    DAYS_IN_WEEK,
    ERR_INVALID_DAY,
    ERR_INVALID_TIME_INTERVAL
)
from libs.utils import next_day_occurence, increment_hour
from .schemas import TimingSchema


class CreateAvailabilitySlotSerializer(serializers.Serializer):

    payload = serializers.JSONField()

    def validate_payload(self, data):
        """
        validating the payload using Marshmallow schema
        """
        for day, timings in data.items():
            if day not in DAYS_IN_WEEK.keys():
                raise RValidationError(ERR_INVALID_DAY)
            else:
                try:
                    data[day] = TimingSchema().load(timings)
                except ValidationError:
                    raise RValidationError(ERR_INVALID_TIME_INTERVAL)
        return data

    def create(self, data):
        for day, timings in data['payload'].items():
            current_date = timezone.now().date()
            weekday = DAYS_IN_WEEK[day]

            dates_list = []
            for week in range(settings.NO_OF_WEEKS_TO_SCHEDULE):
                next_date = next_day_occurence(current_date, weekday)
                dates_list.append(next_date)
                current_date = next_date

            slots_list = []
            for slot in timings['timings']:
                slot_iter = range(slot['start_time'].hour, slot['end_time'].hour)
                slots_list += [hour for hour in slot_iter]

            AvailabilitySlot.create_slots(
                user=self.context['request'].user,
                date_list=dates_list,
                start_time_set=set(slots_list),
            )

        return AvailabilitySlot()


class ListAvailabilitySlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailabilitySlot
        fields = (
            'date',
            'start_time',
            )
