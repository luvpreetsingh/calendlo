from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    """
    TimeStampedModel is an abstract model to add following fields in every
    model where it is inherited.
      - created_at
      - updated_at
      - is_active
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CalendloBaseModel(TimeStampedModel, models.Model):
    """
    CalendloBaseModel is an abstract model to add following fields in every
    model where it is inherited.
      - date
      - start_time
      - end_time
    """
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        abstract = True

    @property
    def duration(self):
        return self.start_time - self.end_time
    