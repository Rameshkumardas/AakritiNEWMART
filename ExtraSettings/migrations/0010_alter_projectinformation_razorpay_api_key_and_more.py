# Generated by Django 4.2.2 on 2023-06-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtraSettings', '0009_projectinformation_vimeo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinformation',
            name='RAZORPAY_API_KEY',
            field=models.CharField(blank=True, default='rzp_test_2zQpTbSjs2CVX0', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectinformation',
            name='RAZORPAY_API_SECRET',
            field=models.CharField(blank=True, default='B5fjrvSJXJSXjfm8wymFZA8e', max_length=255, null=True),
        ),
    ]
