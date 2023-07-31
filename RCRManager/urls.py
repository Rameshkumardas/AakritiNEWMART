from . import RETURNManager, CANCELManager, REPLACEMENTManager
from django.urls import path

from RCRManager.AJAXService import RETURNImportExport, CANCELImportExport, REPLACEMENTImportExport

urlpatterns = [
    # ===================MANAGE-BLOGMainCat====================   
    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
    # ==================================MANAGE-RETURN==============================   
    path('RETURNList/', RETURNManager.ALLRETURNList.as_view(), name='RETURNList'),                   
    path('activateRETURN/<int:pk>/', RETURNManager.activateRETURN, name='activateRETURN'),
    path('deactivateRETURN/<int:pk>/', RETURNManager.deactivateRETURN, name='deactivateRETURN'),
    path('deleteRETURN/<int:pk>/', RETURNManager.deleteRETURN, name='deleteRETURN'),
    path('restoreRETURN/<int:pk>/', RETURNManager.restoreRETURN, name='restoreRETURN'),
    path('PermanentDeleteRETURN/<int:pk>/', RETURNManager.PermanentDeleteRETURN, name='PermanentDeleteRETURN'),
    # ===========================================================================        
    # ===========================================================================   
    path('AJAXService/RETURNImport/', RETURNImportExport.RETURNImport, name='RETURNImport'), 
    path('AJAXService/RETURNExport/', RETURNImportExport.RETURNExport, name='RETURNExport'), 
    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
    # ==================================MANAGE-CANCEL==============================   
    path('CANCELList/', CANCELManager.ALLCANCELList.as_view(), name='CANCELList'),                   
    path('activateCANCEL/<int:pk>/', CANCELManager.activateCANCEL, name='activateCANCEL'),
    path('deactivateCANCEL/<int:pk>/', CANCELManager.deactivateCANCEL, name='deactivateCANCEL'),
    path('deleteCANCEL/<int:pk>/', CANCELManager.deleteCANCEL, name='deleteCANCEL'),
    path('restoreCANCEL/<int:pk>/', CANCELManager.restoreCANCEL, name='restoreCANCEL'),
    path('PermanentDeleteCANCEL/<int:pk>/', CANCELManager.PermanentDeleteCANCEL, name='PermanentDeleteCANCEL'),
    # ===========================================================================        
    # ===========================================================================   
    path('AJAXService/CANCELImport/', CANCELImportExport.CANCELImport, name='CANCELImport'), 
    path('AJAXService/CANCELExport/', CANCELImportExport.CANCELExport, name='CANCELExport'), 
    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
    # ==================================MANAGE-REPLACEMENT==============================   
    path('REPLACEMENTList/', REPLACEMENTManager.ALLREPLACEMENTList.as_view(), name='REPLACEMENTList'),                   
    path('activateREPLACEMENT/<int:pk>/', REPLACEMENTManager.activateREPLACEMENT, name='activateREPLACEMENT'),
    path('deactivateREPLACEMENT/<int:pk>/', REPLACEMENTManager.deactivateREPLACEMENT, name='deactivateREPLACEMENT'),
    path('deleteREPLACEMENT/<int:pk>/', REPLACEMENTManager.deleteREPLACEMENT, name='deleteREPLACEMENT'),
    path('restoreREPLACEMENT/<int:pk>/', REPLACEMENTManager.restoreREPLACEMENT, name='restoreREPLACEMENT'),
    path('PermanentDeleteREPLACEMENT/<int:pk>/', REPLACEMENTManager.PermanentDeleteREPLACEMENT, name='PermanentDeleteREPLACEMENT'),
    # ===========================================================================        
    # ===========================================================================   
    path('AJAXService/REPLACEMENTImport/', REPLACEMENTImportExport.REPLACEMENTImport, name='REPLACEMENTImport'), 
    path('AJAXService/REPLACEMENTExport/', REPLACEMENTImportExport.REPLACEMENTExport, name='REPLACEMENTExport'), 
    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
]


# {% if RCRManager %}
# <li class="nav-item menu-open">
#     {% else %}
# <li class="nav-item">
#     {% endif %}
#     {% if RCRManager %}
#     <a href="#" class="nav-link active"><i class="fas fa-laptop-code nav-icon"></i>
#         <p><b>RETURN Manager</b><i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% else %}
#     <a href="#" class="nav-link"><i class="fas fa-laptop-code nav-icon"></i>
#         <p>RETURN Manager<i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% endif %}
#     <ul class="nav nav-treeview">
#         <li class="nav-item sidebar-control">

#         {% if request.GET.is_draft and RETURNManager and allRETURNS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'RETURNList' %}?is_draft=True" class="nav-link active"><i
#                     class="fas fa-drafting-compass nav-icon text-info"></i>
#                 <p><b>Return Request</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_verified and RETURNManager and allRETURNS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'RETURNList' %}?is_verified=True" class="nav-link active"><i
#                     class="fas fa-check-circle nav-icon text-success"></i>
#                 <p><b>Return Approved</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_active and RETURNManager and allRETURNS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'RETURNList' %}?is_active=True" class="nav-link active"><i
#                     class="fas fa-exclamation-triangle nav-icon text-warning"></i>
#                 <p><b>Return Rejected </b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_deleted and RETURNManager and allRETURNS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'RETURNList' %}?is_deleted=True" class="nav-link active"><i
#                     class="fas fa-trash-alt nav-icon text-danger"></i>
#                 <p><b>Return Deleted</b></p>
#             </a>
#         </li>
#         {% else %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'RETURNList' %}?is_draft=True" class="nav-link"><i
#                     class="fas fa-th-list nav-icon"></i>
#                 <p> All </p>
#             </a>
#         </li>
#         {% endif %}

#         {% if request.GET.is_draft and CANCELManager and allCANCELS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'CANCELList' %}?is_draft=True" class="nav-link active"><i
#                     class="fas fa-drafting-compass nav-icon text-info"></i>
#                 <p><b>CANCEL Request</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_verified and CANCELManager and allCANCELS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'CANCELList' %}?is_verified=True" class="nav-link active"><i
#                     class="fas fa-check-circle nav-icon text-success"></i>
#                 <p><b>CANCEL Approved</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_active and CANCELManager and allCANCELS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'CANCELList' %}?is_active=True" class="nav-link active"><i
#                     class="fas fa-exclamation-triangle nav-icon text-warning"></i>
#                 <p><b>CANCEL Rejected </b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_deleted and CANCELManager and allCANCELS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'CANCELList' %}?is_deleted=True" class="nav-link active"><i
#                     class="fas fa-trash-alt nav-icon text-danger"></i>
#                 <p><b>CANCEL Deleted</b></p>
#             </a>
#         </li>
#         {% else %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'CANCELList' %}?is_draft=True" class="nav-link"><i
#                     class="fas fa-th-list nav-icon"></i>
#                 <p> All </p>
#             </a>
#         </li>
#         {% endif %}
        
#         {% if request.GET.is_draft and REPLACEMENTManager and allREPLACEMENTS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'REPLACEMENTList' %}?is_draft=True" class="nav-link active"><i
#                     class="fas fa-drafting-compass nav-icon text-info"></i>
#                 <p><b>REPLACEMENT Request</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_verified and REPLACEMENTManager and allREPLACEMENTS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'REPLACEMENTList' %}?is_verified=True" class="nav-link active"><i
#                     class="fas fa-check-circle nav-icon text-success"></i>
#                 <p><b>REPLACEMENT Approved</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_active and REPLACEMENTManager and allREPLACEMENTS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'REPLACEMENTList' %}?is_active=True" class="nav-link active"><i
#                     class="fas fa-exclamation-triangle nav-icon text-warning"></i>
#                 <p><b>REPLACEMENT Rejected </b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_deleted and REPLACEMENTManager and allREPLACEMENTS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'REPLACEMENTList' %}?is_deleted=True" class="nav-link active"><i
#                     class="fas fa-trash-alt nav-icon text-danger"></i>
#                 <p><b>REPLACEMENT Deleted</b></p>
#             </a>
#         </li>
#         {% else %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'REPLACEMENTList' %}?is_draft=True" class="nav-link"><i
#                     class="fas fa-th-list nav-icon"></i>
#                 <p> All REPLACEMENT</p>
#             </a>
#         </li>
#         {% endif %}
        
#     </ul>
# </li>
           

