from eCommerce import activityMANAGER as activity
from eCommerce import PRODUCTManager as product
from Accounts import AJAXService as Accounts
from SALESManager import views as seal
from django.urls import path
from . import views

urlpatterns = [
                # ================KHANTAILOR===============
                path('', views.eComHome, name='eComHome'), 
                path('cart', views.cart, name='cart'), 
                path('deleteMyCartList/', views.deleteMYCARTLIST, name='deleteMyCartList'), 
                path('deleteSINGLEPRODUCTFROMCART/<int:pk>/', views.deleteSINGLEPRODUCTFROMCART, name='deleteSINGLEPRODUCTFROMCART'), 

                path('product/all', product.allProductList, name='ProductList'), 
                path('product/<slug>/', product.VIEWProduct, name='VIEWProduct'),                     
                path('CheckOut', activity.CheckOut, name='CheckOutHere'), 
                # path('OrderConfirm/<orderId>/', activity.OrderConfirm, name='OrderConfirm'), 
                # path('productINVOICE/<orderId>/<user>/<pk>/', seal.productINVOICE, name='productINVOICE'),
            ]
