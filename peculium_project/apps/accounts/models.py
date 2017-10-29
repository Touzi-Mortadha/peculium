from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='userprofile', on_delete=models.CASCADE)
    adresse = models.CharField(max_length=100, blank=True)
    numero = models.IntegerField(blank=True, null=True)
    cin = models.IntegerField(blank=True, null=True)  # this one is temporary
    email_confirmed = models.BooleanField(default=False)
    public_rib= models.CharField(max_length=100, blank=True, null=True)
    banc_rib = models.CharField(max_length=100, blank=True, null=True)
    BTC_rib = models.CharField(max_length=100, blank=True, null=True)
    ETH_rib = models.CharField(max_length=100, blank=True, null=True)
    buy = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user.username)


class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='transactions')
    date_of_transaction = models.DateField()
    time_of_transaction = models.TimeField()
    amount_sent = models.FloatField(null=True, blank=True)
    TCL_assigned = models.FloatField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()

        # @receiver(post_save, sender=User)
        # def save_user_profile(sender, instance, **kwargs):
        #     UserProfile.objects.create(user=instance)
        #     instance.userprofile.save()
