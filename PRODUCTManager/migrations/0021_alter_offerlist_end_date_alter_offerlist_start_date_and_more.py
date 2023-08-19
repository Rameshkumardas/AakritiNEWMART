# Generated by Django 4.2.2 on 2023-08-03 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CATEGORYManager', '0002_maincategory_is_header'),
        ('PRODUCTManager', '0020_productmycart_mrp_productmycart_sp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerlist',
            name='end_date',
            field=models.CharField(blank=True, default='03 Aug, 2023', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='offerlist',
            name='start_date',
            field=models.CharField(blank=True, default='03 Aug, 2023', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='SubSubCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CATEGORYManager.subsubcategory'),
        ),
    ]