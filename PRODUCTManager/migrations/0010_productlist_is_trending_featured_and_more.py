# Generated by Django 4.1.7 on 2023-06-23 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTManager', '0009_productlist_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='is_trending_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productlist',
            name='is_trending_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productlist',
            name='is_trending_top_sale',
            field=models.BooleanField(default=False),
        ),
    ]