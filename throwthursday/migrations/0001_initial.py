# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Throw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('points', models.IntegerField()),
                ('matchdone', models.BooleanField()),
            ],
        ),
    ]
