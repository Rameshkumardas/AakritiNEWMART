# Generated by Django 4.1.7 on 2023-05-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BULKEMAILManager', '0004_emaillist_is_sent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillist',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]
