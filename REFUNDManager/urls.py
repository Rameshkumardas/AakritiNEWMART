from django.urls import path
from . import views
from REFUNDManager import REFUNDManager
from REFUNDManager.AJAXService import REFUNDImportExport

urlpatterns = [
        # ==================================MANAGE-REFUND==============================   
        path('REFUNDList/', REFUNDManager.ALLREFUNDList.as_view(), name='REFUNDList'),                   
        path('activateREFUND/<int:pk>/', REFUNDManager.activateREFUND, name='activateREFUND'),
        path('deactivateREFUND/<int:pk>/', REFUNDManager.deactivateREFUND, name='deactivateREFUND'),
        path('deleteREFUND/<int:pk>/', REFUNDManager.deleteREFUND, name='deleteREFUND'),
        path('restoreREFUND/<int:pk>/', REFUNDManager.restoreREFUND, name='restoreREFUND'),
        path('PermanentDeleteREFUND/<int:pk>/', REFUNDManager.PermanentDeleteREFUND, name='PermanentDeleteREFUND'),
        # ===========================================================================        
        # ===========================================================================   
        path('AJAXService/REFUNDImport/', REFUNDImportExport.REFUNDImport, name='REFUNDImport'), 
        path('AJAXService/REFUNDExport/', REFUNDImportExport.REFUNDExport, name='REFUNDExport'), 
        # ---------------------------------------------------------------------------------------------------------
        # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
        # ---------------------------------------------------------------------------------------------------------
    ]


        # {% if request.GET.is_draft and REFUNDManager and allREFUNDS %}
        # <li class="nav-item sidebar-control">
        #     <a href="{% url 'REFUNDList' %}?is_draft=True" class="nav-link active"><i
        #             class="fas fa-drafting-compass nav-icon text-info"></i>
        #         <p><b>REPLACEMENT Request</b></p>
        #     </a>
        # </li>
        # {% elif request.GET.is_verified and REFUNDManager and allREFUNDS %}
        # <li class="nav-item sidebar-control">
        #     <a href="{% url 'REFUNDList' %}?is_verified=True" class="nav-link active"><i
        #             class="fas fa-check-circle nav-icon text-success"></i>
        #         <p><b>REPLACEMENT Approved</b></p>
        #     </a>
        # </li>
        # {% elif request.GET.is_active and REFUNDManager and allREFUNDS %}
        # <li class="nav-item sidebar-control">
        #     <a href="{% url 'REFUNDList' %}?is_active=True" class="nav-link active"><i
        #             class="fas fa-exclamation-triangle nav-icon text-warning"></i>
        #         <p><b>REPLACEMENT Rejected </b></p>
        #     </a>
        # </li>
        # {% elif request.GET.is_deleted and REFUNDManager and allREFUNDS %}
        # <li class="nav-item sidebar-control">
        #     <a href="{% url 'REFUNDList' %}?is_deleted=True" class="nav-link active"><i
        #             class="fas fa-trash-alt nav-icon text-danger"></i>
        #         <p><b>REPLACEMENT Deleted</b></p>
        #     </a>
        # </li>
        # {% else %}
        # <li class="nav-item sidebar-control">
        #     <a href="{% url 'REFUNDList' %}?is_draft=True" class="nav-link"><i
        #             class="fas fa-th-list nav-icon"></i>
        #         <p> All REPLACEMENT</p>
        #     </a>
        # </li>
        # {% endif %}