from django.db import models


class PROJECTInformation(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default='AakritiCMS')
    title = models.CharField(max_length=255, null=True, blank=True, default='CMS Develop By Mr Das : Ramesh Kuamr Das')

    baseURL = models.CharField(max_length=255, null=True, blank=True, default='https://www.aakriticms.com')

    mail = models.EmailField(max_length=255, null=True, blank=True, default='das82916@gmail.com')
    contact = models.CharField(max_length=255, null=True, blank=True, default='7322057677')
    address = models.CharField(max_length=255, null=True, blank=True, default='Siraha-21 Laminiya Siraha Prov. No 2 ( NEPAL ) ')

    SECRET_KEY = models.TextField(max_length=6500, null=True, blank=True, default='django-insecure-ps(#7dz8ul@wc2^17te7x904fb2zsqka1@tic84rgaa%o62i7o')
    DEBUG = models.BooleanField(default=True)

    ALLOWED_HOSTS = models.TextField(max_length=6500, null=True, blank=True, default='*')

    description = models.TextField(max_length=6500, null=True, blank=True, default='No More Description')

    headerLogo = models.ImageField(max_length=200, upload_to="PROJECT/Logo", blank=False, null=False)
    footerLogo = models.ImageField(max_length=200, upload_to="PROJECT/Logo", blank=False, null=False)
    favicon = models.ImageField(max_length=200, upload_to="PROJECT/Logo", blank=False, null=False)

    EMAIL_HOST = models.CharField(max_length=255, default='smtp.gmail.com')
    EMAIL_HOST_USER = models.CharField(max_length=255, default='das82916@gmail.com')
    EMAIL_HOST_PASSWORD = models.CharField(max_length=255, default='rdnrwyrubxutgbgu')
    EMAIL_PORT = models.IntegerField(default=587)
    EMAIL_USE_TLS = models.BooleanField(default=True)

    EMAIL_HOST_NO_REPLY = models.CharField(max_length=255, default='smtp.gmail.com')
    EMAIL_HOST_USER_NO_REPLY = models.CharField(max_length=255, default='das82916@gmail.com')
    EMAIL_HOST_PASSWORD_NO_REPLY = models.CharField(max_length=255, default='rdnrwyrubxutgbgu')
    EMAIL_PORT_NO_REPLY = models.IntegerField(default=587)
    EMAIL_USE_TLS_NO_REPLY = models.BooleanField(default=True)

    RAZORPAY_PAY_ACTIVE = models.BooleanField(default=False)
    RAZORPAY_API_KEY = models.CharField(max_length=255, null=True, blank=True, default='rzp_test_2zQpTbSjs2CVX0')
    RAZORPAY_API_SECRET = models.CharField(max_length=255, null=True, blank=True, default='B5fjrvSJXJSXjfm8wymFZA8e')

    PAYPAL_PAY_ACTIVE = models.BooleanField(default=False)
    PAYPAL_API_KEY = models.CharField(max_length=255, default='AQq4VESxR1hUfAGBVSuD3IXH5TF0LpF1Ixm9Mr5CesX5Gydce3qna5nC01Z0hPkgr_fYgmHu5BZF3UOo')
    PAYPAL_API_SECRET = models.CharField(max_length=255, default='')

    facebook = models.CharField(max_length=255, null=True, blank=True, default='')
    vimeo = models.CharField(max_length=255, null=True, blank=True, default='')
    youtube = models.CharField(max_length=255, null=True, blank=True, default='')
    linkedin = models.CharField(max_length=255, null=True, blank=True, default='')
    pintrest = models.CharField(max_length=255, null=True, blank=True, default='')
    twitter = models.CharField(max_length=255, null=True, blank=True, default='')
    instagram = models.CharField(max_length=255, null=True, blank=True, default='')


    support_email = models.CharField(max_length=255, null=True, blank=True, default='')
    support_contact = models.CharField(max_length=255, null=True, blank=True, default='')
    support_address = models.CharField(max_length=255, null=True, blank=True, default='')

    PrivacyPolicy = models.CharField(max_length=255, null=True, blank=True, default='')
    TermsCondition = models.CharField(max_length=255, null=True, blank=True, default='')
    Security = models.CharField(max_length=255, null=True, blank=True, default='')
    Disclaimer = models.CharField(max_length=255, null=True, blank=True, default='')
    CopyrightPolicy = models.CharField(max_length=255, null=True, blank=True, default='')
    AboutUS = models.CharField(max_length=255, null=True, blank=True, default='')
    ContactUS = models.CharField(max_length=255, null=True, blank=True, default='')


    google_developer_token = models.CharField(max_length=255, null=True, blank=True, default='XeDIz1WJMrfnfVLj64eWbQ')
    google_use_proto_plus = models.BooleanField(default=True)
    google_client_id = models.TextField(max_length=6500, null=True, blank=True, default='101916302276-2t1ck3crpurqti7n3s65kq2n4vpg9tkt.apps.googleusercontent.com')
    google_secret_key = models.CharField(max_length=255, null=True, blank=True, default='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')    
    google_refresh_token = models.CharField(max_length=255, null=True, blank=True, default='1//0gzZbBrO0ykh-CgYIARAAGBASNwF-L9IrPSsJLmtv6IlsHAQuz89kqUTNAHZMj_v3LJ62o_RXpoUSw-WeXu4JYuh_nRKvfpBrO1Y')
    google_login_customer_id = models.CharField(max_length=255, null=True, blank=True, default='1684377039')


    google_analytics = models.TextField(max_length=6500, null=True, blank=True, default='')
    google_meta = models.TextField(max_length=6500, null=True, blank=True, default='')

    tawk = models.TextField(max_length=6500, null=True, blank=True, default='')

    ChatGTP_API_KEY = models.TextField(max_length=6500, null=True, blank=True, default='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')
        
    meta_title = models.TextField(max_length=6500, null=True, blank=True, default='Meta title ')
    meta_keywords = models.TextField(max_length=6500, null=True, blank=True, default='Meta keywords')
    meta_description = models.TextField(max_length=6500, null=True, blank=True, default='Meta description')
    keing_tag = models.TextField(max_length=6500, null=True, blank=True, default='Meta ')
