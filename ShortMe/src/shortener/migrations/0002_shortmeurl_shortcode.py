# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-03 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortmeurl',
            name='shortcode',
            field=models.CharField(default='defaultvalue', max_length=15),
            preserve_default=False,
        ),
    ]