# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-04-19 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200419_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
