# Generated by Django 4.1.7 on 2023-06-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMSManager', '0006_pagelist_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelist',
            name='is_product',
            field=models.BooleanField(default=False),
        ),
    ]
