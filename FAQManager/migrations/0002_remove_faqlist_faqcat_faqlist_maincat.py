# Generated by Django 4.2.2 on 2023-06-25 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FAQManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqlist',
            name='FAQCat',
        ),
        migrations.AddField(
            model_name='faqlist',
            name='mainCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FAQManager.faqcategory'),
        ),
    ]
