from django.urls import path
from Dashboard import views
    
urlpatterns =[
            path('', views.DefaultDashboard, name='DefaultDashboard'),       
            path('default/', views.DefaultDashboard, name='DefaultDashboard'),  
            
            
        ]



