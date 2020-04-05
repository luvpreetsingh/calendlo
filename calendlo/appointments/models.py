from django.db import models

# Project Level Imports
from libs.models import CalendloBaseModel

# Create your models here.

class Appointment(CalendloBaseModel):
    """
    """
    appointer = models.ForeignKey('accounts.CalendloUser', on_delete=models.PROTECT, related_name='appointments')
    slot = models.OneToOneField('availability.AvailabilitySlot', on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    appointee_name = models.CharField(max_length=128)
    appointee_email = models.EmailField(max_length=128)
    description = models.TextField()

    class __meta__:
        db_table = "calendlo_appointment"

    def __str__(self):
        return "{} on {} at {} with {}".format(self.appointer, self.date, self.start_time, self.appointee_name)
