# Generated by Django 4.1.7 on 2023-06-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtraSettings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinformation',
            name='tawk',
            field=models.TextField(blank=True, default='', max_length=6500, null=True),
        ),
    ]