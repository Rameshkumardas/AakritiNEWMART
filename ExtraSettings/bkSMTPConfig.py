from ExtraSettings.models import PROJECTInformation
from django.conf import settings

def config_smtp_credential_support():
    try:
        conf = PROJECTInformation.objects.last()
        if conf != None:
            settings.EMAIL_HOST = conf.EMAIL_HOST
            settings.EMAIL_HOST_USER = conf.EMAIL_HOST_USER
            settings.EMAIL_HOST_PASSWORD = conf.EMAIL_HOST_PASSWORD
            settings.EMAIL_PORT = conf.EMAIL_PORT
            settings.EMAIL_USE_TLS = conf.EMAIL_USE_TLS
        return True
    except Exception as e:
        print("Error:",e)

def config_smtp_credential_no_reply():
    try:
        conf = PROJECTInformation.objects.last()
        if conf != None:
            settings.EMAIL_HOST = conf.EMAIL_HOST_NO_REPLY
            settings.EMAIL_HOST_USER = conf.EMAIL_HOST_USER_NO_REPLY
            settings.EMAIL_HOST_PASSWORD = conf.EMAIL_HOST_PASSWORD_NO_REPLY
            settings.EMAIL_PORT = conf.EMAIL_PORT_NO_REPLY
            settings.EMAIL_USE_TLS = conf.EMAIL_USE_TLS_NO_REPLY
        return True
    except Exception as e:
        print("Error:",e)