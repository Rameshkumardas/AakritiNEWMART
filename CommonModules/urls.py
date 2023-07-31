from django.urls import path

from CommonModules.AJAXService import COLORAJAXService, REGIONAJAXService, SHIPPINGAJAXService 
from CommonModules.AJAXService import COLORBULKAJAX, REGIONBULKAJAX, SHIPPINGBULKAJAX 
from CommonModules.AJAXService import COLORImportExport, REGIONImportExport, SHIPPINGImportExport
from . import views
urlpatterns = [
        # ==============================================================================
        # COLORS SETTINGS
        # ==============================================================================
        path('COLORList/', views.COLORManager, name='COLORList'), 
        path('updateCOLOR/<int:pk>/', views.updateCOLOR, name='updateCOLOR'), 
        path('AJAXService/createCOLOR/', COLORAJAXService.createCOLOR, name='createCOLOR'), 
        path('AJAXService/updateCOLORAJAX/', COLORAJAXService.updateCOLORAJAX, name='updateCOLORAJAX'), 
        path('AJAXService/activatedCOLOR/', COLORAJAXService.activatedCOLOR, name='activatedCOLOR'), 
        path('AJAXService/deactivatedCOLOR/', COLORAJAXService.deactivatedCOLOR, name='deactivatedCOLOR'), 
        path('AJAXService/deleteCOLOR/', COLORAJAXService.deleteCOLOR, name='deleteCOLOR'),
        # ==============================================================================
        # -------------------------------------------------------------------------------------------------------------------
        path('AJAXService/COLORImport/', COLORImportExport.COLORImport, name='COLORImport'), 
        path('AJAXService/COLORExport/', COLORImportExport.COLORExport, name='COLORExport'), 
        # ===========================================================================       
        path('AJAXService/BULK_ACTIVATE_COLOR/', COLORBULKAJAX.BULK_ACTIVATE_COLOR, name='BULK_ACTIVATE_COLOR'), 
        path('AJAXService/BULK_DEACTIVATE_COLOR/', COLORBULKAJAX.BULK_DEACTIVATE_COLOR, name='BULK_DEACTIVATE_COLOR'), 
        path('AJAXService/BULK_DELETE_COLOR/', COLORBULKAJAX.BULK_DELETE_COLOR, name='BULK_DELETE_COLOR'), 
        # ==============================================================================
        
        # ==============================================================================
        # REGION SETTINGS
        # ==============================================================================
        path('REGIONList/', views.REGIONList1, name='REGIONList'), 
        path('updateREGION/<int:pk>/', views.updateREGION, name='updateREGION'), 
        path('AJAXService/createREGION/', REGIONAJAXService.createREGION, name='createREGION'), 
        path('AJAXService/updateREGIONAJAX/', REGIONAJAXService.updateREGIONAJAX, name='updateREGIONAJAX'), 
        path('AJAXService/activatedREGION/', REGIONAJAXService.activatedREGION, name='activatedREGION'), 
        path('AJAXService/deactivatedREGION/', REGIONAJAXService.deactivatedREGION, name='deactivatedREGION'), 
        path('AJAXService/deleteREGION/', REGIONAJAXService.deleteREGION, name='deleteREGION'), 
        # ===========================================================================               
        path('AJAXService/REGIONImport/', REGIONImportExport.REGIONImport, name='REGIONImport'), 
        path('AJAXService/REGIONExport/', REGIONImportExport.REGIONExport, name='REGIONExport'), 
        # ===========================================================================       
        path('AJAXService/BULK_ACTIVATE_REGION/', REGIONBULKAJAX.BULK_ACTIVATE_REGION, name='BULK_ACTIVATE_REGION'), 
        path('AJAXService/BULK_DEACTIVATE_REGION/', REGIONBULKAJAX.BULK_DEACTIVATE_REGION, name='BULK_DEACTIVATE_REGION'), 
        path('AJAXService/BULK_DELETE_REGION/', REGIONBULKAJAX.BULK_DELETE_REGION, name='BULK_DELETE_REGION'), 
        # ===========================================================================       


        # ==============================================================================
        # SHIPPING SETTINGS
        # ==============================================================================
        path('SHIPPINGList/', views.SHIPPINGList1, name='SHIPPINGList'), 
        path('updateSHIPPING/<int:pk>/', views.updateSHIPPING, name='updateSHIPPING'), 
        path('AJAXService/createSHIPPING/', SHIPPINGAJAXService.createSHIPPING, name='createSHIPPING'), 
        path('AJAXService/updateSHIPPINGAJAX/', SHIPPINGAJAXService.updateSHIPPINGAJAX, name='updateSHIPPINGAJAX'), 
        path('AJAXService/activatedSHIPPING/', SHIPPINGAJAXService.activatedSHIPPING, name='activatedSHIPPING'), 
        path('AJAXService/deactivatedSHIPPING/', SHIPPINGAJAXService.deactivatedSHIPPING, name='deactivatedSHIPPING'), 
        path('AJAXService/deleteSHIPPING/', SHIPPINGAJAXService.deleteSHIPPING, name='deleteSHIPPING'), 
        # ===========================================================================               
        path('AJAXService/SHIPPINGImport/', SHIPPINGImportExport.SHIPPINGImport, name='SHIPPINGImport'), 
        path('AJAXService/SHIPPINGExport/', SHIPPINGImportExport.SHIPPINGExport, name='SHIPPINGExport'), 
        # ===========================================================================       
        path('AJAXService/BULK_ACTIVATE_SHIPPING/', SHIPPINGBULKAJAX.BULK_ACTIVATE_SHIPPING, name='BULK_ACTIVATE_SHIPPING'), 
        path('AJAXService/BULK_DEACTIVATE_SHIPPING/', SHIPPINGBULKAJAX.BULK_DEACTIVATE_SHIPPING, name='BULK_DEACTIVATE_SHIPPING'), 
        path('AJAXService/BULK_DELETE_SHIPPING/', SHIPPINGBULKAJAX.BULK_DELETE_SHIPPING, name='BULK_DELETE_SHIPPING'), 
        # ===========================================================================       

        # ==============================================================================
        # MORE SETTINGS
        # ==============================================================================
        
]
