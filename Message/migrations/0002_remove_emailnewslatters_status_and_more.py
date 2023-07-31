# Generated by Django 4.1.7 on 2023-06-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailnewslatters',
            name='status',
        ),
        migrations.RemoveField(
            model_name='mobilenewslatters',
            name='status',
        ),
        migrations.AddField(
            model_name='emailnewslatters',
            name='is_subscribed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='emailnewslatters',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mobilenewslatters',
            name='is_subscribed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mobilenewslatters',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]