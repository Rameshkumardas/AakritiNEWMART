from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from Message.models import Announcements

@login_required
def Announcement(request):
    context = {
        'Message': 'menu-open', 
        'Announcements': 'active',
        'AnnouncementList': Announcements.objects.all(),
    }
    return render(request,"./template/announcement.html", context)



    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    