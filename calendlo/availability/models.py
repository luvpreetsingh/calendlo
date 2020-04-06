# python imports
import datetime

# django level imports
from django.db import models

# Project Level Imports
from libs.models import CalendloBaseModel
from libs.constants import HOUR_SET


class AvailabilitySlot(CalendloBaseModel):
    """
    This model class represents the availability of a user    
    """
    user = models.ForeignKey('accounts.CalendloUser', on_delete=models.PROTECT, related_name='slots')

    class __meta__:
        db_table = "calendlo_availability_slot"

    def get_appointment(self):
        """
        This function returns appointment related to a slot
        """
        try:
            return self.appointment
        except AvailabilitySlot.appointment.RelatedObjectDoesNotExist:
            return None

    @property
    def is_booked(self):
        """
        This function returns if the slot is booked or not
        """
        return True if self.get_appointment() else False            

    def __str__(self):
        """
        This functions returns the string form of a slot
        """
        return "{} on {} at {}".format(
            self.user,
            self.date,
            self.start_time,
        )

    @property
    def day(self):
        """
        This function returns the day name of the date
        """
        return self.date.strftime("%A")

    def delete_appointment(self):
        """
        This function deletes the appointment to a slot
        """
        appointment = self.get_appointment()
        if appointment:
            appointment.delete()

    @classmethod
    def create_slots(cls, user, date_list, start_time_set):
        """
        This classmethod creates slots on the dates given in date_list
        and hours given in start_time_set.
        """

        # generate a list of all hours on which no slot is needed
        inactive_slot_set = HOUR_SET - start_time_set
        for date in date_list:
            for time in list(start_time_set):
                start_time = datetime.time(hour=time, minute=0, second=0)
                try:
                    # checking if a slot is already available on given date
                    # and time
                    existing_slot = cls.objects.get(
                        user=user,
                        date=date,
                        start_time=start_time,
                    )
                except cls.DoesNotExist:
                    # if no slot is available on given date and time, then
                    # create new one
                    cls(user=user, date=date, start_time=start_time).save()
                else:
                    if existing_slot.is_active:
                        # if already available slot is active, then no need
                        #  to do anything.
                        pass
                    else:
                        # if already available is inactive, making it active
                        existing_slot.is_active = True
                        existing_slot.save()

            for time in list(inactive_slot_set):
                start_time = datetime.time(hour=time, minute=0, second=0)
                try:
                    # marking all the slots which are not needed as inactive
                    # and deleting the related appointment
                    existing_slot = cls.objects.get(
                        user=user,
                        date=date,
                        start_time=start_time,
                    )
                    existing_slot.is_active = False
                    existing_slot.save()
                    existing_slot.delete_appointment()
                except cls.DoesNotExist:
                    # if no slot exists, then do nothing
                    pass
