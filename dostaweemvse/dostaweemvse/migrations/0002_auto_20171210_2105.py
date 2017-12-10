# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-10 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dostaweemvse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edge',
            name='end_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location2', to='dostaweemvse.Location'),
        ),
        migrations.AlterField(
            model_name='edge',
            name='start_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location1', to='dostaweemvse.Location'),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location3', to='dostaweemvse.Location'),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location4', to='dostaweemvse.Location'),
        ),
    ]