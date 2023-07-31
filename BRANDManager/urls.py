from django.urls import path

from BRANDManager import BRANDManager

from BRANDManager.AJAXService import BRANDImportExport, BRANDBULKAJAX

urlpatterns = [
                path('BRANDList/', BRANDManager.ALLBRANDList.as_view(), name='BRANDList'), 
                path('CreateBRAND/', BRANDManager.CreateBRAND, name='CreateBRAND'),       
                path('updateBRAND/<int:pk>/', BRANDManager.updateBRAND, name='updateBRAND'),

                path('ActivatedBRAND/<int:pk>/', BRANDManager.ActivatedBRAND, name='ActivatedBRAND'),
                path('DeactivatedBRAND/<int:pk>/', BRANDManager.DeactivatedBRAND, name='DeactivatedBRAND'),

                path('DeleteBRAND/<int:pk>/', BRANDManager.DeleteBRAND, name='DeleteBRAND'),
                path('RestoreBRAND/<int:pk>/', BRANDManager.RestoreBRAND, name='RestoreBRAND'),
                path('PermanentlyDeleteBRAND/<int:pk>/', BRANDManager.PermanentlyDeleteBRAND, name='PermanentlyDeleteBRAND'),
             
             
            # ===========================================================================   
            path('AJAXService/BRANDImport/', BRANDImportExport.BRANDImport, name='BRANDImport'), 
            path('AJAXService/BRANDExport/', BRANDImportExport.BRANDExport, name='BRANDExport'), 
            # ===========================================================================         
            path('AJAXService/BULK_ACTIVATE_BRAND/', BRANDBULKAJAX.BULK_ACTIVATE, name='BULK_ACTIVATE_BRAND'), 
            path('AJAXService/BULK_DEACTIVATE_BRAND/', BRANDBULKAJAX.BULK_DEACTIVATE, name='BULK_DEACTIVATE_BRAND'), 
            path('AJAXService/BULK_MOVE_TO_TRASH_BRAND/', BRANDBULKAJAX.BULK_MOVE_TO_TRASH, name='BULK_BRAND_MOVE_TO_TRASH_BRAND'), 
            path('AJAXService/BULK_RESTORE_FROM_TRASH_BRAND/', BRANDBULKAJAX.BULK_RESTORE_FROM_TRASH, name='BULK_BRAND_RESTORE_FROM_TRASH'), 
            path('AJAXService/BULK_PERMANENTLY_DELETE_BRAND/', BRANDBULKAJAX.BULK_PERMANENTLY_DELETE, name='BULK_PERMANENTLY_DELETE_BRAND'), 
            # ===========================================================================       

            # ---------------------------------------------------------------------------------------------------------
            # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
            # ---------------------------------------------------------------------------------------------------------

             
             ]


# {% if BRANDManager %}
# <li class="nav-item menu-open">
#     {% else %}
# <li class="nav-item">
#     {% endif %}
#     {% if BRANDManager %}
#     <a href="" class="nav-link active">
#         <i class="fas fa-users fa-10x nav-icon"></i>
#         <p> BRAND Manager <i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% else %}
#     <a href="" class="nav-link">
#         <i class="fas fa-users fa-10x nav-icon"></i>
#         <p> BRAND Manager <i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% endif %}
#     <ul class="nav nav-treeview">
#         {% comment %}
#         <!-- <li class="nav-item sidebar-control">
#             {% if tCategory %}
#             <a href="{% url 'CreateBRANDCategory' %}" class="nav-link active">
#                 <i class="fas fa-user-lock nav-icon text-primary"></i>
#                 <p><b>BRAND Category</b></p>
#             </a>
#             {% else %}
#             <a href="{% url 'CreateBRANDCategory' %}" class="nav-link">
#                 <i class="fas fa-users nav-icon"></i>
#                 <p>BRAND Category</p>
#             </a>
#             {% endif %}
#         </li> -->
#         {% endcomment %}

#         <li class="nav-item sidebar-control">
#             {% if CreateBRAND %}
#             <a href="{% url 'CreateBRAND' %}" class="nav-link active">
#                 <i class="fas fa-user-lock nav-icon text-primary"></i>
#                 <p><b>Create BRAND</b></p>
#             </a>
#             {% else %}
#             <a href="{% url 'CreateBRAND' %}" class="nav-link">
#                 <i class="fas fa-users nav-icon"></i>
#                 <p>Create BRAND</p>
#             </a>
#             {% endif %}
#         </li>
#         <li class="nav-item sidebar-control">
#             {% if BRANDListActive %}
#             <a href="{% url 'BRANDList' %}?is_draft=True" class="nav-link active">
#                 <i class="fas fa-user-lock nav-icon text-primary"></i>
#                 <p><b> BRAND List</b></p>
#             </a>
#             {% else %}
#             <a href="{% url 'BRANDList' %}?is_draft=True" class="nav-link">
#                 <i class="fas fa-th-list nav-icon"></i>
#                 <p> BRAND List</p>
#             </a>
#             {% endif %}
#         </li>
#     </ul>
# </li>

