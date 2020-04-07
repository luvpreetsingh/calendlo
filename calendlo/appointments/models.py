# django level imports
from django.db import models

# Project Level Imports
from libs.models import TimeStampedModel


class Appointment(TimeStampedModel):
    """
    """
    slot = models.OneToOneField('availability.AvailabilitySlot', on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    appointee_name = models.CharField(max_length=128)
    appointee_email = models.EmailField(max_length=128)
    description = models.TextField()

    class Meta:
        db_table = "calendlo_appointment"

    def __str__(self):
        return "For {} on {} at {} with {}".format(
            self.slot.user,
            self.slot.date,
            self.slot.start_time,
            self.appointee_name
        )
