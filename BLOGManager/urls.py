from BLOGManager.AJAXService import AJAXService, AJAXAUTOUPDATEBLOG, MAINCATBLOGBULKAJAX, SUBCATBLOGBULKAJAX, BLOGMainCatImportExport, BLOGSubImportExport, BLOGImportExport, BLOGBULKAJAX
from . import BLOGCatManager, BLOGManager, BLOGSubCatMnager
from django.urls import path

urlpatterns = [
    # ===================MANAGE-BLOGMainCat====================   
    # ===================MANAGE-BLOGMainCat====================   
    path('MainCat/all', BLOGCatManager.CreateBLOGMainCat, name='blogMainCategory'),  
    path('update/mainCat/<int:pk>/', BLOGCatManager.UpdateBLOGMainCat, name='blogUpdateMainCategory'),
    path('activated/mainCat/<int:pk>/', BLOGCatManager.ActivatedBLOGMainCat, name='blogActivatedMainCategory'),
    path('deactivated/mainCat/<int:pk>/', BLOGCatManager.DeactivatedBLOGMainCat, name='blogDeactivatedMainCategory'),
    path('copy/mainCat/<int:pk>/', BLOGCatManager.CopyBLOGMainCat, name='blogCopyMainCategory'),
    path('delete/mainCat/<int:pk>/', BLOGCatManager.DeleteBLOGMainCat, name='blogDeleteMainCategory'),
    # ===========================================================================
    path('DELETEBLOGMainCat/', AJAXService.DELETEBLOGMainCat, name='DELETEBLOGMainCat'), 
    # ===========================================================================        
    # ===========================================================================       
    path('AJAXService/BLOGMainCatImport/', BLOGMainCatImportExport.BLOGMainCatImport, name='BLOGMainCatImport'), 
    path('AJAXService/BLOGMainCatExport/', BLOGMainCatImportExport.BLOGMainCatExport, name='BLOGMainCatExport'), 
    # ===========================================================================       
    path('AJAXService/BULK_ACTIVATE_BLOG_MAIN_CATEGORY/', MAINCATBLOGBULKAJAX.BULK_ACTIVATE_BLOG_MAIN_CATEGORY, name='BULK_ACTIVATE_BLOG_MAIN_CATEGORY'), 
    path('AJAXService/BULK_DEACTIVATE_BLOG_MAIN_CATEGORY/', MAINCATBLOGBULKAJAX.BULK_DEACTIVATE_BLOG_MAIN_CATEGORY, name='BULK_DEACTIVATE_BLOG_MAIN_CATEGORY'), 
    path('AJAXService/BULK_DELETE_BLOG_MAIN_CATEGORY/', MAINCATBLOGBULKAJAX.BULK_DELETE_BLOG_MAIN_CATEGORY, name='BULK_DELETE_BLOG_MAIN_CATEGORY'), 
    # ===========================================================================       

    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
    # ===================MANAGE-BLOGSubCat====================   
    # ===================MANAGE-BLOGSubCat====================   
    path('BLOGSubCat/all', BLOGSubCatMnager.CreateSubCategory, name='blogSubCategory'), 
    path('deleteBLOGSubCat/<int:pk>/', BLOGSubCatMnager.DeleteSubCategory, name='deleteBLOGSubCat'),   
    path('updateBLOGSubCat/<int:pk>/', BLOGSubCatMnager.UpdateSubCategory, name='updateBLOGSubCat'),   
    path('copyBLOGSubCat/<int:pk>/', BLOGSubCatMnager.CopySubCategory, name='copyBLOGSubCat'),   
    path('activatedBLOGSubCat/<int:pk>/', BLOGSubCatMnager.activatedSubCategory, name='activatedBLOGSubCat'),
    path('deactivatedBLOGSubCat/<int:pk>/', BLOGSubCatMnager.deactivatedSubCategory, name='deactivatedBLOGSubCat'),
    # ===========================================================================
    path('DELETEBLOGSubCat/', AJAXService.DELETEBLOGSubCat, name='DELETEBLOGSubCat'), 
    # ===========================================================================   
    path('AJAXService/BLOGSubCatImport/', BLOGSubImportExport.BLOGSubCatImport, name='BLOGSubCatImport'), 
    path('AJAXService/BLOGSubCatExport/', BLOGSubImportExport.BLOGSubCatExport, name='BLOGSubCatExport'), 
    # =============================AJAX METHOD ONLY==============================   
    # ===========================================================================       
    path('AJAXService/BULK_ACTIVATE_BLOG_SUB_CATEGORY/', SUBCATBLOGBULKAJAX.BULK_ACTIVATE_BLOG_SUB_CATEGORY, name='BULK_ACTIVATE_BLOG_SUB_CATEGORY'), 
    path('AJAXService/BULK_DEACTIVATE_BLOG_SUB_CATEGORY/', SUBCATBLOGBULKAJAX.BULK_DEACTIVATE_BLOG_SUB_CATEGORY, name='BULK_DEACTIVATE_BLOG_SUB_CATEGORY'), 
    path('AJAXService/BULK_DELETE_BLOG_SUB_CATEGORY/', SUBCATBLOGBULKAJAX.BULK_DELETE_BLOG_SUB_CATEGORY, name='BULK_DELETE_BLOG_SUB_CATEGORY'), 
    # ===========================================================================       

    path('LoadBLOGSubCatLIST/', BLOGManager.LoadBLOGSubCatLIST, name='LoadBLOGSubCatLIST'), 
    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
    # ==================================MANAGE-BLOG==============================   
    # ==================================MANAGE-BLOG==============================   
    path('BLOGList/', BLOGManager.ALLBLOGList.as_view(), name='BLOGList'),                   
    path('createBLOG/', BLOGManager.CreateBLOG, name='createBLOG'),
    path('updateBLOG/<slug>/', BLOGManager.updateBLOG, name='updateBLOG'),
    path('activateBLOG/<int:pk>/', BLOGManager.activateBLOG, name='activateBLOG'),
    path('deactivateBLOG/<int:pk>/', BLOGManager.deactivateBLOG, name='deactivateBLOG'),
    path('deleteBLOG/<int:pk>/', BLOGManager.deleteBLOG, name='deleteBLOG'),
    path('restoreBLOG/<int:pk>/', BLOGManager.restoreBLOG, name='restoreBLOG'),
    path('PermanentDeleteBLOG/<int:pk>/', BLOGManager.PermanentDeleteBLOG, name='PermanentDeleteBLOG'),
    # ===========================================================================        
    # ===========================================================================  
    path('AJAXService/AUTOUPDATEBLOG/', AJAXAUTOUPDATEBLOG.AUTOUPDATEBLOG, name='AUTOUPDATEBLOG'), 
    # ===========================================================================   
    path('AJAXService/BLOGImport/', BLOGImportExport.BLOGImport, name='BLOGImport'), 
    path('AJAXService/BLOGExport/', BLOGImportExport.BLOGExport, name='BLOGExport'), 
    # ===========================================================================         
    path('AJAXService/BULK_ACTIVATE_BLOG/', BLOGBULKAJAX.BULK_ACTIVATE, name='BULK_ACTIVATE_BLOG'), 
    path('AJAXService/BULK_DEACTIVATE_BLOG/', BLOGBULKAJAX.BULK_DEACTIVATE, name='BULK_DEACTIVATE_BLOG'), 
    path('AJAXService/BULK_MOVE_TO_TRASH_BLOG/', BLOGBULKAJAX.BULK_MOVE_TO_TRASH, name='BULK_BLOG_MOVE_TO_TRASH_BLOG'), 
    path('AJAXService/BULK_RESTORE_FROM_TRASH_BLOG/', BLOGBULKAJAX.BULK_RESTORE_FROM_TRASH, name='BULK_BLOG_RESTORE_FROM_TRASH'), 
    path('AJAXService/BULK_PERMANENTLY_DELETE_BLOG/', BLOGBULKAJAX.BULK_PERMANENTLY_DELETE, name='BULK_PERMANENTLY_DELETE_BLOG'), 
    # ===========================================================================       

    # ---------------------------------------------------------------------------------------------------------
    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
    # ---------------------------------------------------------------------------------------------------------
]
# ---------------------------------------------------------------------------------------------------------
# ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
# ---------------------------------------------------------------------------------------------------------
# {% if request.user.is_accountant %}
# <li class="nav-header text-light"><b>CONTENT MANAGER</b></li>
# {% if BLOGManager %}
# <li class="nav-item menu-open">
#     {% else %}
# <li class="nav-item">
#     {% endif %}
#     {% if BLOGManager %}
#     <a href="#" class="nav-link active"><i class="fas fa-laptop-code nav-icon"></i>
#         <p><b>BLOG Manager</b><i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% else %}
#     <a href="#" class="nav-link"><i class="fas fa-laptop-code nav-icon"></i>
#         <p>BLOG Manager<i class="fas fa-angle-left right"></i></p>
#     </a>
#     {% endif %}
#     <ul class="nav nav-treeview">
#         <li class="nav-item sidebar-control">
                # <li class="nav-item sidebar-control">
                #     {% if blogMainCatActive %}
                #     <a href="{% url 'blogMainCategory' %}" class="nav-link active">
                #         <i class="far fa-edit nav-icon text-primary"></i>
                #         <p><b>blog Main Category</b></p>
                #     </a>
                #     {% else %}
                #     <a href="{% url 'blogMainCategory' %}" class="nav-link">
                #         <i class="fas fa-th nav-icon"></i>
                #         <p>blog Main Category</p>
                #     </a>
                #     {% endif %}
                # </li>
#             <li class="nav-item sidebar-control">
#                 {% if blogSubCat %}
#                 <a href="{% url 'blogSubCategory' %}" class="nav-link active">
#                     <i class="far fa-edit nav-icon text-primary"></i>
#                     <p><b>BLOGSubCat</b></p>
#                 </a>
#                 {% else %}
#                 <a href="{% url 'blogSubCategory' %}" class="nav-link">
#                     <i class="fas fa-th nav-icon"></i>
#                     <p>BLOGSubCat</p>
#                 </a>
#                 {% endif %}
#             </li>
#             <li class="nav-item sidebar-control">
#                 {% if CreateBlogs %}
#                 <a href="{% url 'createBLOG' %}" class="nav-link active">
#                     <i class="fas fa-edit nav-icon text-primary"></i>
#                     <p><b>Create Blog</b></p>
#                 </a>
#                 {% else %}
#                 <a href="{% url 'createBLOG' %}" class="nav-link">
#                     <i class="fas fa-edit nav-icon"></i>
#                     <p>Create Blog</p>
#                 </a>
#                 {% endif %}
#             </li>
            
#         {% if request.GET.is_draft and BLOGManager and allBLOGS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'BLOGList' %}?is_draft=True" class="nav-link active"><i
#                     class="fas fa-drafting-compass nav-icon text-info"></i>
#                 <p><b> Draft Blogs</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_verified and BLOGManager and allBLOGS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'BLOGList' %}?is_verified=True" class="nav-link active"><i
#                     class="fas fa-check-circle nav-icon text-success"></i>
#                 <p><b> Active Blogs</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_active and BLOGManager and allBLOGS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'BLOGList' %}?is_active=True" class="nav-link active"><i
#                     class="fas fa-exclamation-triangle nav-icon text-warning"></i>
#                 <p><b> Deactive Blogs</b></p>
#             </a>
#         </li>
#         {% elif request.GET.is_deleted and BLOGManager and allBLOGS %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'BLOGList' %}?is_deleted=True" class="nav-link active"><i
#                     class="fas fa-trash-alt nav-icon text-danger"></i>
#                 <p><b> Deleted Blogs</b></p>
#             </a>
#         </li>
#         {% else %}
#         <li class="nav-item sidebar-control">
#             <a href="{% url 'BLOGList' %}?is_draft=True" class="nav-link"><i
#                     class="fas fa-th-list nav-icon"></i>
#                 <p> All Blogs</p>
#             </a>
#         </li>
#         {% endif %}
#     </ul>
# </li>
# {% endif %}
           

