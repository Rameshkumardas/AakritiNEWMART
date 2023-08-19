from PRODUCTManager.AJAXService import AJAXPRODUCT as AJAXService
from PRODUCTManager.AJAXService import PRODUCTImportExport, PRODUCTBULKAJAX
from PRODUCTManager import  PRODUCTManager as PRODUCT
from django.urls import path

urlpatterns = [

        # ==============================================================================
        # PRODUCT DISPLAY AREA
        # ==============================================================================
        path('ALLPRODUCTList/', PRODUCT.ALLPRODUCTList.as_view(), name='ALLPRODUCTList'),  
        # ==============================================================================
        # CRUD OPERATION ON PRODUCT 
        # ==============================================================================
        path('updatePRODUCT/<int:pk>/<slug>/', PRODUCT.updatePRODUCT, name='updatePRODUCT'),  
        # ==============================================================================
        # AJAXSERVICE CRUD OPERATION ON PRODUCT 
        # ==============================================================================
        path('AJAXService/PRODUCTOPERATION/AddProduct/', AJAXService.AddProduct, name='AddProduct'),  
        path('AJAXService/PRODUCTOPERATION/UPDATEGeneralInformation/', AJAXService.UPDATEGeneralInformation, name='UPDATEGeneralInformation'),  
        path('AJAXService/PRODUCTOPERATION/UPDATEPriceStockGSTSHIPPING/', AJAXService.UPDATEPriceStockGSTSHIPPING, name='UPDATEPriceStockGSTSHIPPING'),  
        path('AJAXService/PRODUCTOPERATION/UPDATEImage/', AJAXService.UPDATEImage, name='UPDATEImage'),  
        path('AJAXService/PRODUCTOPERATION/UPDATEMetaTag/', AJAXService.UPDATEMetaTag, name='UPDATEMetaTag'),  

        path('AJAXService/PRODUCTOPERATION/createATTRIBUTEPRODUCT/', AJAXService.createATTRIBUTEPRODUCT, name='createATTRIBUTEPRODUCT'),  
        path('AJAXService/PRODUCTOPERATION/createSIMILARRODUCT/', AJAXService.createSIMILARRODUCT, name='createSIMILARRODUCT'),  

# 

        path('AJAXService/PRODUCTOPERATION/ACTIVATEProduct/', AJAXService.ACTIVATEProduct, name='ACTIVATEProduct'),  
        path('AJAXService/PRODUCTOPERATION/DEACTIVATEProduct/', AJAXService.DEACTIVATEProduct, name='DEACTIVATEProduct'),  
        path('AJAXService/PRODUCTOPERATION/CLOSEDProduct/', AJAXService.CLOSEDProduct, name='CLOSEDProduct'),
        path('AJAXService/PRODUCTOPERATION/DELETEProduct/', AJAXService.DELETEProduct, name='DELETEProduct'),  
        path('AJAXService/PRODUCTOPERATION/BOOSTREQUESTFORTHISPRODUCT/', AJAXService.BOOSTREQUESTFORTHISPRODUCT, name='BOOSTREQUESTFORTHISPRODUCT'),  
        path('AJAXService/PRODUCTOPERATION/IMPORTProduct/', PRODUCTImportExport.PRODUCTImport, name='PRODUCTImport'),  
        path('AJAXService/PRODUCTOPERATION/EXPORTProduct/', PRODUCTImportExport.PRODUCTExport, name='PRODUCTExport'),  
        path('AJAXService/PRODUCTOPERATION/saveAsADraft/', AJAXService.saveAsADraft, name='saveAsADraft'),  
        path('AJAXService/PRODUCTOPERATION/saveANDunpublish/', AJAXService.saveANDunpublish, name='saveANDunpublish'),  
        # ==============================================================================
        # CART OPERATION 
        # ==============================================================================
        path('AJAXService/CARTOPERATION/ADDTOCART/', AJAXService.addTOCart, name='addTOCartThisProduct'),  
        # =================================END-SETTINGS=================================
        # =================================END-SETTINGS=================================
        # =================================END-SETTINGS=================================
        path('AJAXService/CARTOPERATION/addToWishlist/', AJAXService.addToWishlist, name='AddToWishlistThisProduct'),  
        # =================================END-SETTINGS=================================
        path('AJAXService/PRODUCT/SEARCHPRODUCTAJAXService/', AJAXService.SEARCHPRODUCTAJAXService, name='SEARCHPRODUCTAJAXService'),         
        # =================================END-SETTINGS=================================
        # =================================END-SETTINGS=================================
        # =================================END-SETTINGS=================================
        # =================================END-SETTINGS=================================
        path('AJAXService/FEEDBACK/AddFeedBack/', AJAXService.AddFeedBack, name='AddFeedBack'),  

        # ===========================================================================         
        path('AJAXService/BULK_ACTIVATE_PRODUCT/', PRODUCTBULKAJAX.BULK_ACTIVATE, name='BULK_ACTIVATE_PRODUCT'), 
        path('AJAXService/BULK_DEACTIVATE_PRODUCT/', PRODUCTBULKAJAX.BULK_DEACTIVATE, name='BULK_DEACTIVATE_PRODUCT'), 
        path('AJAXService/BULK_MOVE_TO_TRASH_PRODUCT/', PRODUCTBULKAJAX.BULK_MOVE_TO_TRASH, name='BULK_PRODUCT_MOVE_TO_TRASH_PRODUCT'), 
        path('AJAXService/BULK_RESTORE_FROM_TRASH_PRODUCT/', PRODUCTBULKAJAX.BULK_RESTORE_FROM_TRASH, name='BULK_PRODUCT_RESTORE_FROM_TRASH'), 
        path('AJAXService/BULK_PERMANENTLY_DELETE_PRODUCT/', PRODUCTBULKAJAX.BULK_PERMANENTLY_DELETE, name='BULK_PERMANENTLY_DELETE_PRODUCT'), 
        # ===========================================================================       


]
