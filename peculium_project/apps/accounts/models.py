from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=100, blank=True)
    numero = models.IntegerField(blank=True, null=True)
    cin = models.IntegerField(blank=True, null=True)  # this one is temporary
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     UserProfile.objects.create(user=instance)
#     instance.userprofile.save()