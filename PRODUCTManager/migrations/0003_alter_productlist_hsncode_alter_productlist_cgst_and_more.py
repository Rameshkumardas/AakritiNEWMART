# Generated by Django 4.1.7 on 2023-06-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTManager', '0002_productlist_author_productlist_maincat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='HSNCode',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='cgst',
            field=models.FloatField(blank=True, default=9.0, null=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='igst',
            field=models.FloatField(blank=True, default=18.0, null=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='sgst',
            field=models.FloatField(blank=True, default=9.0, null=True),
        ),
    ]
