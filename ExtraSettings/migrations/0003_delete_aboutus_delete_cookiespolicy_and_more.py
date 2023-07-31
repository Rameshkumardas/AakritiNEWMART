# Generated by Django 4.1.7 on 2023-06-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtraSettings', '0002_projectinformation_tawk'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutUS',
        ),
        migrations.DeleteModel(
            name='CookiesPolicy',
        ),
        migrations.DeleteModel(
            name='CopyrightPolicy',
        ),
        migrations.DeleteModel(
            name='Disclaimer',
        ),
        migrations.DeleteModel(
            name='HowitWorks',
        ),
        migrations.DeleteModel(
            name='HowToShopOnline',
        ),
        migrations.DeleteModel(
            name='Maintenance',
        ),
        migrations.DeleteModel(
            name='OurFabrics',
        ),
        migrations.DeleteModel(
            name='OurGarmentQuality',
        ),
        migrations.DeleteModel(
            name='PerfectFitGuarantee',
        ),
        migrations.DeleteModel(
            name='PrivacyPolicy',
        ),
        migrations.DeleteModel(
            name='RCRPolicy',
        ),
        migrations.DeleteModel(
            name='Security',
        ),
        migrations.DeleteModel(
            name='TermCondition',
        ),
        migrations.DeleteModel(
            name='Weddings',
        ),
        migrations.AlterField(
            model_name='projectinformation',
            name='baseURL',
            field=models.CharField(blank=True, default='https://www.aakriticms.com', max_length=255, null=True),
        ),
    ]
