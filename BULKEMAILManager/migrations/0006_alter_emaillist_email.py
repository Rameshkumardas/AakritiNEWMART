# Generated by Django 4.1.7 on 2023-05-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BULKEMAILManager', '0005_alter_emaillist_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillist',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
