from TESTIMONAILManager.AJAXService import TESTIMONAILImportExport 
from TESTIMONAILManager import TestimonailManager
from . import views, TestimonailCategory
from django.urls import path

urlpatterns = [

                    path('TestimonailCategory/', TestimonailCategory.CreateTestimonailCategory, name='CreateTestimonailCategory'),       
                    # path('MainCategory/', TestimonailCategory.CreateMainCategory, name='createMainCategory'), 
                    # path('updateTestimonailCat/<int:pk>/', TestimonailCategory.UpdateMainCategory, name='UpdateMainCategory'),

                    path('deleteTestimonailCat/<int:pk>/', TestimonailCategory.DeleteTestimonailCategory, name='DeleteTestimonailCategory'),
                    path('ActivatedTestimonailCat/<int:pk>/', TestimonailCategory.ActivatedTestimonailCategory, name='ActivatedTestimonailCategory'),
                    path('DeactivatedTestimonailCat/<int:pk>/', TestimonailCategory.DeactivatedTestimonailCategory, name='DeactivatedTestimonailCategory'),



                    
                    
                    path('TestimonailList/', TestimonailManager.ALLTestimonialList.as_view(), name='TestimonailList'), 
                    path('CreateTestimonail/', TestimonailManager.CreateTestimonail, name='CreateTestimonail'),       
                    path('updateTestimonail/<int:pk>/', TestimonailManager.updateTestimonail, name='updateTestimonail'),

                    path('ActivatedTestimonail/<int:pk>/', TestimonailManager.ActivatedTestimonail, name='ActivatedTestimonail'),
                    path('DeactivatedTestimonail/<int:pk>/', TestimonailManager.DeactivatedTestimonail, name='DeactivatedTestimonail'),

                    path('DeleteTestimonail/<int:pk>/', TestimonailManager.DeleteTestimonail, name='DeleteTestimonail'),
                    path('RestoreTestimonail/<int:pk>/', TestimonailManager.RestoreTestimonail, name='RestoreTestimonail'),
                    path('PermanentlyDeleteTestimonail/<int:pk>/', TestimonailManager.PermanentlyDeleteTestimonail, name='PermanentlyDeleteTestimonail'),



                    # ===========================================================================   
                    path('AJAXService/TESTIMONAILImport/', TESTIMONAILImportExport.TESTIMONAILImport, name='TESTIMONAILImport'), 
                    path('AJAXService/TESTIMONAILExport/', TESTIMONAILImportExport.TESTIMONAILExport, name='TESTIMONAILExport'), 
                    # ---------------------------------------------------------------------------------------------------------
                    # ----------Develop My Mr Das From Nepal Contact WhatApps. +91 7322057677----------------------------------
                    # ---------------------------------------------------------------------------------------------------------

                    ]

