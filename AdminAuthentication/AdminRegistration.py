
import datetime
from AdminAuthentication.models import AdminRegistration
from django.template.loader import render_to_string
from AdminAuthentication.Thread import EmailThread
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from ExtraSettings.models import PROJECTInformation
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


import random
import re 
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
password_validator = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
def AdminRegistrationCenter(request):
    if request.user.is_authenticated:
        return redirect('DefaultDashboard')

    if request.method=="POST":
        if request.POST['full_name']!='':
            name = request.POST['full_name']
        else:
            messages.error(request, 'Full Name Required*')
            return redirect(request.META.get('HTTP_REFERER'))

        if request.POST['email']!='':
            if(re.search(valid_email,request.POST['email'])):   
                email = request.POST['email']
                username = email.split('@')[0]
            else:   
                messages.error(request, 'Email is Not Valid!')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Email Id Required*')
            return redirect(request.META.get('HTTP_REFERER'))

        if request.FILES.get('profileIMG') !='':
            img = request.FILES.get('profileIMG')
        else:
            messages.error(request, 'IMG Required*')
            return redirect(request.META.get('HTTP_REFERER'))

        if request.POST['contactNO']!='':
            contactNO = request.POST['contactNO']
        else:
            messages.error(request, 'contactNO Required*')
            return redirect(request.META.get('HTTP_REFERER'))
    
        if request.POST['password']!='':
            match_re = re.compile(password_validator)
            if(re.search(match_re, request.POST['password'])):
                password = request.POST['password']
            else:
                messages.error(request, "Password Not Formated")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Password Required*')
            return redirect(request.META.get('HTTP_REFERER'))
        
        if request.POST['repassword']!='':
            match_re = re.compile(password_validator)
            if(re.search(match_re, request.POST['repassword'])):
                repassword = request.POST['repassword']
            else:
                messages.error(request, "Password Not Formated")
                return redirect(request.META.get('HTTP_REFERER'))            
        else:
            messages.error(request, 'Repassword Required*')
            return redirect(request.META.get('HTTP_REFERER'))

        if(password != repassword):
            messages.error(request, 'Password Did Not Match!')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            if AdminRegistration.objects.filter(email=email).exists():
                messages.error(request, 'Already Account Exist!')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                AdminRegistration.objects.create_superadmin(name=name,email=email, username=username, password=password, phone=contactNO, img=img)
                try:
                    project = PROJECTInformation.objects.get(pk=1)
                except Exception:
                    PROJECTInformation.objects.create(name="AakritiCMS", title="Content Management System Develop By Mr Das : Ramesh Kuamr Das", mail='das82916@gmail.com', contact=7322057677, address='Siraha-21 Laxminya Siraha Provence No 2 ( NEPAL ) ')
                    project = PROJECTInformation.objects.get(pk=1)
                context = {
                    'email':email,
                    'mobileN':contactNO,
                    'password':password,
                    'fullname':name,
                    'date': datetime.datetime.now().strftime("%d %b %Y"),
                    'PROJECT':project,
                }

                EMAIL_HOST=project.EMAIL_HOST_NO_REPLY
                EMAIL_HOST_USER=project.EMAIL_HOST_USER_NO_REPLY
                EMAIL_HOST_PASSWORD=project.EMAIL_HOST_PASSWORD_NO_REPLY
                EMAIL_PORT=project.EMAIL_PORT_NO_REPLY
                EMAIL_USE_TLS=project.EMAIL_USE_TLS_NO_REPLY

                recipient_list = [email, ]
                html_content = render_to_string("./template/admin/email/adminActivateAccountForAdminAccess.html", context)
                EmailThread(f'Activate Account For Admin Access || {project.name}  ', EMAIL_HOST_USER, html_content, recipient_list).start()
                messages.success(request, 'Admin Create Success')
                return redirect(request.META.get('HTTP_REFERER'))

    return render(request,"./template/admin/adminRegistration.html")