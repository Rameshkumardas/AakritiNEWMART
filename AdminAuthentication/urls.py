from AdminAuthentication import AdminProfile
from . import NSGPost, views, AdminRegistration, AdminLogin, AdminLogOut, AdminForgetPassword
from django.urls import path

urlpatterns = [  
            path('@AdminProfile/', AdminProfile.AdminProfile, name='AdminProfile'),  
            path('@deleteLOG/<int:pk>/', AdminProfile.deleteLOG, name='deleteLOG'),  
            path('@deleteALLLOGS/', AdminProfile.deleteALLLOGS, name='deleteALLLOGS'),  
            path('allowmeasa/admin/<email>/', NSGPost.AdminVerification, name='AdminVerification'),            
            path('AdminLogin/', AdminLogin.AdminLogin, name='AdminLogin'),  
            path('AdminRegistration/', AdminRegistration.AdminRegistrationCenter, name='AdminRegistration'),       
            path('AdminForgetPassword/', AdminForgetPassword.AdminForgetPassword, name='AdminForgetPassword'),   
            path('AdminLockScreen/', views.AdminLockScreen, name='AdminLockScreen'),       
            path('AdminRecoverPassword/', views.AdminRecoverPassword, name='AdminRecoverPassword'),       
            path('AdminLogOut/', AdminLogOut.AdminLogOut, name='AdminLogOut'), 
        ]
