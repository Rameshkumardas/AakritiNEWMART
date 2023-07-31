from django.urls import path
from . import userMANAGER as views
from .AJAXService import USERImportExport

urlpatterns = [

    path('ALLUSERList/', views.ALLUSERList.as_view(), name='ALLUSERList'),    

    path('activateUSER/<int:pk>/', views.activateUSER, name='activateUSER'),
    path('deactivateUSER/<int:pk>/', views.deactivateUSER, name='deactivateUSER'),
    path('deleteUSER/<int:pk>/', views.deleteUSER, name='deleteUSER'),
    path('restoreUSER/<int:pk>/', views.restoreUSER, name='restoreUSER'),
    path('PermanentDeleteUSER/<int:pk>/', views.PermanentDeleteUSER, name='PermanentDeleteUSER'),
    
    # ===========================================================================   
    path('AJAXService/USERImport/', USERImportExport.USERImport, name='USERImport'), 
    path('AJAXService/USERExport/', USERImportExport.USERExport, name='USERExport'), 

]