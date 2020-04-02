from django.db import models

# Project Level Imports
from libs.models import CalendloBaseModel

# Create your models here.

class Appointment(CalendloBaseModel):
    """
    """
    user = models.ForeignKey('accounts.CalendloUser', on_delete=models.PROTECT, related_name='appointments')
    appointment_with = models.CharField(max_length=64)

    class __meta__:
        db_table = "calendlo_appointment"
