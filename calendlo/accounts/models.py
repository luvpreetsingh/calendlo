# Django Level Imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils import timezone

# rest_framework level imports
from rest_framework.authtoken.models import Token

# Project Level Imports
from libs.models import TimeStampedModel
from libs.constants import ACCOUNT_ROLES, USER_IDENTIFIER_REGEX
from .managers import CalendloUserManager
from appointments.models import Appointment


class CalendloUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    """
    identifier = models.CharField(
        max_length=32,
        unique=True,
        help_text="Your unique identifier on Calendlo",
        validators=[RegexValidator(
            regex=USER_IDENTIFIER_REGEX,
            message="identifier can only have alphanumeric and _"
            )]
        )
    email = models.EmailField(
        max_length=128,
        unique=True,
        )
    role = models.CharField(choices=ACCOUNT_ROLES, max_length=4, default='OTH')
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CalendloUserManager()

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['email']

    class __meta__:
        db_table = "calendlo_user"

    @property
    def access_token(self):
        token = Token.objects.get_or_create(user=self)
        return token[0].key

    def __str__(self):
        return "{}".format(self.identifier)

    def get_appointments(self):
        """
        This function returns upcoming appointments of a user
        """
        current_date = timezone.now().date()
        filled_slots = self.slots.filter(
            appointment__isnull=False,
            date__gte=current_date
        )
        appointment_ids = filled_slots.values_list('appointment', flat=True)
        qs = Appointment.objects.filter(id__in=appointment_ids)
        return qs
