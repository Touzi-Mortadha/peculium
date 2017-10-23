from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class ConfiTCL(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_tokens = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)