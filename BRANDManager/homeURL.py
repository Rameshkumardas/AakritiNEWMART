from django.urls import path
from . import homeBRANDS as views

urlpatterns =[
            path('brand/<slug>/', views.BRAND, name='BRANDVIEW'),          
        ]



