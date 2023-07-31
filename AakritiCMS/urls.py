from decouple import config
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from AdminAuthentication import AdminLogin
from AakritiCMS.Settings import live, local
from django.contrib.auth import views as auth_views
from AakritiMART import ERRORHandler 


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('paypal/', include("paypal.standard.ipn.urls")),
    path('auth/', include('Accounts.urls')), 
    path('admin/', AdminLogin.NORMALADMINLogin, name='NORMALADMINLogin'),  
    path('', include('AakritiMART.urls')), 
    # ==========================================================
    path('CATEGORYManager/', include('CATEGORYManager.urls')),
    path('Message/', include('Message.urls')),
    path('CommonModules/', include('CommonModules.urls')),
    path('PRODUCTManager/', include('PRODUCTManager.urls')),
    path('RCRManager/', include('RCRManager.urls')),
    path('SALESManager/', include('SALESManager.urls')),
    path('REFUNDManager/', include('REFUNDManager.urls')),
    # ==========================================================
    path('', include('BLOGManager.homeURL')),
    path('BLOGManager/', include('BLOGManager.urls')),
    # ==========================================================
    # ==========================================================
    # ==========================================================
    # ==========================================================
    path('FAQManager/', include('FAQManager.urls')),
    path('SLIDERManager/', include('SLIDERManager.urls')),
    path('TESTIMONAILManager/', include('TESTIMONAILManager.urls')),
    # ==========================================================
    # ==========================================================
    path('AdminAuthentication/', include('AdminAuthentication.urls')),
    path('STAFFManager/', include('AdminAuthentication.staffURL')),
    path('USERMAnager/', include('AdminAuthentication.userURL')),
    # ==========================================================
    # ==========================================================
    path('Dashboard/', include('Dashboard.urls')),    
    path('ExtraSettings/', include('ExtraSettings.urls')),    
    # ==========================================================
    # ==========================================================
    path('tinymce/', include('tinymce.urls')),
    # ==========================================================
    # ==========================================================
    # ==========================================================
    path('', include('BRANDManager.homeURL')),
    path('BRANDManager/', include('BRANDManager.urls')),
    # ==========================================================
    # ==========================================================
    path('', include('CMSManager.homeURL')),
    path('CMSManager/', include('CMSManager.urls')),
    # ==========================================================
    # ==========================================================
    path('BULKEMAILManager/', include('BULKEMAILManager.urls')),

]

handler400 = 'AakritiMART.ERRORHandler.ERROR400'
handler403 = 'AakritiMART.ERRORHandler.ERROR403'
handler404 = 'AakritiMART.ERRORHandler.ERROR404'
handler500 = 'AakritiMART.ERRORHandler.ERROR500'

if config("DEBUG") != False:
    urlpatterns +=static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)
else:
    urlpatterns += static(live.MEDIA_URL, document_root=live.MEDIA_ROOT)
    
urlpatterns+=path('__debug__/', include('debug_toolbar.urls')),
