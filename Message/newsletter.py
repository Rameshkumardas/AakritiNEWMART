from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Message.models import EmailNewslatters, MobileNewslatters

@login_required
def NewsletterList(request):
    context = {
        'Message': 'menu-open', 
        'Newsletter': 'active',
        'emailLIST':EmailNewslatters.objects.all(),
        'phoneLIST':MobileNewslatters.objects.all(),
    }
    return render(request,"./template/newsletters/newsletter.html",context)

@login_required
def sendMESSAGEWITHEMAIL(request):
    context = {
        'Message': 'menu-open', 
        'Newsletter': 'active',
    }
    return render(request,"./template/newsletters/sendEMAIL.html",context)

@login_required
def sendMESSAGEWITHNumber(request):
    context = {
        'Message': 'menu-open', 
        'Newsletter': 'active',
    }
    return render(request,"./template/newsletters/sendMESSAGEONPHONE.html",context)
