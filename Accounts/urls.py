from SALESManager.views import productINVOICEFORUser
from Accounts import AJAXService as AJAX
from django.urls import path
from . import views, dashboard
# from eCommerce import activityMANAGER as activity

urlpatterns = (
            path('AJAXService/GetOneTimeVerificationCode/', AJAX.GetOneTimeVerificationCode, name='GetOneTimeVerificationCode'), 
            path('dashbaord/', dashboard.Dashboard, name='Dashboard'), 
            path('address/', dashboard.Address, name='Address'), 
            path('orders/', dashboard.Orders, name='Orders'), 

            path('order/<orderId>/', views.ViewConfirmOrder, name='ViewConfirmOrder'), 
                        
            # path('OrderConfirm/<orderId>/', activity.OrderConfirm, name='OrderConfirm'), 
            path('invoice/<orderId>/<user>/<pk>/', productINVOICEFORUser, name='productINVOICEFORUser'), 
            # path('order/<int:pk>/', dashboard.cancelORDER, name='cancelORDER'), 
            # ==============================================================================
            # path('create-new-account/', views.CREATE_NEW_USER, name='CREATE_NEW_USER'), 
            # path('forgot-user-password/', views.FORGOT_USER_ACCOUNT, name='FORGOT_USER_ACCOUNT'), 
            # path('AccountVerification/<token>/', views.AccountVerification, name='AccountVerification'), 
            # ==============================================================================
            # ACCOUNTS SETTINGS
            path('AJAXService/updateIMG/', AJAX.updateIMG, name='updateIMG'), 
            path('AJAXService/updateINFORMATION/', AJAX.updateINFORMATION, name='updateINFORMATION'), 
            path('AJAXService/updatePASSWORD/', AJAX.updatePASSWORD, name='updatePASSWORD'), 
            # ==============================================================================
            # ==============================================================================
            path('AJAXService/USERLOGINRequest/', AJAX.USERLOGINRequest, name='USERLOGINRequest'), 
            # path('AJAXService/USERRegstrationRequest/', AJAX.USERRegstrationRequest, name='USERRegstrationRequest'), 
            path('AJAXService/USERFORGOTRequest/', AJAX.USERFORGOTRequest, name='USERFORGOTRequest'), 
            path('AJAXService/USERVERIFYFORGOTRequest/', AJAX.USERVERIFYFORGOTRequest, name='USERVERIFYFORGOTRequest'), 
            path('AJAXService/updateUSERPROFILE/', AJAX.updateUSERPROFILE, name='updateUSERPROFILE'), 
            path('AJAXService/updateBILLINGAddress/', AJAX.updateBILLINGAddress, name='updateBILLINGAddress'), 
            # path('AJAXService/GetOneTimeVerificationCode/', AJAX.GetOneTimeVerificationCode, name='GetOneTimeVerificationCode'), 
            path('AJAXService/VerifyOneTimeVerificationCode/', AJAX.VerifyOneTimeVerificationCode, name='VerifyOneTimeVerificationCode'), 
            path('AJAXService/SaveAndChangePassword/', AJAX.SaveAndChangePassword, name='SaveAndChangePassword'), 
            path('AJAXService/createBILLINGAddress/', AJAX.BILLINGAddress, name='BILLINGAddress'), 
            path('AJAXService/updateBILLINGAddress/', AJAX.updateBILLINGAddress, name='updateBILLINGAddress'), 
            path('AJAXService/deleteBILLINGAddress/<int:pk>/', AJAX.deleteBILLINGAddress, name='deleteBILLINGAddress'), 
           
            path('AJAXService/createSHIPPINGAddress/', AJAX.SHIPPINGAddress, name='SHIPPINGAddress'), 
            path('AJAXService/updateSHIPPINGAddress/', AJAX.updateSHIPPINGAddress, name='updateSHIPPINGAddress'), 
            path('AJAXService/deleteSHIPPINGAddress/<int:pk>/', AJAX.deleteSHIPPINGAddress, name='deleteSHIPPINGAddress'), 
            path('AJAXService/LOGOUTUSER/', AJAX.LOGOUTUSER, name='LOGOUTUSER'), 
    )



































































































































































# from Accounts.api.UPDATEUSERInformations import UPDATEUSERINFORMATION, UPDATEUSERIMG
# from Accounts.api.UPDATEUSERInformations import UPDATEUSERINFORMATION



    # path('UPDATEUSERINFORMATION/<int:pk>', UPDATEUSERINFORMATION.as_view(), name="UPDATEUSERINFORMATIONAPI"),
    # path('UPDATEUSERIMG/<int:pk>', UPDATEUSERIMG.as_view(), name="UPDATEUSERIMGAPI"),
    # path('UserRegistration', views.STRIKEINDIAUserRegistration.as_view(), name="UserRegistrationAPI"),
    # path('UserVerification', USERVerification.as_view(), name="UserVerificationAPI"),
    # path('UserLogOut', USERLogOut.as_view(), name="UserLogOutAPI"),