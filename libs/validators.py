# django level imports
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_absolute_hour(value):
    """
    This function validates if the given value is an absolute hour
    otherwise it raises an error
    """
    if (value.minute != 0) or (value.second != 0) or (value.microsecond != 0):
        raise ValidationError(
            _('{} is not an absolute hour'.format(value))
            )
