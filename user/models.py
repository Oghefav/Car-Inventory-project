from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomAdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)


    def __str__(self):
        return self.username