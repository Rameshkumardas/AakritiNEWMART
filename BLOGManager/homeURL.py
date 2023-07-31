from django.urls import path
from . import homeBLOGS as views
from .AJAXService import AJAXService
urlpatterns =[
            path('blogs/', views.ALLBLOGS, name='ALLBLOGS'),  
            path('blogs/<main_slug>/<slug>/', views.ALLSUBCATBLOGS, name='ALLSUBCATBLOGS'),  
            path('blogs/<slug>/', views.ALLMAINCATBLOGS, name='ALLMAINCATBLOGS'),  
            path('learn/<slug>/', views.BLOG, name='BLOGVIEW'),       
             
            path('AJAXService/ReplyComment/', AJAXService.ReplyCommentRequest, name='ReplyCommentRequest'),        
            path('AJAXService/DELETEComment/', AJAXService.DELETECommentRequest, name='DELETECommentRequest'),        

        ]



