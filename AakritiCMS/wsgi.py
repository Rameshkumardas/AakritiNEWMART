"""
WSGI config for KHANTAILOR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
from decouple import config
import os
from django.core.wsgi import get_wsgi_application

if config("DEBUG") == False:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.Settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.Settings.local')

application = get_wsgi_application()


