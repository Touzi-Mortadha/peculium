# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_transaction_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount_sent',
            field=models.FloatField(blank=True, null=True),
        ),
    ]