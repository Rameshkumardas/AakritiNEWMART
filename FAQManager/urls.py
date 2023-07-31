from django.urls import path
from . import  FAQManage, views, FAQMainCategory
from .AJAXService import FAQMAINCATBULKAJAX, FAQMainCatImportExport, FAQImportExport, FAQBULKAJAX
urlpatterns = [

                    path('FAQCatManager', FAQMainCategory.CreateFAQCategory, name='FAQCatManager'),       
                    path('FAQMainCategory/', FAQMainCategory.CreateFAQCategory, name='createFAQMainCategory'), 
                    path('deleteFAQmainCat/<int:pk>/', FAQMainCategory.DeleteFAQCategory, name='DeleteFAQMainCategory'),
                    path('updateFAQmainCat/<int:pk>/', FAQMainCategory.UpdateFAQCategory, name='UpdateFAQMainCategory'),
                    path('copyFAQmainCat/<int:pk>/', FAQMainCategory.CopyFAQCategory, name='CopyFAQMainCategory'),
                    path('ActivatedFAQmainCat/<int:pk>/', FAQMainCategory.ActivatedFAQCategory, name='ActivatedFAQMainCategory'),
                    path('DeactivatedFAQmainCat/<int:pk>/', FAQMainCategory.DeactivatedFAQCategory, name='DeactivatedFAQMainCategory'),
                    # ====================AJAX SERVECE===========================
                    path('AJAXService/CRUDOperation/DELETEFAQMainCat/', FAQMainCategory.DELETEFAQMainCat, name='DELETEFAQMainCat'),
                    # -------------------------------------------------------------------------------------------------------------------
                    path('AJAXService/FAQMainCatImport/', FAQMainCatImportExport.FAQMainCatImport, name='FAQMainCatImport'), 
                    path('AJAXService/FAQMainCatExport/', FAQMainCatImportExport.FAQMainCatExport, name='FAQMainCatExport'), 
                    # ===========================================================================       
                    path('AJAXService/BULK_ACTIVATE_FAQ_MAIN_CATEGORY/', FAQMAINCATBULKAJAX.BULK_ACTIVATE_FAQ_MAIN_CATEGORY, name='BULK_ACTIVATE_FAQ_MAIN_CATEGORY'), 
                    path('AJAXService/BULK_DEACTIVATE_FAQ_MAIN_CATEGORY/', FAQMAINCATBULKAJAX.BULK_DEACTIVATE_FAQ_MAIN_CATEGORY, name='BULK_DEACTIVATE_FAQ_MAIN_CATEGORY'), 
                    path('AJAXService/BULK_DELETE_FAQ_MAIN_CATEGORY/', FAQMAINCATBULKAJAX.BULK_DELETE_FAQ_MAIN_CATEGORY, name='BULK_DELETE_FAQ_MAIN_CATEGORY'), 
                    # ===========================================================================       



    path('FAQList/', FAQManage.ALLFAQList.as_view(), name='FAQList'),
    path('createFAQ/', FAQManage.createFAQ, name='createFAQ'),
    path('updateFAQ/<slug>/', FAQManage.updateFAQ, name='updateFAQ'),
    path('viewFAQ/<slug>/', FAQManage.viewFAQ, name='viewFAQ'),    
    # # =============================================================================
    # # =============================================================================
    # # FAQ OPERATIONS
    # # =============================================================================
    # # =============================================================================
    path('ActivateFAQ/<int:pk>/', FAQManage.ActivateFAQ, name='ActivateFAQ'),
    path('DeactivateFAQ/<int:pk>/', FAQManage.DeactivateFAQ, name='DeactivateFAQ'),
    path('DeleteFAQ/<int:pk>/', FAQManage.DeleteFAQ, name='DeleteFAQ'),
    path('RestoreFAQ/<int:pk>/', FAQManage.RestoreFAQ, name='RestoreFAQ'),
    path('deletePermanentlyFAQ/<int:pk>/', FAQManage.deletePermanentlyFAQ, name='deletePermanentlyFAQ'),
    # # =============================================================================
    # # =============================================================================
    # # AJAX SERVICE PROVIDER
    # # =============================================================================
    # # =============================================================================
    # # =============================================================================
    path('AJAXService/FAQImport/', FAQImportExport.FAQImport, name='FAQImport'), 
    path('AJAXService/FAQExport/', FAQImportExport.FAQExport, name='FAQExport'), 
    # ===========================================================================       
    path('AJAXService/BULK_ACTIVATE_FAQ/', FAQBULKAJAX.BULK_ACTIVATE, name='BULK_ACTIVATE_FAQ'), 
    path('AJAXService/BULK_DEACTIVATE_FAQ/', FAQBULKAJAX.BULK_DEACTIVATE, name='BULK_DEACTIVATE_FAQ'), 
    path('AJAXService/BULK_MOVE_TO_TRASH_FAQ/', FAQBULKAJAX.BULK_MOVE_TO_TRASH, name='BULK_MOVE_TO_TRASH_FAQ'), 
    path('AJAXService/BULK_RESTORE_FROM_TRASH_FAQ/', FAQBULKAJAX.BULK_RESTORE_FROM_TRASH, name='BULK_FAQ_RESTORE_FROM_TRASH'), 
    path('AJAXService/BULK_PERMANENTLY_DELETE_FAQ/', FAQBULKAJAX.BULK_PERMANENTLY_DELETE, name='BULK_PERMANENTLY_DELETE_FAQ'), 
    # # =============================================================================

    # # =============================================================================
    # # =============================================================================
    # # LOAD CATEGORY DATA USING AJAX METHOD
    # # =============================================================================
    # # =============================================================================    
]

# # =============================================================================
# # =============================================================================
# # FAQ template/slidebar.html Copy Past For This FAQ App.
# # =============================================================================
#   {% if FAQManager %}
    # <li class="nav-item menu-open">
    # {% else %}
    # <li class="nav-item">
    # {% endif %}

    #     {% if FAQManager %}
    #     <a href="#" class="nav-link active">
    #         <i class="nav-icon fa fa-rocket"></i>
    #         <p>FAQ Manager<i class="fas fa-angle-left right"></i></p>
    #     </a>
    #     {% else %}
    #     <a href="#" class="nav-link">
    #         <i class="nav-icon fas fa-copy"></i>
    #         <p>FAQ Manager<i class="fas fa-angle-left right"></i></p>
    #     </a>
    #     {% endif %}

    #     <ul class="nav nav-treeview">
    #         <li class="nav-item " >
    #             {% if FAQCat %}
    #             <a href="{% url 'FAQCatManager' %}" class="nav-link active">
    #                 <i class="fas fa-edit nav-icon text-primary"></i>
    #                 <p><b>FAQ Category</b></p>
    #             </a>
    #             {% else %}
    #             <a href="{% url 'FAQCatManager' %}" class="nav-link"><i class="fas fa-th-list nav-icon"></i>
    #                 <p>FAQ Category</p>
    #             </a>
    #             {% endif %}
    #         </li>

    #         <li class="nav-item " >
    #             {% if createFAQ %}
    #             <a href="{% url 'createFAQ' %}" class="nav-link active">
    #                 <i class="fas fa-edit nav-icon text-primary"></i>
    #                 <p><b>Create FAQ</b></p>
    #             </a>
    #             {% else %}
    #             <a href="{% url 'createFAQ' %}" class="nav-link">
    #                 <i class="fas fa-edit nav-icon"></i>
    #                 <p>Create FAQ</p>
    #             </a>
    #             {% endif %}
    #         </li>

    #         {% if updateFAQ %}
    #         <li class="nav-item " >
    #             <a href="{% url 'createFAQ' %}" class="nav-link active">
    #                 <i class="fas fa-edit nav-icon text-primary"></i>
    #                 <p><b>Update FAQ</b></p>
    #             </a>                                
    #         </li>
    #         {% endif %}

    #         {% if FAQManager and allFAQ and request.GET.is_draft %}
    #         <li class="nav-item " >
    #             <a href="{% url 'FAQList' %}?is_draft=True" class="nav-link active">
    #                 <i class="fas fa-th-list nav-icon text-primary"></i>
    #                 <p><b>Draft FAQs</b></p>
    #             </a>
    #         </li>
    #         {% elif FAQManager and allFAQ and request.GET.is_active %}
    #         <li class="nav-item " >
    #             <a href="{% url 'FAQList' %}?is_verified=True" class="nav-link  active">
    #                 <i class="fas fa-check-circle nav-icon text-success"></i>
    #                 <p><b>Active FAQs</b></p>
    #             </a>
    #         </li>
    #         {% elif FAQManager and allFAQ and request.GET.is_active %}
    #         <li class="nav-item " >
    #             <a href="{% url 'FAQList' %}?is_active=False" class="nav-link {% if request.GET.is_active %} active {% endif %}">
    #                 <i class="fas fa-exclamation-triangle nav-icon text-warning"></i>
    #                 <p><b>Deactive FAQs</b></p>
    #             </a>
    #         </li>
    #         {% elif FAQManager and allFAQ and request.GET.is_deleted %}
    #         <li class="nav-item " >
    #             <a href="{% url 'FAQList' %}?is_deleted=True" class="nav-link active ">
    #                 <i class="fas fa-trash-alt nav-icon text-danger"></i>
    #                 <p><b>Deleted FAQs</b></p>
    #             </a>
    #         </li>
    #         {% else %}
    #         <li class="nav-item " >
    #             <a href="{% url 'FAQList' %}?is_draft=True" class="nav-link ">
    #                 <i class="fas fa-th-list nav-icon"></i>
    #                 <p><b>All FAQs</b></p>
    #             </a>
    #         </li>
    #         {% endif %}
    #     </ul>
    # </li>
