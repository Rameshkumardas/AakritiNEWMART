from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from AdminAuthentication.decorators import accountant_required
from Message.models import Announcements
from django.core import serializers
import json 
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
# ==============================================================================
# ANNOUNCEMENT
# ==============================================================================
@accountant_required
def Announcement(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS'):
        context = {
            'Message': 'menu-open', 
            'Announcements': 'active',
            'AnnouncementList':Announcements.objects.all(),
        }
        return render(request,"./template/announcement/announcement.html", context)

    else:
        return redirect("AdminLogOut")
# ==============================================================================
# ANNOUNCEMENT LIST
# ==============================================================================
@accountant_required
def AnnouncementList(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS'):
        return JsonResponse({'AnnouncementList': serializers.serialize("json", Announcements.objects.all())})
    else:
        return redirect("AdminLogOut")
# ==============================================================================
# ADD NEW ANNOUNCEMENT
# ==============================================================================
@accountant_required
def addNEWAnnouncement(request):
    if request.user.is_admin:
        if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS'):
            subject = request.POST['subject']
            description = request.POST['description']
            if subject == '':
                return JsonResponse({'status':0, 'message':'Subject Field Required!'})
            elif description == '':
                return JsonResponse({'status':0, 'message':'Description Field Required!'})
            else:
                Announcements.objects.create(subject=subject, description=description, author=request.user)
                base_url = reverse('Announcements')  
                query_string =  urlencode({'is_draft': True}) 
                url = '{}?{}'.format(base_url, query_string) 
                context = {
                    'status':1, 
                    'message':'Announcement Created',
                    'redirectURL':url,
                    'AnnouncementList':'Announcement Created',
                }
                return JsonResponse(context)
        else:
            return redirect("AdminLogOut")
    else:
        return redirect("AdminLogOut")
# ==============================================================================
# COMMON OPERATION ANNOUNCEMENT
# ==============================================================================
@accountant_required
def commonOPERATIONSFORAnnouncement(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS'):

        target = request.POST['target']
        targetType = request.POST['targetType']
        if target == '':
            return JsonResponse({'status':0, 'message':'Target Not Found!'})
            
        elif targetType == '':
            return JsonResponse({'status':0, 'message':'Targettype Not Found!'})
    
        else:
            base_url = reverse('Announcements')  
            query_string =  urlencode({'is_draft': True}) 
            url = '{}?{}'.format(base_url, query_string) 

            if (targetType =='approved'):
                try:
                    approvedNOW = Announcements.objects.get(pk=target)
                    approvedNOW.status = 'approved'
                    approvedNOW.save()
                    return JsonResponse({'redirectURL':url,'status':1, 'message':'Announcement Approved', 'AnnouncementList': serializers.serialize("json", Announcements.objects.all())})
                except Announcements.DoesNotExist:
                    return JsonResponse({'status':0, 'message':'Something Went..'})
                    
            elif (targetType=='pending'):
                try:
                    approvedNOW = Announcements.objects.get(pk=target)
                    approvedNOW.status = 'pending'
                    approvedNOW.save()
                    return JsonResponse({'redirectURL':url, 'status':1, 'message':'Announcement Pending'})
                except Announcements.DoesNotExist:
                    return JsonResponse({'status':0, 'message':'Something Went..'})
                    
            elif (targetType=='delete'):
                try:
                    approvedNOW = Announcements.objects.get(pk=target)
                    approvedNOW.delete()
                    return JsonResponse({'redirectURL':url, 'status':1, 'message':'Announcement Deleted'})
                except Announcements.DoesNotExist:
                    return JsonResponse({'status':0, 'message':'Something Went..'})
                    
    else:
        return redirect("AdminLogOut")
# ==============================================================================
# MORE OTHER ACTION
# ==============================================================================









