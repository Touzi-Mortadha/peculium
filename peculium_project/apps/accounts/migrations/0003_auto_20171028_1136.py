# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='time_of_transaction',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_of_transaction',
            field=models.DateField(),
        ),
    ]
