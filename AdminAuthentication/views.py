
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout
import re 
import random
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import Http404
from django.contrib import messages

from AdminAuthentication.models import AdminRegistration
from django.contrib.auth.decorators import login_required

# Create your views here.
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
password_validator = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

def AdminLockScreen(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user:
            return render(request,"templadmin/adminLocksScreen.html")
        else:   
            raise Http404
    else:   
        raise Http404
    
def AdminRecoverPassword(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user:
            return render(request,"template/admin/adminRecoverPassword.html")
        else:   
            raise Http404
    else:   
        raise Http404