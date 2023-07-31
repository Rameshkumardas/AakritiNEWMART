from ExtraSettings.models import PROJECTInformation
from django.conf import settings
from math import log, floor

def CONFIG_SMTP_SUPPORT():
    try:
        conf = PROJECTInformation.objects.last()
        if conf != None:
            settings.EMAIL_HOST = conf.EMAIL_HOST
            settings.EMAIL_HOST_USER = conf.EMAIL_HOST_USER
            settings.EMAIL_HOST_PASSWORD = conf.EMAIL_HOST_PASSWORD
            settings.EMAIL_PORT = conf.EMAIL_PORT
            settings.EMAIL_USE_TLS = conf.EMAIL_USE_TLS
        if conf.DEBUG == True:
            settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            return True
        elif conf.DEBUG == False:
            settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            return True
        else:
            settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            return True
    except Exception as e:
        print("Error:",e)

def CONFIG_SMTP_NO_REPLY():
    try:
        conf = PROJECTInformation.objects.last()
        if conf != None:
            settings.EMAIL_HOST = conf.EMAIL_HOST_NO_REPLY
            settings.EMAIL_HOST_USER = conf.EMAIL_HOST_USER_NO_REPLY
            settings.EMAIL_HOST_PASSWORD = conf.EMAIL_HOST_PASSWORD_NO_REPLY
            settings.EMAIL_PORT = conf.EMAIL_PORT_NO_REPLY
            settings.EMAIL_USE_TLS = conf.EMAIL_USE_TLS_NO_REPLY
        if conf.DEBUG == True:
            settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            return True
        elif conf.DEBUG == False:
            settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            return True
        else:
            settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            return True
    except Exception as e:
        print("Error:", e)


def CONVERT_NUMBER(count, *args, **kwargs):
        if(count>1000):
            units = ['', 'K', 'M', 'G', 'T', 'P']
            k = 1000.0
            magnitude = int(floor(log(count, k)))
            return '%.2f%s' % (count / k**magnitude, units[magnitude])
        else:
            return count