# Generated by Django 4.1.7 on 2023-06-13 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CATEGORYManager', '0002_maincategory_is_header'),
        ('PRODUCTManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productlist',
            name='mainCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CATEGORYManager.maincategory'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='subCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CATEGORYManager.subcategory'),
        ),
        migrations.AlterField(
            model_name='offerlist',
            name='end_date',
            field=models.CharField(blank=True, default='14 Jun, 2023', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='offerlist',
            name='start_date',
            field=models.CharField(blank=True, default='14 Jun, 2023', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='SubSubCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CATEGORYManager.subsubcategory'),
        ),
    ]
