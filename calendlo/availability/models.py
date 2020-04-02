# django level imports
from django.db import models

# Project Level Imports
from libs.models import CalendloBaseModel

# Create your models here.

class AvailabilitySlot(CalendloBaseModel):
    """
    """
    user = models.ForeignKey('accounts.CalendloUser', on_delete=models.PROTECT, related_name='slots')

    class __meta__:
        db_table = "calendlo_availability_slot"

    @property
    def is_booked(self):
        from django.core.exceptions import ObjectDoesNotExist
        try:
            self.appointment
            return True
        except ObjectDoesNotExist:
            return False
