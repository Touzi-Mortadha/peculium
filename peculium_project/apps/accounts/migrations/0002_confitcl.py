# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiTCL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_tokens', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]