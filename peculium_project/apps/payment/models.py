from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class ConfiTCL(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_PCL = models.IntegerField(blank=True, null=True)
    PCL_amount = models.FloatField(blank=True, null=True)