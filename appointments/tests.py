# python level imports
import datetime

# django level imports
from django.test import TestCase
from django.utils import timezone

# project level imports
from accounts.models import CalendloUser
from availability.models import AvailabilitySlot
from .models import Appointment


class CalendloUserTestCase(TestCase):

    def setUp(self):
        self.user = CalendloUser.objects.create(
            identifier="tom_the_cat_3",
            email="tom_the_cat@gmail.org"
        )
        date = timezone.now().date() + datetime.timedelta(5)
        start_time = datetime.time(hour=10, minute=0, second=0)
        self.slot = AvailabilitySlot.objects.create(
            date=date,
            start_time=start_time,
            user=self.user
        )
        self.title = "Meeting with Jerry"
        self.appointee_email = "jerry@gmail.com"
        self.appointee_name = "Jerry"
        self.description = "Resolve Conflicts"
        self.appointment = Appointment.objects.create(
            slot=self.slot,
            title=self.title,
            appointee_email=self.appointee_email,
            appointee_name=self.appointee_name,
            description=self.description
        )

    def test_user(self):
        self.assertTrue(Appointment._meta.db_table == 'calendlo_appointment')
        app_str = "For {} on {} at {} with {}".format(
            self.appointment.slot.user,
            self.appointment.slot.date,
            self.appointment.slot.start_time,
            self.appointment.appointee_name
        )
        self.assertTrue(self.appointment.__str__() == app_str)
