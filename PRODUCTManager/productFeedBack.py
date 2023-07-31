from django.http import Http404
from django.shortcuts import render, redirect
from AdminAuthentication.models import AdminRegistration
from django.contrib import messages
import random
from PRODUCTManager.models import ProductRatting

# Create your views here.
def ProductFreedBack(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            rattings = ProductRatting.objects.all()
            context = {
                    'AllProducts':'menu-open', 
                    'productFeedback': 'active',
                    'rattings':rattings
            }
            return render(request,"./template/feedback/ProductFeedback.html", context)
        else:
            raise Http404
    else:
        raise Http404

