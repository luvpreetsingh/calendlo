# Django Level Imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Project Level Imports
from libs.models import TimeStampedModel
from .constants import ACCOUNT_ROLES
from .managers import CalendloUserManager

# Here goes the models.


class CalendloUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    """
    identifier = models.CharField(max_length=32, unique=True, help_text="Your unique identifier on Calendlo")
    email = models.EmailField(max_length=128, unique=True, null=True)
    role = models.CharField(choices=ACCOUNT_ROLES, max_length=4, default='OTH')
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    objects = CalendloUserManager()

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = []

    class __meta__:
        db_table = "calendlo_user"
