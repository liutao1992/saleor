# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0035_auto_20170906_0806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('view', 'View Products in Dashboard'), ('edit', 'Edit Product in Dashboard')), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
