# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 09:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0041_auto_20170907_0827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'permissions': (('view_category', 'Can view categories'), ('edit_category', 'Can edit categories')), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('view_product', 'Can view products'), ('edit_product', 'Can edit products')), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='stocklocation',
            options={'permissions': (('view_stock_location', 'Can view stock location'), ('edit_stock_location', 'Can edit stock location'))},
        ),
    ]
