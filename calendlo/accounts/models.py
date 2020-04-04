# Django Level Imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator, EmailValidator

# Project Level Imports
from libs.models import TimeStampedModel
from .constants import ACCOUNT_ROLES, USER_IDENTIFIER_REGEX
from .managers import CalendloUserManager

# Other imports
from rest_framework.authtoken.models import Token

# Here goes the models.


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
        validators=[EmailValidator]
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
