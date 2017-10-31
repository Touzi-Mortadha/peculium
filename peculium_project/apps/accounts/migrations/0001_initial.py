# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 20:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_transaction', models.DateField()),
                ('time_of_transaction', models.TimeField()),
                ('amount_sent', models.FloatField(blank=True, null=True)),
                ('TCL_assigned', models.FloatField()),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(blank=True, max_length=100)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('cin', models.IntegerField(blank=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('public_rib', models.CharField(blank=True, max_length=100, null=True)),
                ('banc_rib', models.CharField(blank=True, max_length=100, null=True)),
                ('BTC_rib', models.CharField(blank=True, max_length=100, null=True)),
                ('ETH_rib', models.CharField(blank=True, max_length=100, null=True)),
                ('buy', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.UserProfile'),
        ),
    ]
