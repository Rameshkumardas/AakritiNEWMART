from .AJAXService import SETTINGImportExport, AJAXService
from ExtraSettings import REQUIRMENTS, INISettings
from django.urls import path
from . import views


urlpatterns = [
    path('Email-Templates-Config/', views.EmailTemplateConfigs, name='EmailTemplateConfigs'),    
    path('Contact-US-List/', views.Notifications, name='Notifications'),  
    
    path('General-Settings/', views.GeneralSettings, name='GeneralSettings'),    
      
    # ================================AjaxServiceProvider=============================
    path('AjaxServiceProviderUpdateDetails/', AJAXService.UpdateDetails, name='UpdateDetails'),
    # path('AjaxServiceProviderUpdateTermsCondition/', AjaxServiceProvider.UpdateTermsCondition, name='UpdateTermsCondition'),
    # ================================End-AjaxServiceProvider=============================
    # ================================AJAXService=============================
    # ================================AJAXService=============================
    # ================================AJAXService=============================
    # ================================AJAXService=============================
    path('AJAXService/ExtraSetting/UpdatePROJECTInformation/', AJAXService.UpdatePROJECTInformation, name='UpdatePROJECTInformation'),
    path('AJAXService/ExtraSetting/UpdateLOGOANDICONS/', AJAXService.UpdateLOGOANDICONS, name='UpdateLOGOANDICONS'),

    path('AJAXService/ExtraSetting/UpdatePROJECPAYWithRAZORPAY/', AJAXService.UpdatePROJECPAYWithRAZORPAY, name='UpdatePROJECPAYWithRAZORPAY'),
    path('AJAXService/ExtraSetting/UpdatePROJECPAYWithPAYPAL/', AJAXService.UpdatePROJECPAYWithPAYPAL, name='UpdatePROJECPAYWithPAYPAL'),
    path('AJAXService/ExtraSetting/UpdateSMTPSettings', AJAXService.UpdateSMTPSettings, name='UpdateSMTPSettings'),
    path('AJAXService/ExtraSetting/UpdateNOReplySMTPSettings/', AJAXService.UpdateNOReplySMTPSettings, name='UpdateNOReplySMTPSettings'),
    path('AJAXService/ExtraSetting/UpdateSocailMedia/', AJAXService.UpdateSocailMedia, name='UpdateSocailMedia'),
    # ================================AJAXService=============================
    # ================================AJAXService=============================
    # ================================AJAXService=============================
    # ================================AJAXService=============================
    
    path('AJAXService/ExtraSetting/updateCHATGTPSettings/', AJAXService.updateCHATGTPSettings, name='updateCHATGTPSettings'),

    path('AJAXService/ExtraSetting/UpdateCHATBOTPSettings/', AJAXService.UpdateCHATBOTPSettings, name='UpdateCHATBOTSettings'),
    path('AJAXService/ExtraSetting/UpdateGOOGLEPSettings/', AJAXService.UpdateGOOGLEPSettings, name='UpdateGOOGLEPSettings'),
    path('AJAXService/ExtraSetting/UpdateMETASettings/', AJAXService.UpdateMETASettings, name='UpdateMETASettings'),
    # ===========================================================================   
    path('AJAXService/SETTINGImport/', SETTINGImportExport.SETTINGImport, name='SETTINGImport'), 
    path('AJAXService/SETTINGExport/', SETTINGImportExport.SETTINGExport, name='SETTINGExport'), 

    path('ExtraSettings/Create/Settings.in/', INISettings.CREATESettings, name='CREATESettings'), 
    path('ExtraSettings/CREATEREQUIRMENT_TXTSettings/', REQUIRMENTS.CREATEREQUIRMENT_TXTSettings, name='CREATEREQUIRMENT_TXTSettings'), 
]

