# Generated by Django 4.1.7 on 2023-05-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommonModules', '0010_alter_colorlist_date_alter_regionlist_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorlist',
            name='date',
            field=models.CharField(blank=True, default='11, May - 2023', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='regionlist',
            name='date',
            field=models.CharField(blank=True, default='11, May - 2023', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='shippinglist',
            name='date',
            field=models.CharField(blank=True, default='11, May - 2023', max_length=15, null=True),
        ),
    ]
