# django level imports
from django.contrib import admin

# project level imports
from .models import AvailabilitySlot


@admin.register(AvailabilitySlot)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'start_time',
        'day',
        'is_active',
        'is_booked',
        )
