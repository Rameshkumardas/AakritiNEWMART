# Generated by Django 4.1.7 on 2023-06-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOGManager', '0003_alter_bloglist_maincat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='description',
            field=models.TextField(max_length=6500),
        ),
    ]
