# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_public_rib'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='buy',
            field=models.BooleanField(default=False),
        ),
    ]