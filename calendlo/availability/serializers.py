from rest_framework import serializers

from django.utils import timezone

import datetime

from .models import AvailabilitySlot

from django.conf import settings

class CreateAvailabilitySlotSerializer(serializers.ModelSerializer):
    """
    """

    days_in_week = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
    }

    day = serializers.CharField(max_length=12)

    class Meta:
        model = AvailabilitySlot
        fields = ('day', 'start_time', 'end_time',)

    def validate(self, data):
        if data['day'] not in self.days_in_week.keys():
            return "Exception"
        return data

    def next_day_occurence(self, current_date, weekday):
        days_ahead = weekday - current_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return current_date + datetime.timedelta(days_ahead)

    def create(self, data):
        """
        Here data is coming after validation
        """
        current_date = timezone.now()
        slot_end_time = data['end_time']
        slot_start_time = data['start_time']
        slot_creation_weekday = self.days_in_week[data["day"]]
        user = self.context['request'].user
        bulk_object_list = []
        for week in range(settings.NO_OF_WEEKS_TO_SCHEDULE):
            slot_date = self.next_day_occurence(current_date.date(), slot_creation_weekday)
            slot_date += datetime.timedelta(7 * week)
            for hour in range(slot_end_time.hour - slot_start_time.hour):
                start_time = slot_start_time.replace(hour=slot_start_time.hour + hour)
                bulk_object_list.append(AvailabilitySlot(
                    user=user,
                    date=slot_date,
                    start_time=slot_start_time.replace(hour=slot_start_time.hour + hour),
                    end_time=start_time.replace(hour=start_time.hour + 1)
                    ))

        AvailabilitySlot.objects.bulk_create(bulk_object_list)
        return bulk_object_list[0]
