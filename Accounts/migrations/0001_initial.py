# Generated by Django 4.1.7 on 2023-04-21 06:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='emailOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Email Example@gmail.com Allowed.', regex='^\\+?1?\\d{9,15}$')])),
                ('Vcode', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mobileOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pNumber', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Vcode', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shippingADDRESS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scode', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('shouse_no', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('slandmark', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('scolony', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('scity', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sstate', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('scountry', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('more', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BILLINGADDRESS', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='billingADDRESS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bcode', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('bhouse_no', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('blandmark', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('bcolony', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('bcity', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('bstate', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('bcountry', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('more', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SHIPPINGADDRESS', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
