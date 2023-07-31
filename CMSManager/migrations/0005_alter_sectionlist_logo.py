# Generated by Django 4.1.7 on 2023-04-29 18:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('CMSManager', '0004_alter_sectionlist_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionlist',
            name='logo',
            field=tinymce.models.HTMLField(blank=True, default='logo', max_length=6000, null=True),
        ),
    ]
