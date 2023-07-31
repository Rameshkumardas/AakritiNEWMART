from django.urls import path
from CATEGORYManager import views, manageMainCategory, manageSubCategory, manageSubSubCategory

from CATEGORYManager.AJAXService import MAINCATBULKAJAX, SUBCATBULKAJAX, SUBSUBCATBULKAJAX, MainCatImportExport, SubCatImportExport, SubSubCatImportExport

urlpatterns = [

                    path('', manageMainCategory.CreateMainCategory, name='MainCategory'),       
                    path('MainCategory/', manageMainCategory.CreateMainCategory, name='createMainCategory'), 
                    path('deletemainCat/<int:pk>/', manageMainCategory.DeleteMainCategory, name='DeleteMainCategory'),
                    path('updatemainCat/<int:pk>/', manageMainCategory.UpdateMainCategory, name='UpdateMainCategory'),
                    path('copymainCat/<int:pk>/', manageMainCategory.CopyMainCategory, name='CopyMainCategory'),
                    path('ActivatedmainCat/<int:pk>/', manageMainCategory.ActivatedMainCategory, name='ActivatedMainCategory'),
                    path('DeactivatedmainCat/<int:pk>/', manageMainCategory.DeactivatedMainCategory, name='DeactivatedMainCategory'),
                    path('ActiveHeaderMainCategory/<int:pk>/', manageMainCategory.ActiveHeaderMainCategory, name='ActiveHeaderMainCategory'),                    
                    path('DeactiveHeaderMainCategory/<int:pk>/', manageMainCategory.DeactiveHeaderMainCategory, name='DeactiveHeaderMainCategory'),                    

                    # ====================AJAX SERVECE===========================
                    path('AJAXService/CRUDOperation/DELETEMainCat/', manageMainCategory.DELETEMainCat, name='DELETEMainCat'),
                    # -------------------------------------------------------------------------------------------------------------------
                    path('AJAXService/MainCatImport/', MainCatImportExport.MainCatImport, name='MainCatImport'), 
                    path('AJAXService/MainCatExport/', MainCatImportExport.MainCatExport, name='MainCatExport'), 
                    # ===========================================================================       
                    path('AJAXService/BULK_ACTIVATE_MAIN_CATEGORY/', MAINCATBULKAJAX.BULK_ACTIVATE_MAIN_CATEGORY, name='BULK_ACTIVATE_MAIN_CATEGORY'), 
                    path('AJAXService/BULK_DEACTIVATE_MAIN_CATEGORY/', MAINCATBULKAJAX.BULK_DEACTIVATE_MAIN_CATEGORY, name='BULK_DEACTIVATE_MAIN_CATEGORY'), 
                    path('AJAXService/BULK_DELETE_MAIN_CATEGORY/', MAINCATBULKAJAX.BULK_DELETE_MAIN_CATEGORY, name='BULK_DELETE_MAIN_CATEGORY'), 
                    # ===========================================================================       


                    path('SubCategory/', manageSubCategory.CreateSubCategory, name='createSubCategory'), 
                    path('SubCategory/', manageSubCategory.CreateSubCategory, name='SubCategory'), 
                    path('deletesubCat/<int:pk>/', manageSubCategory.DeleteSubCategory, name='DeleteSubCategory'),   
                    path('updatesubCat/<int:pk>/', manageSubCategory.UpdateSubCategory, name='UpdateSubCategory'),   
                    path('copysubCat/<int:pk>/', manageSubCategory.CopySubCategory, name='CopySubCategory'),   
                    path('ActivatedSubCategory/<int:pk>', manageSubCategory.ActivatedSubCategory, name='ActivatedSubCategory'),
                    path('DeactivatedSubCategory/<int:pk>', manageSubCategory.DeactivatedSubCategory, name='DeactivatedSubCategory'),
                    # ====================AJAX SERVECE===========================
                    path('AJAXService/CRUDOperation/DELETESubCat/', manageSubCategory.DELETESubCat, name='DELETESubCat'),
                    path('AJAXService/SubCatImport/', SubCatImportExport.SubCatImport, name='SubCatImport'), 
                    path('AJAXService/SubCatExport/', SubCatImportExport.SubCatExport, name='SubCatExport'), 
                    # ====================AJAX SERVECE===========================
                    # ====================AJAX SERVECE===========================
                     # ===========================================================================       
                    path('AJAXService/BULK_ACTIVATE_SUB_CATEGORY/', SUBCATBULKAJAX.BULK_ACTIVATE_SUB_CATEGORY, name='BULK_ACTIVATE_SUB_CATEGORY'), 
                    path('AJAXService/BULK_DEACTIVATE_SUB_CATEGORY/', SUBCATBULKAJAX.BULK_DEACTIVATE_SUB_CATEGORY, name='BULK_DEACTIVATE_SUB_CATEGORY'), 
                    path('AJAXService/BULK_DELETE_SUB_CATEGORY/', SUBCATBULKAJAX.BULK_DELETE_SUB_CATEGORY, name='BULK_DELETE_SUB_CATEGORY'), 
                    # ===========================================================================       

                    
                    path('SubSubCategory/', manageSubSubCategory.CreateSubSubCategory, name='createSubSubCategory'), 
                    path('SubSubCategory/', manageSubSubCategory.CreateSubSubCategory, name='SubSubCategory'), 
                    path('deleteSubSubCat/<int:pk>/', manageSubSubCategory.DeleteSubSubCategory, name='DeleteSubSubCategory'),   
                    path('updateSubSubCat/<int:pk>/', manageSubSubCategory.UpdateSubSubCategory, name='UpdateSubSubCategory'),   
                    path('copySubSubCat/<int:pk>/', manageSubSubCategory.CopySubSubCategory, name='CopySubSubCategory'),   
                    path('ActivatedSubSubCategory/<int:pk>', manageSubSubCategory.ActivatedSubSubCategory, name='ActivatedSubSubCategory'),
                    path('DeactivatedSubSubCategory/<int:pk>', manageSubSubCategory.DeactivatedSubSubCategory, name='DeactivatedSubSubCategory'),
                    # ====================AJAX SERVECE===========================
                    path('AJAXService/CRUDOperation/DELETESubSubCat/', manageSubSubCategory.DELETESubSubCat, name='DELETESubSubCat'),
                    path('AJAXService/SubSubCatImport/', SubSubCatImportExport.SubSubCatImport, name='SubSubCatImport'), 
                    path('AJAXService/SubSubCatExport/', SubSubCatImportExport.SubSubCatExport, name='SubSubCatExport'), 
                     # ===========================================================================       
                    path('AJAXService/BULK_ACTIVATE_SUB_SUB_CATEGORY/', SUBSUBCATBULKAJAX.BULK_ACTIVATE_SUB_SUB_CATEGORY, name='BULK_ACTIVATE_SUB_SUB_CATEGORY'), 
                    path('AJAXService/BULK_DEACTIVATE_SUB_SUB_CATEGORY/', SUBSUBCATBULKAJAX.BULK_DEACTIVATE_SUB_SUB_CATEGORY, name='BULK_DEACTIVATE_SUB_SUB_CATEGORY'), 
                    path('AJAXService/BULK_DELETE_SUB_SUB_CATEGORY/', SUBSUBCATBULKAJAX.BULK_DELETE_SUB_SUB_CATEGORY, name='BULK_DELETE_SUB_SUB_CATEGORY'), 
                    # ===========================================================================       

                    # ====================AJAX SERVECE===========================
                    # ====================AJAX SERVECE===========================
                    path('LoadSubCatList', views.LoadSubCatList, name='LoadSubCatList'), 
                    path('LoadSubSubCatList', views.LoadSubSubCatList, name='LoadSubSubCatList'), 

                ]