from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, blank=True, null=True)  # Job Role
    company = models.CharField(max_length=255, blank=True, null=True)  # User's Company
