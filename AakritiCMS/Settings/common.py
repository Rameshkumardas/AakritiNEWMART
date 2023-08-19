from django.urls import reverse_lazy
from decouple import config
from pathlib import Path
import os
# ==============================================================================
# DIR SETTINGS
# ==============================================================================
BASE_DIR = Path(__file__).resolve().parent.parent
# =============================================================================
# =============================================================================
# SERVER HOSTING SETTINGS
# =============================================================================
# =============================================================================
DEBUG = True
ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(',')
# =============================================================================
# =============================================================================
# ==============================================================================
# SETTINGS.INI SETUP
# ==============================================================================
SECRET_KEY = config("SECRET_KEY")
ROOT_URLCONF = f'{config("PROJECT_NAME")}.urls'
WSGI_APPLICATION = f'{config("PROJECT_NAME")}.wsgi.application'
ASGI_APPLICATION = f'{config("PROJECT_NAME")}.asgi.application'
# ==============================================================================
# DEFAULT APPS SETTINGS
# ==============================================================================
INSTALLED_DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# ==============================================================================
# THIRD PARTY APPS SETTINGS
# ==============================================================================
INSTALLING_THIRD_PARTY_APPS = [
    'django_cleanup.apps.CleanupConfig',
    'django.contrib.sitemaps',
    'django.contrib.sites', 
    'paypal.standard.ipn',
    'django_social_share',
    'rest_framework',
    'rest_framework.authtoken',
    'import_export',
    'django_crontab',
    'tinymce',  
    'debug_toolbar',

]

# ==============================================================================
# CUSTOM APPS SETTINGS
# ==============================================================================
INSTALLING_CUSTOM_APPS = [

        'AdminAuthentication',
        'Accounts',
        'Dashboard',
        'BLOGManager',
        'ExtraSettings',
        
        'CATEGORYManager',
        'CommonModules',
        'PRODUCTManager',
        'RCRManager',
        'SALESManager',
        'REFUNDManager',
        'Message',
        'FAQManager',
        'SLIDERManager',
        'TESTIMONAILManager',        
        'BRANDManager',
        'CMSManager',
        'BULKEMAILManager',
        #HOME
        'AakritiMART',
        # 'eCommerce',
    ]

PAYPAL_TEST = True
# ==============================================================================
# INSTALL APP SETTINGS
# ==============================================================================
INSTALLED_APPS = INSTALLED_DEFAULT_APPS+INSTALLING_THIRD_PARTY_APPS+INSTALLING_CUSTOM_APPS
# ==============================================================================
# END APP INSTALLATION SETTINGS
# ==============================================================================
# ==============================================================================
# ==============================================================================
SITE_ID = 1
# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'ExtraSettings.middleware.MRDasDeveloper',
    # 'ExtraSettings.middleware.PROJECTInformationMiddleWare', 
    #Add Debug Toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                # ADMIN INTERFACE
                os.path.join(BASE_DIR, './../Accounts'),
                os.path.join(BASE_DIR, './../AdminAuthentication'),
                os.path.join(BASE_DIR, './../Dashboard'),
                os.path.join(BASE_DIR, './../template'),
                os.path.join(BASE_DIR, './../BLOGManager'),
                os.path.join(BASE_DIR, './../ExtraSettings'),

                os.path.join(BASE_DIR, './../CATEGORYManager'),
                os.path.join(BASE_DIR, './../CommonModules'),
                os.path.join(BASE_DIR, './../PRODUCTManager'),
                os.path.join(BASE_DIR, './../RCRManager'),
                os.path.join(BASE_DIR, './../SALESManager'),
                os.path.join(BASE_DIR, './../REFUNDManager'),
                os.path.join(BASE_DIR, './../Message'),

                os.path.join(BASE_DIR, './../FAQManager'),
                os.path.join(BASE_DIR, './../SLIDERManager'),
                os.path.join(BASE_DIR, './../TESTIMONAILManager'),

 
                 os.path.join(BASE_DIR, './../BRANDManager'),

                 os.path.join(BASE_DIR, './../CMSManager'),
                 os.path.join(BASE_DIR, './../BULKEMAILManager'),

                # WEBSITE INTERFACE 
                os.path.join(BASE_DIR, './../AakritiMART'),
                os.path.join(BASE_DIR, './../eCommerce'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'ExtraSettings.PROJECTInformation_context_processors.PROJECTInformations',
            'CATEGORYManager.MainCatList_context_processors.mainCatList',
            'BLOGManager.BLOGMainCatList_context_processors.BLOGmainCatList',
            # 'eCommerce.MyCartList_context_processors.MyCartList',
            # 'eCommerce.MyCartList_context_processors.CountMyCart',
            'AakritiMART.allCOUNT_context_processors.allWISHCOUNT',
            'AakritiMART.allCOUNT_context_processors.allCARTCOUNT',
            'AakritiMART.allCOUNT_context_processors.allCARTList',            
            'django.template.context_processors.request',
            'CMSManager.SECTIONList_context_processors.HEADERSECTIONList',
            'CMSManager.SECTIONList_context_processors.FOOTERSECTIONList',
            # 'CMSManager.SECTIONList_context_processors.MOBILESECTIONList',

            ],
        },
    },
]

# ==============================================================================
# SESSION SETTINGS
# ==============================================================================
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 8*60*60*60
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'AdminLogOut'
# ==============================================================================
# DATETIME SETTINGS
# ==============================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# ==============================================================================
# EXTRA SETTINGS
# ==============================================================================
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ====================================================
IMPORT_EXPORT_USE_TRANSACTIONS = True
# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================
EMAIL_USE_TLS=''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT=''
EMAIL_BACKEND = ''
# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================
# ==============================================================================
# PAYPAL SETTINGS
# ==============================================================================
PAYPAL_API_KEY = ''
PAYPAL_API_SECRET = ''
PAYPAL_TEST = ''
# ==============================================================================
# PAYTM SETTINGS
# ==============================================================================
# PAYTM_COMPANY_NAME = "Company Name"   # For representation purposes 
# PAYTM_INDUSTRY_TYPE_ID = "Retail"     # For staging environment
# PAYTM_CHANNEL_ID = "WEB"
# PAYTM_MERCHANT_KEY = "your_merchant_key"
# PAYTM_MERCHANT_ID = "your_merchant_id"
# PAYTM_CALLBACK_URL = "http://localhost:8000/response/" # Hardcode
# PAYTM_WEBSITE = "WEBSTAGING"
# PAYTM_PAYMENT_GATEWAY_URL = "https://securegw-stage.paytm.in/order/process"
# PAYTM_TRANSACTION_STATUS_URL = "https://securegw-stage.paytm.in/order/status"
# ------------------------------------------------------------------------------
PAYTM_MERCHANT_COMPANY_NAME = "RAMESH KUMAR DAS"
PAYTM_CHANNEL_ID = "WEB"
PAYTM_EMAIL  = "das82916@gmail.com"
PAYTM_MOBILE = "7322057677"
PAYTM_STAGING = True
if PAYTM_STAGING:
    PAYTM_MERCHANT_KEY = "<YOUR-STAGING-MERCHANT-KEY>"
    PAYTM_INDUSTRY_TYPE_ID = "Retail"
    PAYTM_MERCHANT_ID = "ucliRd55339186982337"
    PAYTM_CALLBACK_URL = "http://localhost:8000/wallet/response/" if DEBUG else "http://www.yourwebsite.com/wallet/response/"
    PAYTM_WEBSITE = "WEB_STAGING"
    PAYTM_TRANSACTION_STATUS_URL = "https://pguat.paytm.com/oltp/HANDLER_INTERNAL/TXNSTATUS"
    PAYTM_PAYMENT_GATEWAY_URL = "https://pguat.paytm.com/oltp-web/processTransaction"
else:
    PAYTM_MERCHANT_KEY = "<YOUR-LIVE-MERCHANT-KEY>"
    PAYTM_MERCHANT_ID = "ucliRd55339186982337"
    PAYTM_CALLBACK_URL = "<YOUR-LIVE-CALLBACK-URL>"
    PAYTM_INDUSTRY_TYPE_ID = "Retail92"
    PAYTM_WEBSITE = "<PAYTM-WEBSITE-ID>"
    PAYTM_TRANSACTION_STATUS_URL = "https://secure.paytm.in/oltp/HANDLER_INTERNAL/TXNSTATUS"
    PAYTM_PAYMENT_GATEWAY_URL = "https://secure.paytm.in/oltp-web/processTransaction"
# ==============================================================================
# RAZORPAY SETTINGS
# ==============================================================================
RAZORPAY_API_KEY = ''
RAZORPAY_API_SECRET = ''
RAZORPAY_IS_ACTIVE = ''
# ==============================================================================
# MORE DEFAULT SETTINGS
# ==============================================================================
DATA_UPLOAD_MAX_NUMBER_FIELDS = None
# ==============================================================================
# REST FRAMEWORK SETTINGS
# ==============================================================================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated', 'rest_framework.permissions.AllowAny',],
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication', 'oauth2_provider.contrib.rest_framework.OAuth2Authentication', 'drf_social_oauth2.authentication.SocialAuthentication',],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15,
}
# ==============================================================================
# AUTHENTICATION BACKENDS SETTINGS
# ==============================================================================
AUTH_USER_MODEL = f'AdminAuthentication.AdminRegistration'
AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.AllowAllUsersModelBackend',
        'django.contrib.auth.backends.ModelBackend',
        'Accounts.backends.LoginWithEmailBackend',
        'AdminAuthentication.backends.CaseInsensitiveModelBackend',
    ]

# 'student_management_app.EmailBackEnd.EmailBackEnd',   
# This Error: No module named 'Accounts.EmailBackend'
# ==============================================================================
# IMPORT EXPORT SETTINGS
# ==============================================================================
IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = False
IMPORT_EXPORT_CHUNK_SIZE = 100
IMPORT_EXPORT_SKIP_ADMIN_CONFIRM = True
IMPORT_EXPORT_ESCAPE_OUTPUT_ON_EXPORT = False
# ==============================================================================
# IMPORT EXPORT SETTINGS
# ==============================================================================

# ==============================================================================
# CRON JOBS
# ==============================================================================
CRONJOBS = [
    ('*/10 * * * *', 'KHANTAILOR.cron.delete_my_activity')
]

