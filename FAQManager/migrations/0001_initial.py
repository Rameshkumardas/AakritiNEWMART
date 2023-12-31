# Generated by Django 4.2.2 on 2023-06-25 03:18

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, max_length=255, populate_from='name', unique=True)),
                ('img', models.ImageField(max_length=200, upload_to='FAQMainCat')),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, max_length=255, populate_from='name', unique=True)),
                ('description', models.TextField(default='Description is Required', max_length=6000)),
                ('is_draft', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('FAQCat', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='FAQManager.faqcategory')),
            ],
        ),
    ]
