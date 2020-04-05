from django.contrib import admin

from .models import Appointment
# Register your models here.

@admin.register(Appointment)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = (
        'appointer',
        'date',
        'start_time',
        'end_time',
        'appointee_name',
        'appointee_email',
        'title',
        'slot',
        )
