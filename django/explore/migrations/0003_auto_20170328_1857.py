# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0002_auto_20170319_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieobj',
            name='budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movieobj',
            name='fblikes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movieobj',
            name='gross',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movieobj',
            name='numCritic',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movieobj',
            name='numReviews',
            field=models.IntegerField(null=True),
        ),
    ]