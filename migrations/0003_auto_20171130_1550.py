# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_auto_20171129_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='prescription_details',
            field=models.CharField(max_length=1000),
        ),
    ]
