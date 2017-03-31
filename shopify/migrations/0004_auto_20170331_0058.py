# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0003_auto_20170330_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_discounts',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]