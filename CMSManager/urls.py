from django.urls import path
from .AJAXService import AJAXService, PAGEImportExport, SECTIONImportExport, SECTIONBULKAJAX, PAGEBULKAJAX
from . import PAGEManage, views, SECTIONManager

urlpatterns = [

    
    path('CMSSettings/', views.CMSSettings, name='CMSSettings'),    

    # ===================MANAGE-SECTIONSECTION====================   
    # ===================MANAGE-SECTIONSECTION====================   
    path('SECTION/all', SECTIONManager.CreateSECTION, name='SECTIONList'),  
    path('update/<int:pk>/', SECTIONManager.UpdateSECTION, name='UpdateSECTION'),
    path('activated/<int:pk>/', SECTIONManager.ActivatedSECTION, name='ActivatedSECTION'),
    path('deactivated/<int:pk>/', SECTIONManager.DeactivatedSECTION, name='DeactivatedSECTION'),
    path('copy/<int:pk>/', SECTIONManager.CopySECTION, name='CopySECTION'),
    path('delete/<int:pk>/', SECTIONManager.DeleteSECTION, name='DeleteSECTION'),
    # ===========================================================================
    path('DELETESECTION/', AJAXService.DELETESECTION, name='DELETESECTION'), 
    # ===========================================================================        
    # ===========================================================================       
    path('AJAXSECTION/SECTIONImport/', SECTIONImportExport.SECTIONImport, name='SECTIONImport'), 
    path('AJAXSECTION/SECTIONExport/', SECTIONImportExport.SECTIONExport, name='SECTIONExport'), 

    # ===========================================================================       
    path('AJAXService/BULK_ACTIVATE_SECTION/', SECTIONBULKAJAX.BULK_ACTIVATE_SECTION, name='BULK_ACTIVATE_SECTION'), 
    path('AJAXService/BULK_DEACTIVATE_SECTION/', SECTIONBULKAJAX.BULK_DEACTIVATE_SECTION, name='BULK_DEACTIVATE_SECTION'), 
    path('AJAXService/BULK_DELETE_SECTION/', SECTIONBULKAJAX.BULK_DELETE_SECTION, name='BULK_DELETE_SECTION'), 
    # ===========================================================================       

    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------

    path('PAGEList/', PAGEManage.ALLPAGEList.as_view(), name='PAGEList'),
    path('createPAGE/', PAGEManage.createPAGE, name='createPAGE'),
    path('updatePAGE/<slug>/', PAGEManage.updatePAGE, name='updatePAGE'),
    # # =============================================================================
    # # =============================================================================
    # # PAGE OPERATIONS
    # # =============================================================================
    # # =============================================================================
    path('ActivatePAGE/<int:pk>/', PAGEManage.ActivatePAGE, name='ActivatePAGE'),
    path('DeactivatePAGE/<int:pk>/', PAGEManage.DeactivatePAGE, name='DeactivatePAGE'),
    path('DeletePAGE/<int:pk>/', PAGEManage.DeletePAGE, name='DeletePAGE'),
    path('RestorePAGE/<int:pk>/', PAGEManage.RestorePAGE, name='RestorePAGE'),
    path('deletePermanentlyPAGE/<int:pk>/', PAGEManage.deletePermanentlyPAGE, name='deletePermanentlyPAGE'),
    # # =============================================================================
    # # =============================================================================
    # # AJAX SERVICE PROVIDER
    # # =============================================================================
    # # =============================================================================
    path('AJAXService/PAGEImport/', PAGEImportExport.PAGEImport, name='PAGEImport'), 
    path('AJAXService/PAGEExport/', PAGEImportExport.PAGEExport, name='PAGEExport'), 
    # ===========================================================================         
    path('AJAXService/BULK_ACTIVATE_PAGE/', PAGEBULKAJAX.BULK_ACTIVATE, name='BULK_ACTIVATE_PAGE'), 
    path('AJAXService/BULK_DEACTIVATE_PAGE/', PAGEBULKAJAX.BULK_DEACTIVATE, name='BULK_DEACTIVATE_PAGE'), 
    path('AJAXService/BULK_MOVE_TO_TRASH_PAGE/', PAGEBULKAJAX.BULK_MOVE_TO_TRASH, name='BULK_PAGE_MOVE_TO_TRASH_PAGE'), 
    path('AJAXService/BULK_RESTORE_FROM_TRASH_PAGE/', PAGEBULKAJAX.BULK_RESTORE_FROM_TRASH, name='BULK_PAGE_RESTORE_FROM_TRASH'), 
    path('AJAXService/BULK_PERMANENTLY_DELETE_PAGE/', PAGEBULKAJAX.BULK_PERMANENTLY_DELETE, name='BULK_PERMANENTLY_DELETE_PAGE'), 
    # ===========================================================================       

    # # =============================================================================
    # # =============================================================================
    # # LOAD CATEGORY DATA USING AJAX METHOD
    # # =============================================================================
    # # =============================================================================    
    # UpdateCHATBOTSettings
]

# # =============================================================================
# # =============================================================================
# # PAGE template/slidebar.html Copy Past For This PAGE App.
# # =============================================================================


    # {% if PAGEManager %}
    # <li class="nav-item menu-open">
    # {% else %}
    # <li class="nav-item">
    # {% endif %}
    #     {% if PAGEManager %}
    #     <a href="#" class="nav-link active">
    #         <i class="nav-icon fa fa-rocket"></i>
    #         <p>PAGE Manager<i class="fas fa-angle-left right"></i></p>
    #     </a>
    #     {% else %}
    #     <a href="#" class="nav-link">
    #         <i class="nav-icon fas fa-copy"></i>
    #         <p>PAGE Manager<i class="fas fa-angle-left right"></i></p>
    #     </a>
    #     {% endif %}

    #     <ul class="nav nav-treeview">
    #         <li class="nav-item " >
    #             {% if PAGECat %}
    #             <a href="{% url 'PAGECatManager' %}" class="nav-link active">
    #                 <i class="fas fa-edit nav-icon text-primary"></i>
    #                 <p><b>PAGE Category</b></p>
    #             </a>
    #             {% else %}
    #             <a href="{% url 'PAGECatManager' %}" class="nav-link"><i class="fas fa-th-list nav-icon"></i>
    #                 <p>PAGE Category</p>
    #             </a>
    #             {% endif %}
    #         </li>

    #         <li class="nav-item " >
    #             {% if createPAGE %}
    #             <a href="{% url 'createPAGE' %}" class="nav-link active">
    #                 <i class="fas fa-edit nav-icon text-primary"></i>
    #                 <p><b>Create PAGE</b></p>
    #             </a>
    #             {% else %}
    #             <a href="{% url 'createPAGE' %}" class="nav-link">
    #                 <i class="fas fa-edit nav-icon"></i>
    #                 <p>Create PAGE</p>
    #             </a>
    #             {% endif %}
    #         </li>

    #         {% if updatePAGE %}
    #         <li class="nav-item " >
    #             <a href="{% url 'createPAGE' %}" class="nav-link active">
    #                 <i class="fas fa-edit nav-icon text-primary"></i>
    #                 <p><b>Update PAGE</b></p>
    #             </a>                                
    #         </li>
    #         {% endif %}

    #         {% if PAGEManager and allPAGE and request.GET.is_draft %}
    #         <li class="nav-item " >
    #             <a href="{% url 'PAGEList' %}?is_draft=True" class="nav-link active">
    #                 <i class="fas fa-th-list nav-icon text-primary"></i>
    #                 <p><b>Draft PAGEs</b></p>
    #             </a>
    #         </li>
    #         {% elif PAGEManager and allPAGE and request.GET.is_active %}
    #         <li class="nav-item " >
    #             <a href="{% url 'PAGEList' %}?is_verified=True" class="nav-link  active">
    #                 <i class="fas fa-check-circle nav-icon text-success"></i>
    #                 <p><b>Active PAGEs</b></p>
    #             </a>
    #         </li>
    #         {% elif PAGEManager and allPAGE and request.GET.is_active %}
    #         <li class="nav-item " >
    #             <a href="{% url 'PAGEList' %}?is_active=False" class="nav-link {% if request.GET.is_active %} active {% endif %}">
    #                 <i class="fas fa-exclamation-triangle nav-icon text-warning"></i>
    #                 <p><b>Deactive PAGEs</b></p>
    #             </a>
    #         </li>
    #         {% elif PAGEManager and allPAGE and request.GET.is_deleted %}
    #         <li class="nav-item " >
    #             <a href="{% url 'PAGEList' %}?is_deleted=True" class="nav-link active ">
    #                 <i class="fas fa-trash-alt nav-icon text-danger"></i>
    #                 <p><b>Deleted PAGEs</b></p>
    #             </a>
    #         </li>
    #         {% else %}
    #         <li class="nav-item " >
    #             <a href="{% url 'PAGEList' %}?is_draft=True" class="nav-link ">
    #                 <i class="fas fa-th-list nav-icon"></i>
    #                 <p><b>All PAGEs</b></p>
    #             </a>
    #         </li>
    #         {% endif %}
    #     </ul>
    # </li>
