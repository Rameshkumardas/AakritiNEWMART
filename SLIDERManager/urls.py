from django.urls import path
from .AJAXService import AJAXService, BANNERCatImportExport, BANNERImportExport 
from . import BANNERManager, BANNERCatManager

urlpatterns = [
        
        # ===================MANAGE-BANNERCatMainCat====================   
        # ===================MANAGE-BANNERCatMainCat====================   
        path('BANNERCat/all', BANNERCatManager.CreateBANNERCat, name='BANNERCatList'),  
        path('update/<int:pk>/', BANNERCatManager.UpdateBANNERCat, name='UpdateBANNERCat'),
        path('activated/<int:pk>/', BANNERCatManager.ActivatedBANNERCat, name='ActivatedBANNERCat'),
        path('deactivated/<int:pk>/', BANNERCatManager.DeactivatedBANNERCat, name='DeactivatedBANNERCat'),
        path('copy/<int:pk>/', BANNERCatManager.CopyBANNERCat, name='CopyBANNERCat'),
        path('delete/<int:pk>/', BANNERCatManager.DeleteBANNERCat, name='DeleteBANNERCat'),
        # ===========================================================================
        path('DELETEBANNERCat/', AJAXService.DELETEBANNERCat, name='DELETEBANNERCat'), 
        # ===========================================================================        
        # ===========================================================================       
        path('AJAXBANNERCat/BANNERCatImport/', BANNERCatImportExport.BANNERCatImport, name='BANNERCatImport'), 
        path('AJAXBANNERCat/BANNERCatExport/', BANNERCatImportExport.BANNERCatExport, name='BANNERCatExport'), 
        # ---------------------------------------------------------------------------------------------------------
        # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
        # ---------------------------------------------------------------------------------------------------------


        # ===================ADMIN ONLY INTERFACE====================   
        path('BANNERList/', BANNERManager.ALLBANNERList.as_view(), name='BANNERList'),                   
        path('updateBANNER/<slug>/', BANNERManager.updateBANNER, name='updateBANNER'),

        path('createBANNER/', BANNERManager.CreateBANNER, name='createBANNER'),
        path('activateBANNER/<int:pk>/', BANNERManager.activateBANNER, name='activateBANNER'),
        path('deactivateBANNER/<int:pk>/', BANNERManager.deactivateBANNER, name='deactivateBANNER'),
        path('deleteBANNER/<int:pk>/', BANNERManager.deleteBANNER, name='deleteBANNER'),
        path('restoreBANNER/<int:pk>/', BANNERManager.restoreBANNER, name='restoreBANNER'),
        path('PermanentDeleteBANNER/<int:pk>/', BANNERManager.PermanentDeleteBANNER, name='PermanentDeleteBANNER'),
        # ===========================================================================
        path('AJAXBANNE/BANNEImport/', BANNERImportExport.BANNERImport, name='BANNERImport'), 
        path('AJAXBANNE/BANNEExport/', BANNERImportExport.BANNERExport, name='BANNERExport'), 
        # ---------------------------------------------------------------------------------------------------------
        # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
        # ---------------------------------------------------------------------------------------------------------


]

#  {% if BANNERManager %}
#     <li class="nav-item menu-open">
#         {% else %}
#     <li class="nav-item">
#         {% endif %}
#         {% if BANNERManager %}
#         <a href="#" class="nav-link active"><i class="fas fa-laptop-code nav-icon"></i>
#             <p><b>BANNER Manager</b><i class="fas fa-angle-left right"></i></p>
#         </a>
#         {% else %}
#         <a href="#" class="nav-link"><i class="fas fa-laptop-code nav-icon"></i>
#             <p>BANNER Manager<i class="fas fa-angle-left right"></i></p>
#         </a>
#         {% endif %}
#         <ul class="nav nav-treeview">
#             <li class="nav-item sidebar-control">

#                 <li class="nav-item sidebar-control">
#                     {% if BANNERMainCatActive %}
#                     <a href="{% url 'BANNERMainCategory' %}" class="nav-link active">
#                         <i class="fas fa-edit nav-icon text-primary"></i>
#                         {% else %}
#                         <a href="{% url 'BANNERMainCategory' %}" class="nav-link">
#                             <i class="fas fa-th-large nav-icon"></i>
#                             {% endif %}
#                             <p>BANNER Main Category</p>
#                         </a>
#                 </li>
#                 <li class="nav-item sidebar-control">
#                     {% if BANNERSubCat %}
#                     <a href="{% url 'BANNERSubCategory' %}" class="nav-link active">
#                         <i class="far fa-edit nav-icon text-primary"></i>
#                         <p><b>BANNER SubCategory</b></p>
#                     </a>
#                     {% else %}
#                     <a href="{% url 'BANNERSubCategory' %}" class="nav-link">
#                         <i class="fas fa-th nav-icon"></i>
#                         <p>BANNER SubCategory</p>
#                     </a>
#                     {% endif %}
#                 </li>
#                 <li class="nav-item sidebar-control">
#                     {% if CreateBANNERs %}
#                     <a href="{% url 'createBANNER' %}" class="nav-link active">
#                         <i class="fas fa-edit nav-icon text-primary"></i>
#                         <p><b>Create BANNER</b></p>
#                     </a>
#                     {% else %}
#                     <a href="{% url 'createBANNER' %}" class="nav-link">
#                         <i class="fas fa-edit nav-icon"></i>
#                         <p>Create BANNER</p>
#                     </a>
#                     {% endif %}
#                 </li>
                


#             {% if request.GET.is_draft and BANNERManager and allBANNERS %}
#             <li class="nav-item sidebar-control">
#                 <a href="{% url 'BANNERList' %}?is_draft=True" class="nav-link active"><i
#                         class="fas fa-drafting-compass nav-icon text-info"></i>
#                     <p><b> Draft BANNERs</b></p>
#                 </a>
#             </li>
#             {% elif request.GET.is_verified and BANNERManager and allBANNERS %}
#             <li class="nav-item sidebar-control">
#                 <a href="{% url 'BANNERList' %}?is_verified=True" class="nav-link active"><i
#                         class="fas fa-check-circle nav-icon text-success"></i>
#                     <p><b> Active BANNERs</b></p>
#                 </a>
#             </li>
#             {% elif request.GET.is_active and BANNERManager and allBANNERS %}
#             <li class="nav-item sidebar-control">
#                 <a href="{% url 'BANNERList' %}?is_active=True" class="nav-link active"><i
#                         class="fas fa-exclamation-triangle nav-icon text-warning"></i>
#                     <p><b> Deactive BANNERs</b></p>
#                 </a>
#             </li>
#             {% elif request.GET.is_deleted and BANNERManager and allBANNERS %}
#             <li class="nav-item sidebar-control">
#                 <a href="{% url 'BANNERList' %}?is_deleted=True" class="nav-link active"><i
#                         class="fas fa-trash-alt nav-icon text-danger"></i>
#                     <p><b> Deleted BANNERs</b></p>
#                 </a>
#             </li>
#             {% else %}
#             <li class="nav-item sidebar-control">
#                 <a href="{% url 'BANNERList' %}?is_draft=True" class="nav-link"><i
#                         class="fas fa-th-list nav-icon"></i>
#                     <p> All BANNERs</p>
#                 </a>
#             </li>
#             {% endif %}

#         </ul>
#     </li>
#     {% endif %}
