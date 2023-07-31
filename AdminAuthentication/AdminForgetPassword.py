from django.http import Http404
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from AdminAuthentication.models import AdminRegistration
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
from AdminAuthentication.Thread import EmailThread
from ExtraSettings.models import PROJECTInformation
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
import random
import array
import re 
# Create your views here.gaierror
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
password_validator = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
def AdminForgetPassword(request):
    if request.session.has_key('AdminVerificationCode'):
        try:
            if request.method=="POST":
                if request.POST['email']!='':
                    if(re.search(valid_email,request.POST['email'])):   
                        AdminEmail = request.POST['email']
                    else:   
                        messages.error(request, 'Email is Not Valid!')
                        return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, 'Email Id is Empty!')
                    return redirect(request.META.get('HTTP_REFERER'))
 
                if AdminRegistration.objects.filter(email=AdminEmail, login_block=False, is_verified=True, is_active=True).exists():
                    
                    request.session['ForgetAdminVerificationCode'] = 'eMART'+''.join((random.choice('!@#$%^&*()0') for i in range(10)))+'SHOP'
                    
                    MAX_LEN = 20
                    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
                    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
                    rand_digit = random.choice(DIGITS)
                    rand_upper = random.choice(UPCASE_CHARACTERS)
                    rand_lower = random.choice(LOCASE_CHARACTERS)
                    rand_symbol = random.choice(SYMBOLS)

                    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

                    for x in range(MAX_LEN - 4):
                        temp_pass = temp_pass + random.choice(COMBINED_LIST)
                        temp_pass_list = array.array('u', temp_pass)
                        random.shuffle(temp_pass_list)

                    password = ""
                    for x in temp_pass_list:
                        password = password + x
                            
                    print(password)
                    new_pass = make_password(password)
                    admin = AdminRegistration.objects.get(email=AdminEmail, login_block=False, is_verified=True, is_active=True, is_accountant=True)
                    try:
                        project = PROJECTInformation.objects.get(pk=1)
                    except Exception:
                        pass
                    context = {
                        'DigitCode': request.session['ForgetAdminVerificationCode'],
                        'user':admin,
                        'date': timezone.now(),
                        'PROJECT':project,
                    }   
                    CONFIG_SMTP_NO_REPLY()

                    html_content = render_to_string("./template/email/adminPasswordForgetEmail.html", context)
                    recipient_list = [AdminEmail, ]
                    EmailThread(f'Hi [ {admin.name} ] - Your Password Updated || {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                    
                    # html_content = render_to_string("./template/email/adminPasswordForgetEmail.html", context)
                    # recipient_list = [AdminEmail, ]                                    
                    # EmailThread(f'Hi [ {admin.name} ] - Your Password Updated || {project.name} ', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
                    
                    AdminRegistration.objects.filter(email = AdminEmail).update(password=new_pass)
                    messages.success(request, 'Updated Password Sent on Email')
                    return redirect('AdminLogin')
                else:
                    raise Http404
        except Exception:
            raise Http404
    else:
        raise Http404
    
    return render(request,"./template/admin/adminForgetPassword.html")





