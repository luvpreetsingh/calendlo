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
