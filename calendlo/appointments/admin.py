# django imports
from django.contrib import admin

# project level imports
from .models import Appointment


@admin.register(Appointment)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = (
        'appointee_name',
        'appointee_email',
        'title',
        'slot',
        )
