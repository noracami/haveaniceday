# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-31 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
