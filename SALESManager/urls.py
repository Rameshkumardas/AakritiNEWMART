from django.urls import path
from . import CRUDOperation, views, AJAXService, deliveryMANAGER


urlpatterns = [
    
     
        path('ALLORDERList/', views.ALLORDERList.as_view(), name='ALLORDERList'),  

        path('MoveToTrash/ORDER/<int:pk>/', CRUDOperation.MoveToTrash, name='MoveToTrash'),
        path('RestoreFromTrash/ORDER/<int:pk>/', CRUDOperation.RestoreFromTrash, name='RestoreFromTrash'),
        path('delete/ORDER/<int:pk>/', CRUDOperation.deleteORDER, name='deleteORDER'),
        path('confirmed/ORDER/<int:pk>/', CRUDOperation.confirmORDER, name='confirmORDER'),
        path('shippedORDER/ORDER/<int:pk>/', CRUDOperation.shippedORDER, name='shippedORDER'),
        path('CancelORDER/ORDER/<int:pk>/', CRUDOperation.CancelORDER, name='CancelORDER'),
        path('OnTheWayORDER/ORDER/<int:pk>/', CRUDOperation.OnTheWayORDER, name='OnTheWayORDER'),
        path('deliveredORDER/ORDER/<int:pk>/', CRUDOperation.deliveredORDER, name='deliveredORDER'),
        
        path('Delivered/', deliveryMANAGER.productDelivered, name='productDelivered'),
        path('Replacement/', deliveryMANAGER.replacementORDER, name='replacementORDER'),
        path('ReturnandCancel/', deliveryMANAGER.cancelORDER, name='cancelORDER'),
        # ===============================================================================================================================================
        # ===============================================================================================================================================
        path('INVOICE/<orderId>/<int:user>/<int:pk>/', views.productINVOICE, name='productADMININVOICE'),
        # ===============================================================================================================================================
        # ===============================================================================================================================================
        path('AJAXService/ORDER/SHIPPEDTHISPRODUCT_US/', AJAXService.SHIPPEDTHISPRODUCT_BY_US, name='SHIPPEDTHISPRODUCT_US'), 
        

        # ===============================================================================================================================================
        # ===============================================================================================================================================
        path('AJAXService/ORDER/CODVerificationCode/', AJAXService.COD_ORDER_GENERATE, name='CODVerificationCode'), 
        path('AJAXService/COD_ORDER_CONFIRM_AND_VERIFY/', AJAXService.COD_ORDER_CONFIRM_AND_VERIFY, name='COD_ORDER_CONFIRM_AND_VERIFY'), 
        # ===============================================================================================================================================
        # ===============================================================================================================================================
        path('AJAXService/ORDER/ORDER_GENERATE_WITH_RAZORPAY/', AJAXService.ORDER_GENERATE_WITH_RAZORPAY, name='ORDER_GENERATE_WITH_RAZORPAY'), 
        path('AJAXServiceProvider/PAYMENTVERIFICATIONWITHrazorpay/', AJAXService.PAYMENTVERIFICATIONWITHRAZORPAY, name='PAYMENT_VERIFICATION_WITH_RAZORPAY'), 




        

        # ===============================================================================================================================================
        # ===============================================================================================================================================
        
        
        # ===============================================================================================================================================
        # ===============================================================================================================================================
        # ===============================================================================================================================================
        # ===============================================================================================================================================
        # ===============================================================================================================================================

]

