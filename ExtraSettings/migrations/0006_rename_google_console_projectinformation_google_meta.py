# Generated by Django 4.1.7 on 2023-06-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExtraSettings', '0005_alter_projectinformation_chatgtp_api_key_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectinformation',
            old_name='google_console',
            new_name='google_meta',
        ),
    ]
