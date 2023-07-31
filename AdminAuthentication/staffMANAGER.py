from AdminAuthentication.Thread import EmailThread
from AdminAuthentication.decorators import superadmin_required
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from AdminAuthentication.models import AdminRegistration
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
from ExtraSettings.models import PROJECTInformation
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from django.contrib import messages
from django.conf import settings
import random
import array
import re 
# Create your views here.
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
password_validator = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
# =============================================================================
# STAFF LIST
# =============================================================================
@superadmin_required
def AllStaffs(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            Admins = AdminRegistration.objects.filter(is_accountant=True).order_by('-id')
            if request.method=="POST":
                try:
                    if request.POST['Referance']!='':
                        ref_email = request.POST['Referance']
                        if AdminRegistration.objects.filter(is_active=True, is_verified=True, email=ref_email, is_superadmin=True, is_reference=False).exists():
                            if request.POST['name']!='':
                                name = request.POST['name']
                            else:
                                messages.error(request, 'Admin Name Required*')
                                return redirect(request.META.get('HTTP_REFERER'))
                        
                            if request.POST['role']!='':
                                role = request.POST['role']
                            else:
                                messages.error(request, 'Admin Role Required*')
                                return redirect(request.META.get('HTTP_REFERER'))

                            if request.POST['phone']!='':
                                phone = request.POST['phone']
                            else:
                                messages.error(request, 'Phone Number Required*')
                                return redirect(request.META.get('HTTP_REFERER'))
                        
                            if request.FILES.get('img')!='':
                                img = request.FILES.get('img')
                            else:
                                img=False
                                messages.error(request, 'IMG Required*')
                                return redirect(request.META.get('HTTP_REFERER'))
                        
                            if request.POST['email']!='':
                                if(re.search(valid_email, request.POST['email'])):   
                                    email = request.POST['email']
                                    AdminEmail = request.POST['email']
                                    username = email.split('@')[0]
                                else:
                                    messages.error(request, 'Email is Not Valid')
                                    return redirect(request.META.get('HTTP_REFERER'))
                            else:
                                messages.error(request, 'Email Required*')
                                return redirect(request.META.get('HTTP_REFERER'))

                            if request.POST['password']!='':
                                match_re = re.compile(password_validator)
                                if(re.search(match_re, request.POST['password'])):   
                                    password = request.POST['password']
                                else:
                                    messages.error(request, 'Password is Not Valid')
                                    return redirect(request.META.get('HTTP_REFERER'))
                            else:
                                messages.error(request, 'Password Required*')
                                return redirect(request.META.get('HTTP_REFERER'))

                            if AdminRegistration.objects.filter(email=AdminEmail).exists():
                                messages.error(request, f'{email} Has Already Account Exist')
                                return redirect(request.META.get('HTTP_REFERER'))
                            else:
                                if(role == 'is_admin'):
                                    admin = AdminRegistration.objects.create_reference_staff(name=name, username=username, email=email, phone=phone, password=password, img=img)
                                    admin.reference = ref_email
                                    admin.save()
                                if(role == 'is_superadmin'):
                                    admin = AdminRegistration.objects.create_superuser(name=name, username=username, email=email, phone=phone, password=password, img=img)
                                    admin.is_reference = True
                                    admin.reference = ref_email
                                    admin.save()

                                if(role == 'is_manager'):
                                    admin = AdminRegistration.objects.create_reference_manager(name=name, username=username, email=email, phone=phone, password=password, img=img)
                                    admin.reference = ref_email
                                    admin.save()
                                if(role == 'is_accountant'):
                                    admin = AdminRegistration.objects.create_reference_accountant(name=name, username=username, email=email, phone=phone, password=password, img=img)
                                    admin.reference = ref_email
                                    admin.save()
                                context = {
                                    'password': password,
                                    }
                                
                                # ==================================================================================
                                CONFIG_SMTP_NO_REPLY()
                                # html_content = render_to_string("./template/staff/email/Create.Staff.email.template.html", context)
                                # recipient_list = [email, 'das82916@gmail.com', 'javascript7322@gmail.com',]
                                # EmailThread(f'Hi [ { namme } ] - Create Successfully | {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
                                # ==================================================================================

                                messages.success(request, 'Staff Successfully Created! - Password Sent on Your Mail')
                                return redirect(request.META.get('HTTP_REFERER'))
                        else:
                            messages.error(request, 'Admin Referance Not Valid')
                            return redirect(request.META.get('HTTP_REFERER'))

                    else:
                        messages.error(request, 'Admin Referance Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            return render(request,"./template/staff/allStaffs.html", {'staff': 'menu-open', 'allStaffs': 'active', 'Admins':Admins})
        else:
            messages.error(request, f'You dont have permission to Change.')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Permission')
        return redirect("AdminLogOut")
# =============================================================================
# UPDATE STAFF ACCOUNT ACCESS
# =============================================================================
@superadmin_required
def UpdateStaffAccount(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            Staff = AdminRegistration.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    ref_email = request.POST.get('Referance')
                    if ref_email:
                        ref_email = ref_email
                        is_reference = True
                    else: 
                        is_reference = False
                        ref_email = ''

                    if request.POST['name']!='':
                        name = request.POST['name']
                    else:
                        messages.error(request, 'Admin Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                
                    if request.POST['role']!='':
                        role = request.POST['role']
                    else:
                        messages.error(request, 'Admin Role Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    if request.POST['phone']!='':
                        phone = request.POST['phone']
                    else:
                        messages.error(request, 'Phone Number Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    img = request.FILES.get('img')
                    if img:
                        img = img
                    else:
                        img=Staff.img
                   
                    if request.POST['email']!='':
                        if(re.search(valid_email, request.POST['email'])):   
                            email = request.POST['email']
                            username = email.split('@')[0]
                        else:
                            messages.error(request, 'Email is Not Valid')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, 'Email Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    pass_change_req = request.POST.get('password')
                    if pass_change_req:
                        match_re = re.compile(password_validator)
                        if(re.search(match_re, pass_change_req)):   
                            new_password = pass_change_req
                            password = make_password(new_password)
                        else:
                            messages.error(request, 'Password is Not Valid')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        password = Staff.password

                    try:
                        project = PROJECTInformation.objects.last()
                        context = {
                            'password': new_password,
                            'admin':Staff,
                        }
                        if(role == 'is_superadmin'):
                            AdminRegistration.objects.filter(email=email).update(name=name, username=username, email=email, phone=phone, password=password, img=img, is_superadmin=True, is_admin=True, is_manager=True, is_accountant=True, is_reference=is_reference,reference=ref_email)

                        elif(role == 'is_admin'):
                            AdminRegistration.objects.filter(email=email).update(name=name, username=username, email=email, phone=phone, password=password, img=img, is_superadmin=False, is_admin=True, is_manager=True, is_accountant=True, is_reference=is_reference,reference=ref_email)

                        elif(role == 'is_manager'):
                            AdminRegistration.objects.filter(email=email).update(name=name, username=username, email=email, phone=phone, password=password, img=img, is_superadmin=False, is_admin=False, is_manager=True, is_accountant=True, is_reference=is_reference,reference=ref_email)
                        elif(role == 'is_accountant'):
                            AdminRegistration.objects.filter(email=email).update(name=name, username=username, email=email, phone=phone, password=password, img=img, is_superadmin=False, is_admin=False, is_manager=False, is_accountant=True, is_reference=is_reference,reference=ref_email)
                        # ==================================================================================
                        CONFIG_SMTP_NO_REPLY()
                        html_content = render_to_string("./template/staff/email/Update.Staff.email.template.html", context)
                        recipient_list = [email, ]
                        EmailThread(f'Hi [ { name } ] - Account Updated || {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
                        # ==================================================================================
                        messages.success(request, 'Staff Successfully Updated! - Password Sent on Your Mail')
                        return redirect(request.META.get('HTTP_REFERER'))

                    except Exception as e:
                        messages.error(request, f'{e} Error Occured')
                        return redirect(request.META.get('HTTP_REFERER'))

                except Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))

            context = {
                'staff': 'menu-open', 
                'allStaffs': 'active', 
                'admin': Staff
            }
            return render(request, './template/staff/updateAdminProfile.html', context)

    else:
        messages.error(request, 'Please Login First')
        return redirect('AdminLogOut')
# =============================================================================
# ACTIVBATE ADMIN STAFF
# =============================================================================
@superadmin_required
def activateAdmin(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                AdminRegistration.objects.filter(pk=pk).update(is_active=True, is_verified=True, login_block=False)
                messages.success(request, 'Activate Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            pass
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# =============================================================================
# MORE FUNCTION AND CLASSES
# =============================================================================
# =============================================================================
# DEACTIVATE ADMIN STAFF
# =============================================================================
@superadmin_required
def deactivateAdmin(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                AdminRegistration.objects.filter(pk=pk).update(is_active=False, is_verified=False, login_block=True)
                messages.success(request, 'Deactivate Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            pass
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# =============================================================================
# DELETE ADMIN STAFF
# =============================================================================
@superadmin_required
def DeleteAdmin(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                Admin = AdminRegistration.objects.get(pk=pk)
                Admin.delete()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META.get('HTTP_REFERER')) 
            except Exception as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            pass
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')


