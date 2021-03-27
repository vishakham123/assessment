from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

class User(PermissionsMixin, AbstractBaseUser):
    first_name = models.CharField(max_length=256, blank=False, unique=True)
    last_name = models.CharField(max_length=256, blank=False)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    USERNAME_FIELD = 'first_name'