from AdminAuthentication.models import AdminActivity, AdminRegistration 
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from django.template.loader import render_to_string
from ExtraSettings.models import PROJECTInformation
from AdminAuthentication.Thread import EmailThread
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.http import Http404
from random import choice
import re 

valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
password_validator = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

def AdminVerification(request, email):
    if request.user.is_authenticated:
        return redirect('DefaultDashboard')
    else:
        if request.method=="POST":
            if request.POST['verification']!='':
                admin = AdminRegistration.objects.get(email=email, is_accountant=True)
                try:
                    if (request.POST['verification'] == request.session['AdminVerificationCode']) and (email==admin.email) and (admin.login_block==False):
                        if admin.login_block == False:    
                            messages.success(request, f"Welcome to {request.session['project']}.")
                            return redirect('AdminLogin')
                        else:
                            messages.error(request, 'Blocked! - You Dont Have Access')
                            return redirect('/')
                    else:
                        if admin.AttemptCount >= 3 and email==admin.email:
                            logout(request)
                            messages.error(request, 'No More Attempt & Try Again Later')
                            AdminRegistration.objects.filter(email=email, is_accountant=True).update(AttemptCount=0, login_block=True)
                            return redirect('/')
                        else:
                            AdminRegistration.objects.filter(email=email, is_accountant=True).update(AttemptCount=admin.AttemptCount+1)
                            messages.error(request, 'Verification Code Not Valid!')
                            return render(request, './template/admin/verification/adminVerification.html', {'code':request.session['AdminVerificationCode']})
                except Exception:
                    messages.success(request, 'Refresh Page Again')
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Verification Code Required*')
                return render(request, './template/admin/verification/adminVerification.html', {'code':request.session['AdminVerificationCode']})
        
        if email != "":
            if(re.search(valid_email, email)):   
                if AdminRegistration.objects.filter(email=email, is_accountant=True, is_suspended=False, is_verified=True, is_active=True).exists():
                    logout(request)
                    try:
                        admin = AdminRegistration.objects.get(email=email, is_accountant=True)    
                        project = PROJECTInformation.objects.last()
                        request.session['AdminVerificationCode'] = f'{project.name}'+''.join((choice('!@#$%^&*()0o') for i in range(10)))
                        request.session['AdminVerificationEmail'] = email
                        request.session['project'] = project.name
                        context = {
                            'code': request.session['AdminVerificationCode'],
                            'admin': admin,
                            'project': project,
                            'date': timezone.now(),

                        } 
                        # ==================================================================================
                        CONFIG_SMTP_NO_REPLY()
                        html_content = render_to_string("./template/admin/email/adminVerificationCode.email.html", context)
                        recipient_list = [email,]            
                        EmailThread(f'Admin Verification Code  || {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
                        # ==================================================================================                    
                        AdminActivity.objects.create(admin=admin, log='<span class="text-success">Your Email Id Used<span>')
                        messages.success(request, 'Get Verification Code From Mail')
                        return render(request, './template/admin/verification/adminVerification.html', )
                    except Exception as a:
                        print(a)
                        raise Http404
                else:
                    raise Http404
            else:   
                raise Http404
        else:   
            raise Http404



