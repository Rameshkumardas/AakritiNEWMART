# Generated by Django 4.1.7 on 2023-06-23 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTManager', '0008_rename_is_arrivals_productlist_is_arrivals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='label',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
