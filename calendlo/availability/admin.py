from django.contrib import admin

from .models import AvailabilitySlot
# Register your models here.

@admin.register(AvailabilitySlot)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'start_time',
        'end_time',
        'day'
        )
