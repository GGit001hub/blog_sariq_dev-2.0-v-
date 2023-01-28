from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    manzil = models.CharField(max_length=50,null=True, blank=True)
    ismi = models.CharField(max_length=60,null=True, blank=True)

