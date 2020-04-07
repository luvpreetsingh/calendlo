# python level imports
import datetime

# django level imports
from django.test import TestCase
from django.utils import timezone

# project level imports
from .models import AvailabilitySlot
from accounts.models import CalendloUser
from appointments.models import Appointment
from libs.constants import DAYS_IN_WEEK


class AvailabilitySlotTestCase(TestCase):

    def setUp(self):
        self.identifier = "tom_the_catto"
        self.email = "tom_the_cat@gmail.in"
        self.user = CalendloUser.objects.create(
            identifier=self.identifier,
            email=self.email
        )
        self.date_1 = timezone.now().date() + datetime.timedelta(3)
        self.date_2 = timezone.now().date() + datetime.timedelta(4)
        self.start_time = datetime.time(hour=9, minute=0, second=0)
        self.slot_1 = AvailabilitySlot.objects.create(
            date=self.date_1,
            start_time=self.start_time,
            user=self.user
        )
        self.slot_2 = AvailabilitySlot.objects.create(
            date=self.date_2,
            start_time=self.start_time,
            user=self.user
        )
        self.appointment = Appointment.objects.create(
            slot=self.slot_1,
            title="Meeting with Jerry",
            appointee_email="jerry@gmail.com",
            appointee_name="Jerry",
            description="Resolve Conflicts"
        )

    def test_slot(self):
        self.assertTrue(AvailabilitySlot._meta.db_table == 'calendlo_availability_slot')
        unique_together = list(map(list, AvailabilitySlot._meta.unique_together))
        self.assertTrue(unique_together == [['date', 'start_time']])
        self.assertTrue(self.slot_1.is_booked is True)
        self.assertTrue(self.slot_2.is_booked is False)
        self.assertTrue(self.slot_1.__str__() == "{} on {} at {}".format(
            self.identifier,
            self.date_1,
            self.start_time
            )
        )
        self.assertTrue(isinstance(self.slot_1.get_appointment(), Appointment))
        self.assertTrue(self.slot_2.get_appointment() is None)
        self.assertTrue(self.slot_1.day in DAYS_IN_WEEK.keys())
        self.assertTrue(
            isinstance(self.slot_1.delete_appointment(), Appointment)
        )
        self.assertTrue(self.slot_2.delete_appointment() is None)

        with self.assertRaises(Appointment.DoesNotExist):
            # appointment has been deleted in the above test
            Appointment.objects.get(slot=self.slot_1)
