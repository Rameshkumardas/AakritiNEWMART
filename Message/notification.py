from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, OperationalError
from django.shortcuts import render, redirect
from AdminAuthentication.models import AdminActivity
from Message.models import ContactUS
from django.contrib import messages

@login_required
def NotificationList(request):
    allNotification = AdminActivity.objects.all()
    context = {
        'Notification': 'menu-open', 
        'Notification': 'active',
        'NotificationList': allNotification,

    }
    return render(request,"./template/notification/notificationList.html",context)
