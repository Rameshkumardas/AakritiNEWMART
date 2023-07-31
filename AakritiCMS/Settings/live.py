
from decouple import config
from .common import *
import os
# STATIC_PRODUCTION_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'public_html/aakriticms.com/'))
STATIC_PRODUCTION_DIR = BASE_DIR
# DATABASES SETTINGS
# =============================================================================
# =============================================================================
DATABASES = {  
        'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': f'{config("DB_NAME")}dB',  
        'USER': f'{config("DB_USER")}',  
        'PASSWORD': f'{config("DB_PASSWORD")}',
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        }  
    } 
# ==============================================================================
# ==============================================================================
# STATIC SETTINGS
# ==============================================================================
# ==============================================================================
STATIC_URL = 'static/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(STATIC_PRODUCTION_DIR, '../static')]
else:
    STATIC_ROOT = os.path.join(STATIC_PRODUCTION_DIR, '../static')
# ==============================================================================
# ==============================================================================
# MEDIA SETTINGS
# ==============================================================================
# ==============================================================================
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(STATIC_PRODUCTION_DIR, "../media/")
