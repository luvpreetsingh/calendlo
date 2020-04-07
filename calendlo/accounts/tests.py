# python level imports
import datetime

# django level imports
from django.test import TestCase
from django.utils import timezone
from django.db.models.query import QuerySet

# project level imports
from .models import CalendloUser
from availability.models import AvailabilitySlot
from appointments.models import Appointment


class CalendloUserTestCase(TestCase):

    def setUp(self):
        self.user = CalendloUser.objects.create(
            identifier="tom_the_cat",
            email="tom_the_cat@gmail.com"
        )
        date = timezone.now().date() + datetime.timedelta(2)
        start_time = datetime.time(hour=10, minute=0, second=0)
        self.slot = AvailabilitySlot.objects.create(
            date=date,
            start_time=start_time,
            user=self.user
        )
        self.appointment = Appointment.objects.create(
            slot=self.slot,
            title="Meeting with Jerry",
            appointee_email="jerry@gmail.com",
            appointee_name="Jerry",
            description="Resolve Conflicts"
        )

    def test_user(self):
        self.assertTrue(isinstance(self.user, CalendloUser))
        self.assertTrue(CalendloUser._meta.db_table, 'calendlo_user')
        self.assertTrue(isinstance(self.user.access_token, str))
        self.assertTrue(isinstance(self.user.get_appointments(), QuerySet))
        for app in self.user.get_appointments():
            self.assertTrue(isinstance(app, Appointment))
