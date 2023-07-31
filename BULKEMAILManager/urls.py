from BULKEMAILManager import EMAILSENDSTATUSManager, EMAILTEMPLATEManager
from BULKEMAILManager.AJAXService import AJAXService, AJAXAUTOUPDATEEMAIL, EMAILImportExport, EMAILTEMPLATEImportExport
from BULKEMAILManager.AJAXService.AJAXAUTOUPDATEEMAILTEMPLATE import AUTOUPDATEEMAILTEMPLATE
from .AJAXService import EMAILBULKAJAX, EMAILTEMPLATEBULKAJAX
from . import EMAILManager
from django.urls import path

urlpatterns = [    
    # ==================================MANAGE-EMAIL==============================   
    
    path('RESETEMAILList/', EMAILManager.resetEMAILSTATUS, name='resetEMAILSTATUS'),                   
    # ==================================MANAGE-EMAIL==============================   
    path('EMAILList/', EMAILManager.ALLEMAILList.as_view(), name='EMAILList'),                   
    path('Compose-New-Email/', EMAILManager.composeEMAIL, name='createEMAIL'),
    path('updateEMAIL/<slug>/', EMAILManager.updateEMAIL, name='updateEMAIL'),
    path('activateEMAIL/<int:pk>/', EMAILManager.activateEMAIL, name='activateEMAIL'),
    path('deactivateEMAIL/<int:pk>/', EMAILManager.deactivateEMAIL, name='deactivateEMAIL'),
    path('deleteEMAIL/<int:pk>/', EMAILManager.deleteEMAIL, name='deleteEMAIL'),
    path('restoreEMAIL/<int:pk>/', EMAILManager.restoreEMAIL, name='restoreEMAIL'),
    path('PermanentDeleteEMAIL/<int:pk>/', EMAILManager.PermanentDeleteEMAIL, name='PermanentDeleteEMAIL'),
    # ===========================================================================        
    # ===========================================================================  
    path('AJAXService/AUTOUPDATEEMAIL/', AJAXAUTOUPDATEEMAIL.AUTOUPDATEEMAIL, name='AUTOUPDATEEMAIL'), 
    # ===========================================================================   
    path('AJAXService/EMAILImport/', EMAILImportExport.EMAILImport, name='EMAILImport'), 
    path('AJAXService/EMAILExport/', EMAILImportExport.EMAILExport, name='EMAILExport'), 
    # ===========================================================================        
    # ===========================================================================         
    path('AJAXService/BULK_ACTIVATE_EMAIL/', EMAILBULKAJAX.BULK_ACTIVATE, name='BULK_ACTIVATE_EMAIL'), 
    path('AJAXService/BULK_DEACTIVATE_EMAIL/', EMAILBULKAJAX.BULK_DEACTIVATE, name='BULK_DEACTIVATE_EMAIL'), 
    path('AJAXService/BULK_MOVE_TO_TRASH_EMAIL/', EMAILBULKAJAX.BULK_MOVE_TO_TRASH, name='BULK_EMAIL_MOVE_TO_TRASH_EMAIL'), 
    path('AJAXService/BULK_RESTORE_FROM_TRASH_EMAIL/', EMAILBULKAJAX.BULK_RESTORE_FROM_TRASH, name='BULK_EMAIL_RESTORE_FROM_TRASH'), 
    path('AJAXService/BULK_PERMANENTLY_DELETE_EMAIL/', EMAILBULKAJAX.BULK_PERMANENTLY_DELETE, name='BULK_PERMANENTLY_DELETE_EMAIL'), 
    # ===========================================================================       

    path('AJAXService/addEMAIL/', AJAXService.addEMAIL, name='addEMAIL'), 
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ==================================MANAGE-EMAIL-TEMPLATE==============================   
    # ==================================MANAGE-EMAIL-TEMPLATE==============================   
    path('EMAILTEMPLATEList/', EMAILTEMPLATEManager.ALLEMAILTEMPLATEList.as_view(), name='EMAILTEMPLATEList'),                   
    path('Compose-New-EmailTEMPLATE/', EMAILTEMPLATEManager.createEMAILTEMPLATE, name='createEMAILTEMPLATE'),
    path('updateEMAILTEMPLATE/<int:pk>/', EMAILTEMPLATEManager.updateEMAILTEMPLATE, name='updateEMAILTEMPLATE'),
    # sendEMAILTEMPLATE
    path('sendEMAILTEMPLATE/<int:pk>/', EMAILTEMPLATEManager.sendEMAILTEMPLATE, name='sendEMAILTEMPLATE'),
    path('activateEMAILTEMPLATE/<int:pk>/', EMAILTEMPLATEManager.activateEMAILTEMPLATE, name='activateEMAILTEMPLATE'),
    path('deactivateEMAILTEMPLATE/<int:pk>/', EMAILTEMPLATEManager.deactivateEMAILTEMPLATE, name='deactivateEMAILTEMPLATE'),
    path('deleteEMAILTEMPLATE/<int:pk>/', EMAILTEMPLATEManager.deleteEMAILTEMPLATE, name='deleteEMAILTEMPLATE'),
    path('restoreEMAILTEMPLATE/<int:pk>/', EMAILTEMPLATEManager.restoreEMAILTEMPLATE, name='restoreEMAILTEMPLATE'),
    path('PermanentDeleteEMAILTEMPLATE/<int:pk>/', EMAILTEMPLATEManager.PermanentDeleteEMAILTEMPLATE, name='PermanentDeleteEMAILTEMPLATE'),
    # ===========================================================================        
    # ===========================================================================  
    path('AJAXService/AUTOUPDATEEMAILTEMPLATE/', AUTOUPDATEEMAILTEMPLATE, name='AUTOUPDATEEMAILTEMPLATE'), 
    # ===========================================================================   
    path('AJAXService/EMAILTEMPLATEImport/', EMAILTEMPLATEImportExport.EMAILTEMPLATEImport, name='EMAILTEMPLATEImport'), 
    path('AJAXService/EMAILTEMPLATEExport/', EMAILTEMPLATEImportExport.EMAILTEMPLATEExport, name='EMAILTEMPLATEExport'), 
    # ===========================================================================         
    path('AJAXService/BULK_ACTIVATE_EMAILTEMPLATE/', EMAILTEMPLATEBULKAJAX.BULK_ACTIVATE, name='BULK_ACTIVATE_EMAILTEMPLATE'), 
    path('AJAXService/BULK_DEACTIVATE_EMAILTEMPLATE/', EMAILTEMPLATEBULKAJAX.BULK_DEACTIVATE, name='BULK_DEACTIVATE_EMAILTEMPLATE'), 
    path('AJAXService/BULK_MOVE_TO_TRASH_EMAILTEMPLATE/', EMAILTEMPLATEBULKAJAX.BULK_MOVE_TO_TRASH, name='BULK_EMAILTEMPLATE_MOVE_TO_TRASH_EMAILTEMPLATE'), 
    path('AJAXService/BULK_RESTORE_FROM_TRASH_EMAILTEMPLATE/', EMAILTEMPLATEBULKAJAX.BULK_RESTORE_FROM_TRASH, name='BULK_EMAILTEMPLATE_RESTORE_FROM_TRASH'), 
    path('AJAXService/BULK_PERMANENTLY_DELETE_EMAILTEMPLATE/', EMAILTEMPLATEBULKAJAX.BULK_PERMANENTLY_DELETE, name='BULK_PERMANENTLY_DELETE_EMAILTEMPLATE'), 
    # ===========================================================================       

    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
    # 
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ===========================================================================        
    # ==================================MANAGE-EMAIL-TEMPLATE==============================   
    # ==================================MANAGE-EMAIL-TEMPLATE==============================   
    path('ALLSENDEMAILSTATUSList/', EMAILSENDSTATUSManager.ALLEMAILSENDSTATUSList.as_view(), name='ALLSENDEMAILSTATUSList'),                   

]
# ---------------------------------------------------------------------------------------------------------
# ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
# ---------------------------------------------------------------------------------------------------------
# {% if request.user.is_accountant %}
# <li class="nav-header text-light"><b>CONTENT MANAGER</b></li>
# {% if EMAILManager %}
# <li class="nav-item menu-open">
#     {% else %}
# <li class="nav-item">
#     {% endif %}
#     {% if EMAILManager %}
#     <a href="#" class="nav-link active"><i class="fas fa-laptop-code nav-icon"></i>
#         <p><b>EMAIL Manager</b><i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% else %}
#     <a href="#" class="nav-link"><i class="fas fa-laptop-code nav-icon"></i>
#         <p>EMAIL Manager<i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% endif %}
#     <ul class="nav nav-treeview">
#         <li class="nav-item sidebar-control">
#             <li class="nav-item sidebar-control">
#                 {% if CreateEMAILs %}
#                 <a href="{% url 'createEMAIL' %}" class="nav-link active">
#                     <i class="fas fa-edit nav-icon text-primary"></i>
#                     <p><b>Create EMAIL</b></p>
#                 </a>
#                 {% else %}
#                 <a href="{% url 'createEMAIL' %}" class="nav-link">
#                     <i class="fas fa-edit nav-icon"></i>
#                     <p>Create EMAIL</p>
#                 </a>
#                 {% endif %}
#             </li>
            
#         {% if request.GET.is_draft and EMAILManager and allEMAILS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'EMAILList' %}?is_draft=True" class="nav-link active"><i
#                     class="fas fa-drafting-compass nav-icon text-info"></i>
#                 <p><b> Draft EMAILs</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_verified and EMAILManager and allEMAILS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'EMAILList' %}?is_verified=True" class="nav-link active"><i
#                     class="fas fa-check-circle nav-icon text-success"></i>
#                 <p><b> Active EMAILs</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_active and EMAILManager and allEMAILS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'EMAILList' %}?is_active=True" class="nav-link active"><i
#                     class="fas fa-exclamation-triangle nav-icon text-warning"></i>
#                 <p><b> Deactive EMAILs</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_deleted and EMAILManager and allEMAILS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'EMAILList' %}?is_deleted=True" class="nav-link active"><i
#                     class="fas fa-trash-alt nav-icon text-danger"></i>
#                 <p><b> Deleted EMAILs</b></p>
#             </a>
#         </li>
#         {% else %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'EMAILList' %}?is_draft=True" class="nav-link"><i
#                     class="fas fa-th-list nav-icon"></i>
#                 <p> All EMAILs</p>
#             </a>
#         </li>
#         {% endif %}
#     </ul>
# </li>
# {% endif %}
           

