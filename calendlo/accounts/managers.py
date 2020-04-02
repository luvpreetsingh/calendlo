# django imports
from django.contrib.auth.models import BaseUserManager


class CalendloUserManager(BaseUserManager):
    def create_user(self, identifier, password=None, **extra_fields):
        """
        Creates and saves a User with the given identifier and password
        """
        if not identifier:
            raise ValueError('A User must have an identifier')

        user = self.model(
            identifier=identifier,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identifier, password, **extra_fields):
        """
        Creates and saves a superuser with the given identifier and password.
        """
        user = self.create_user(
            identifier,
            password=password,
            **extra_fields
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
