from django.urls import path
from . import staffMANAGER as views
from .AJAXService import STAFFImportExport

urlpatterns = [
    path('All-Staffs/', views.AllStaffs, name='AllStaffs'),    
    path('DeleteAdmin/<int:pk>/', views.DeleteAdmin, name='DeleteAdminAccount'),    
    path('Update/<int:pk>/', views.UpdateStaffAccount, name='StaffUpdate'),  
    path('Update/<int:pk>/', views.UpdateStaffAccount, name='StaffUpdate'),  
    path('activateSTAFF/<int:pk>/', views.activateAdmin, name='activateAdmin'),    
    path('deactivateSTAFF/<int:pk>/', views.deactivateAdmin, name='deactivateAdmin'),    
    # ===========================================================================   
    path('AJAXService/STAFFImport/', STAFFImportExport.STAFFImport, name='STAFFImport'), 
    path('AJAXService/STAFFExport/', STAFFImportExport.STAFFExport, name='STAFFExport'), 
]

