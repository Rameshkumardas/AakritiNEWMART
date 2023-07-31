# from AdminAuthentication.Client import get_client_ip
from AdminAuthentication.models import AdminActivity, AdminRegistration
from django.contrib.auth import authenticate, login, logout
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from django.template.loader import render_to_string
from ExtraSettings.models import PROJECTInformation
from AdminAuthentication.Thread import EmailThread
from rest_framework.authtoken.models import Token
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import Http404
import datetime
import re

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
password_validator = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
def AdminLogin(request):
    if request.session.has_key('AdminVerificationCode') and request.session.has_key('AdminVerificationEmail'):
        if request.user.is_authenticated:
            return redirect('DefaultDashboard')
        elif request.method == 'POST':        
            try:
                if request.POST['email']!='':
                    if(re.search(valid_email,request.POST['email'])):   
                        if request.POST['email'] == request.session['AdminVerificationEmail']:
                            email = request.POST['email']
                        else:
                            messages.error(request, 'I Have Already Request.')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:   
                        messages.error(request, 'Email is Not Valid!')
                        return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, 'Email Id is Empty!')
                    return redirect(request.META.get('HTTP_REFERER'))

                if request.POST['password']!='':
                    password = request.POST['password']
                else:
                    messages.error(request, 'Password is Empty!')
                    return redirect(request.META.get('HTTP_REFERER'))
                if AdminRegistration.objects.filter(email=email, login_block=False, is_verified=True, is_active=True , is_accountant=True).exists():
                    admin = AdminRegistration.objects.get(email=email, login_block=False, is_verified=True, is_active=True, is_accountant=True)
                    db_password = admin.password
                    db_email = admin.email  
                    db_role = admin.role  
                    db_name = admin.name
                    db_Contact = admin.phone
                    user = authenticate(request, email=email, password=password)
                    if user is not None:
                        login(request, user)
                        Token.objects.filter(user=admin).delete()
                        token = Token.objects.create(user=admin)
                        if token:
                            if request.user.is_authenticated:
                                AdminRegistration.objects.filter(email=email).update(is_login=True, token=token.key)
                                client_ip = get_client_ip(request)
                                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> LogIn Success With <span class="text-primary">[ {client_ip} ]</span> Ip.<span>')
                                request.session['SUPERADMIN'] = db_email
                                request.session['ADMINUSERID'] = admin.pk
                                request.session['ADMIN-PASS'] = True
                                request.session['token'] = token.key
                                request.session['ADMIN-ROLE'] = db_role
                                try:
                                    project = PROJECTInformation.objects.get(pk=1)
                                except Exception:
                                    project=False

                                context = {
                                    'fullname':db_name,
                                    'data':datetime.datetime.now().strftime("%d %b, %Y - %a %I:%M %p"),
                                    'email':db_email,
                                    'mobileN':db_Contact,
                                    'project':project,
                                } 
                                # ==================================================================================
                                CONFIG_SMTP_NO_REPLY()
                                # html_content = render_to_string("./template/email/adminLOGINSUCCESS.html", context)
                                # recipient_list = [email,]
                                # EmailThread(f'Hi [ { db_name } ] - Login Success | {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
                                # ==================================================================================
                                messages.success(request, 'Welcome Back! ' + ' - ' + db_name)
                                return redirect('DefaultDashboard')
                            else:
                                messages.error(request, 'Informations is Not Valid')
                                return redirect(request.META.get('HTTP_REFERER'))
                        else:
                            messages.error(request, 'Token Generate Error')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, 'Credentials Not Match')
                        return redirect(request.META.get('HTTP_REFERER'))                    
                else:
                    messages.error(request, 'Account Not Exist!')
                    return redirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, f'This Error: {e}')
                return redirect(request.META.get('HTTP_REFERER'))
        return render(request,"./template/admin/adminLogin.html")
    else:
        raise Http404

def NORMALADMINLogin(request):
    if request.user.is_authenticated:
        return redirect('DefaultDashboard')
    elif request.method == 'POST':        
        try:
            if request.POST['email']!='':
                if(re.search(valid_email, request.POST['email'])):   
                    if request.POST['email'] == request.POST['email']:
                        email = request.POST['email']
                    else:
                        messages.error(request, 'I Have Already Request.')
                        return redirect(request.META.get('HTTP_REFERER'))
                else:   
                    messages.error(request, 'Email is Not Valid!')
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Email Id is Empty!')
                return redirect(request.META.get('HTTP_REFERER'))

            if request.POST['password']!='':
                password = request.POST['password']
            else:
                messages.error(request, 'Password is Empty!')
                return redirect(request.META.get('HTTP_REFERER'))
            if AdminRegistration.objects.filter(email=email, login_block=False, is_verified=True, is_active=True).exists():
                admin = AdminRegistration.objects.get(email=email, login_block=False, is_verified=True, is_active=True)
                db_password = admin.password
                db_email = admin.email  
                db_role = admin.role  
                db_name = admin.name
                db_Contact = admin.phone
                user = authenticate(request, email=email, password=password)                
                if user is not None:
                    login(request, user)
                else:
                    messages.error(request, 'Credentials Not Match')
                    return redirect(request.META.get('HTTP_REFERER'))

                Token.objects.filter(user=admin).delete()
                token = Token.objects.create(user=admin)

                if token:
                    if request.user.is_authenticated:
                        AdminRegistration.objects.filter(email=email).update(is_login=True, token=token.key)
                        client_ip = get_client_ip(request)
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> LogIn Success With <span class="text-dark">[ {client_ip} ]</span> Ip. On<span>')
                        request.session['SUPERADMIN'] = db_email
                        request.session['ADMINUSERID'] = admin.pk
                        request.session['ADMIN-PASS'] = True
                        request.session['token'] = token.key
                        request.session['ADMIN-ROLE'] = db_role
                        try:
                            project = PROJECTInformation.objects.get(pk=1)
                        except Exception:
                            project=False

                        context = {
                            'fullname':db_name,
                            'data':datetime.datetime.now().strftime("%d %b, %Y - %a %I:%M %p"),
                            'email':db_email,
                            'mobileN':db_Contact,
                            'project':project,
                        } 
                        # ==================================================================================
                        CONFIG_SMTP_NO_REPLY()
                        # html_content = render_to_string("./template/email/adminLOGINSUCCESS.html", context)
                        # recipient_list = [email,]
                        # EmailThread(f'Hi [ { db_name } ] - Login Success | {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
                        # ==================================================================================
                        messages.success(request, 'Welcome Back! ' + ' - ' + db_name)
                        return redirect('DefaultDashboard')
                    else:
                        messages.error(request, 'Informations is Not Valid')
                        return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, 'Token Generate Error')
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Account Not Exist!')
                return redirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            messages.error(request, f'This Error: {e}')
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request,"./template/admin/adminLogin.html")
