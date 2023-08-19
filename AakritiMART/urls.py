from AakritiMART.AJAXService import AJAXService as AJAX
from django.urls import path
from . import views

from django.contrib.sitemaps import GenericSitemap
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import  staticSiteMap, PageListSiteMap
from PRODUCTManager.sitemaps import MainCatProductListSiteMap, SubCatProductListSiteMap, SubSubCatProductListSiteMap, ProductListSiteMap

from BLOGManager.BLOGsitemap import MAINCATBLOGListSiteMap, SUBCATBLOGListSiteMap, BLOGListSiteMap

from CMSManager.PAGEsitemap import PAGEListSiteMap



sitemaps = {
    'static': staticSiteMap,
    
    'MainCatProductListSiteMap': MainCatProductListSiteMap,
    'SubCatProductListSiteMap': SubCatProductListSiteMap,
    'SubSubCatProductListSiteMap': SubSubCatProductListSiteMap,
    'ProductList': ProductListSiteMap,

    'MAINCATBLOGListSiteMap': MAINCATBLOGListSiteMap,
    'SUBCATBLOGListSiteMap': SUBCATBLOGListSiteMap,
    'BLOGListSiteMap': BLOGListSiteMap,

    'PAGEListSiteMap':PAGEListSiteMap,

}
urlpatterns = [
    
    
                path("robots.txt", TemplateView.as_view(template_name="./template/home/robots.txt", content_type="text/plain")),  
                path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
                # ===============================
                path('', views.allProducts, name='allProducts'), 
                # path('oops', views.AakritiMART, name='AakritiMART'), 
                path('contact-us/', views.ContactUs, name='ContactUs'), 
                path('my/compare/', views.CompareMART, name='CompareMART'), 
                path('my/wishlist/', views.WishlistMART, name='WishlistMART'), 
                path('my/cart/', views.MYCart, name='MYCart'), 

                path('all/<main_slug>/<sub_slug>/<slug>/', views.SubSubCatProductList, name='SubSubCatProductList'), 
                path('all/<main_slug>/<slug>/', views.subCatProductList, name='subCatProductList'), 
                path('all/<slug>/', views.mainCatProductList, name='mainCatProductList'), 
                
                
                path('checkout/', views.CheckOut, name='CheckOut'), 
                path('product/<slug>/', views.OPENProduct, name='OPENProduct'), 

                # ================================================================
                # ================================================================
                # ================================================================
                path('AJAXService/QUICKView/', views.QUICKView, name='QUICKView'), 
                
                path('AJAXService/addToCart/', AJAX.addToCart, name='addToCart'), 
                path('AJAXService/deleteCart/', AJAX.deleteCart, name='deleteCart'), 
                path('AJAXService/updateCART/', AJAX.updateCART, name='updateCART'), 

                path('AJAXService/addToWishlist/', AJAX.addToWishlist, name='addToWishlist'), 
                path('AJAXService/deleteWishlistProduct/', AJAX.deleteWishlistProduct, name='deleteWishlistProduct'), 

                path('AJAXService/COMPAREProduct/', AJAX.COMPAREProduct, name='COMPAREProduct'), 
                path('AJAXService/deleteCOMPAREProduct/', AJAX.deleteCOMPAREProduct, name='deleteCOMPAREProduct'), 
                
                
                
                path('AJAXService/WRITEREVIEWRequest/', AJAX.WRITEREVIEWRequest, name='WRITEREVIEWRequest'), 
                path('AJAXService/ASKQuestion/', AJAX.ASKQuestion, name='ASKQuestion'), 
                
                 path('AJAXService/QUICKASKQuestion/', AJAX.QUICKASKQuestion, name='QUICKASKQuestion'), 

               
                path('AJAXService/ReplyQuestionWithAnswer/', AJAX.ReplyQuestionWithAnswer, name='ReplyQuestionWithAnswer'), 
                path('AJAXService/DELETEQA/', AJAX.DELETEQA, name='DELETEQA'), 

                path('AJAXService/CheckShipping/', AJAX.CheckShipping, name='CheckShipping'), 
                
                
            ]
