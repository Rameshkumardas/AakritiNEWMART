# Generated by Django 4.1.7 on 2023-06-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtraSettings', '0007_projectinformation_google_client_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinformation',
            name='google_client_id',
            field=models.TextField(blank=True, default='101916302276-2t1ck3crpurqti7n3s65kq2n4vpg9tkt.apps.googleusercontent.com', max_length=6500, null=True),
        ),
        migrations.AlterField(
            model_name='projectinformation',
            name='google_developer_token',
            field=models.CharField(blank=True, default='XeDIz1WJMrfnfVLj64eWbQ', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectinformation',
            name='google_login_customer_id',
            field=models.CharField(blank=True, default='1684377039', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectinformation',
            name='google_refresh_token',
            field=models.CharField(blank=True, default='1//0gzZbBrO0ykh-CgYIARAAGBASNwF-L9IrPSsJLmtv6IlsHAQuz89kqUTNAHZMj_v3LJ62o_RXpoUSw-WeXu4JYuh_nRKvfpBrO1Y', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectinformation',
            name='google_secret_key',
            field=models.CharField(blank=True, default='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', max_length=255, null=True),
        ),
    ]
