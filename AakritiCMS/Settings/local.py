from decouple import config
from .common import *
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / f'../{config("PROJECT_NAME")}dB.db',
    }    
}
# DATABASES SETTINGS
# =============================================================================
# =============================================================================
# DATABASES = {  
#         'default': {  
#         'ENGINE': 'django.db.backends.mysql',  
#         'NAME': f'{config("DB_NAME")}dB',  
#         'USER': f'{config("DB_USER")}',  
#         'PASSWORD': f'{config("DB_PASSWORD")}',
#         'HOST': '127.0.0.1',  
#         'PORT': '3306',  
#         }  
#     } 
# ==============================================================================
# STATIC SETTINGS
# ==============================================================================
STATIC_URL = 'static/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, '../static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, '../static')
    # STATIC_ROOT = os.path.join('/home/tdipbnvp/public_html/static')

# ==============================================================================
# MEDIA SETTINGS
# ==============================================================================
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "../media/")

# MEDIA_ROOT = os.path.join("/home/tdipbnvp/public_html/media/")










INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True,
}

# ==============================================================================
# DEBUG_TOOLBAR_PANELS
# ==============================================================================
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.history.HistoryPanel',
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
# ]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True,
}

ENABLE_STACKTRACES = True
ENABLE_STACKTRACES_LOCALS= False
# ==============================================================================
# END DEBUG_TOOLBAR_PANELS
# ==============================================================================
