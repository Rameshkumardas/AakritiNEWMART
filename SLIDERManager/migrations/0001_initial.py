# Generated by Django 4.2.2 on 2023-06-24 18:16

import autoslug.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CMSManager', '0007_pagelist_is_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='BANNERCatList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BANNERList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('target', models.CharField(max_length=225)),
                ('title', models.CharField(blank=True, default='', max_length=225, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=225, null=True)),
                ('img', models.ImageField(blank=True, default='', max_length=200, null=True, upload_to='SLIDER/BANNERS/IMG/')),
                ('is_video', models.BooleanField(default=False)),
                ('is_youtube', models.BooleanField(default=False)),
                ('is_vimeo', models.BooleanField(default=False)),
                ('is_local', models.BooleanField(default=False)),
                ('local_video', models.FileField(default='', null=True, upload_to='SLIDER/BANNERS/VIDEO/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('is_draft', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('BANNERCat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SLIDERManager.bannercatlist')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMSManager.pagelist')),
            ],
        ),
    ]
