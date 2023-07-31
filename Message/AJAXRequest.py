from Accounts.HELPERS import GENERATE_ONE_TIME_VERIFICATION_CODE
from ExtraSettings.models import PROJECTInformation
from Message.models import MobileNewslatters, EmailNewslatters
from AdminAuthentication.HELPER import CONFIG_SMTP_SUPPORT
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from AdminAuthentication.Thread import EmailThread
from Message.models import ContactUS, Feedback
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from decouple import config
import requests
import json
import re
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
valid_phone = '^\\+?[1-9][0-9]{7,14}$'
# ==============================================================================
# CONTACT US LIST
# ==============================================================================
def GENERATE_CONTACT_REQUEST(request):
    jsonOBJ = request.POST.get('jsonOBJ')
    obj = json.loads(jsonOBJ)
    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):        
        is_generated = GENERATE_ONE_TIME_VERIFICATION_CODE(request, obj['email'])
        if is_generated:
            return JsonResponse({'status':1, 'message': 'Sent Verification Code'})
        else:
            return JsonResponse({'status':0, 'message': 'Email Not Valid'})  
    else:
        is_generated = GENERATE_ONE_TIME_VERIFICATION_CODE(request, obj['email'])
        if is_generated:
            return JsonResponse({'status':1, 'message': 'Sent Verification Code'})
        else:
            return JsonResponse({'status':0, 'message': 'Email Not Valid'})
# ==============================================================================
def SAVE_CONTACT_US_REQUEST_SEND_EMAIL(request):
    if request.method == 'POST':
        vCode = request.POST.get('get_otp_for_verify_contact_us')   
        if vCode == request.session['OneTimeVerificationCode']:
            jsonOBJ = request.POST.get('jsonOBJ')   
            obj = json.loads(jsonOBJ)
            if obj['fname'] == '' or obj['lname'] == None:
                return JsonResponse({'status':0, 'message': 'First Name Required'})
            elif obj['email'] == '' or obj['email'] == None:
                return JsonResponse({'status':0, 'message': 'Email Required'})
            elif obj['contact'] == '' or obj['contact'] == None:
                return JsonResponse({'status':0, 'message': 'Contact No Required'})
            elif obj['subject'] == '' or obj['subject'] == None:
                return JsonResponse({'status':0, 'message': 'Subject is Required'})
            elif obj['message'] == '' or obj['message'] == None:
                return JsonResponse({'status':0, 'message': 'Message is Required'})
            else:
                try:
                    if ContactUS.objects.filter(email=obj['email'], subject=obj['subject'], is_received=False).exists():
                        return JsonResponse({'status':0, 'message': 'Query Already Exists'})
                    else:
                        ContactUS.objects.create(firstname=obj['fname'], lastname=obj['lname'], email=obj['email'], phone=obj['contact'],  subject=obj['subject'], message=obj['message'])
                        CONFIG_SMTP_SUPPORT()
                        context = {
                            'obj':obj,
                            'project':PROJECTInformation.objects.last(),
                        }
                        html_content = render_to_string("./template/email/ContactRequest.html", context)
                        recipient_list = ['support@aakriticms.com', 'aakriticms@gmail.com', ]
                        EmailThread(f'[ {config("PROJECT_NAME")} ] New Contact Request ', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
                        return JsonResponse({'status':1, 'message': f'Thnaks For Contact Us'})
                except Exception as e:
                    return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
        else:
            return JsonResponse({'status':0, 'message': f'OTP Not Valid'})
    else:
        return JsonResponse({'status':0, 'message': f'Bad Request'})
# ==============================================================================
# SUBSCRIBE NEWSLETTERS
# ==============================================================================
def SUBSCRIBE_NEWSLETTER(request):
    target = request.POST['target']
    compile_email = re.compile(valid_email)
    compile_phone = re.compile(valid_phone)    
    if target == '' or target == None :
        messages.error(request, "Input Field Required!")
        return JsonResponse({'status':0, 'message':'Input Field Required!'})
    else:
        if(re.search(compile_email, target)):
            if(EmailNewslatters.objects.filter(email=target).exists()):
                return JsonResponse({'status':0, 'message': f'Already Exists'})
            else:
                EmailNewslatters.objects.create(email=target)
                return JsonResponse({'status':1, 'message': f'Successfully Subscribed'})
        elif(re.search(compile_phone, target)):   
            if(MobileNewslatters.objects.filter(number=target).exists()):
                return JsonResponse({'status':0, 'message': f'Already Exists'})
            else:
                MobileNewslatters.objects.create(number=target)
                return JsonResponse({'status':1, 'message': f'Successfully Subscribed'})
        else:   
            return JsonResponse({'status':0, 'message': f'Sorry You Input Not Valid'})
