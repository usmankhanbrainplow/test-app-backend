# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-07 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=500, null=True)),
                ('product_quantity', models.CharField(default='', max_length=1000, null=True)),
                ('product_price', models.CharField(default=None, max_length=500, null=True)),
                ('product_description', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
    ]
