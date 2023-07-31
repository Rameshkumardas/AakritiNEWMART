import json
from django.contrib.auth import logout
import array
import random
import datetime
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from Accounts.models import billingADDRESS, shippingADDRESS
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from AdminAuthentication.Thread import EmailThread
from AdminAuthentication.models import AdminRegistration
from django.utils import timezone
from django.contrib.auth import login, logout
from AdminAuthentication.models import AdminRegistration
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from decouple import config
import re
from Accounts.backends import  LoginWithEmailBackend
from BULKEMAILManager.models import EMAILList
from ExtraSettings.models import PROJECTInformation
from Message.models import EmailNewslatters, MobileNewslatters

valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
valid_phone = '^\\+?[1-9][0-9]{7,14}$'

compiled_email = re.compile(valid_email)
compiled_phone = re.compile(valid_phone)

def GENERATEOTP(request, UserId=None):  
    # del request.session["OneTimeVerificationEmail"]
    # del request.session["OneTimeVerificationCode"]
    
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    COMBINED_LIST = DIGITS 
    rand_digit = random.choice(DIGITS)
    temp_pass = rand_digit 
    for x in range(5):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
        
    vCode = ""
    for x in temp_pass_list:
            vCode = vCode + x
            
    print(UserId)
    print(vCode)
    request.session['OneTimeVerificationEmail'] = UserId
    request.session['OneTimeVerificationCode'] = vCode
    return request.session['OneTimeVerificationCode']
 
def SYSTEMGENERATEPASSWORD(request):
    MAX_LEN = 14
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
    return password

def GENERATE_ONE_TIME_VERIFICATION_CODE(request, userid):
    OneTimeVerificationCode = GENERATEOTP(request, userid) 
    if(re.search(compiled_email, userid)):
        try:                
            user = AdminRegistration.objects.get(email=userid)  
 
        except Exception:
            user = AdminRegistration.objects.create(fname="Gust", lname="User", email=request.session['OneTimeVerificationEmail'], login_block=False)
            EMAILList.objects.create(author_id=user.pk, email=request.session['OneTimeVerificationEmail'])   


        context = {
                'user':user,
                'project':PROJECTInformation.objects.last(),
                'code':OneTimeVerificationCode,
            }
        CONFIG_SMTP_NO_REPLY()
        # requests.get(f"http://www.smsalert.co.in/api/push.json?apikey=62b2af4c1a5d7&route=transactional&sender=VOFREE&mobileno={user.mobileN}&text=Thanks%20for%20choosing%20Voicefreedom%20{OneTimeVerificationCode}%20Click%20Here.")
        html_content = render_to_string("./template/account/email/OneTimeVerificationCode.html", context)
        recipient_list = [userid, ]
        EmailThread(f'OneTime Verification Code || {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
        return True
    else:
        return False
        
        
def USER_ACCESS_GRANTED(request):
    try:
        # request.session['OneTimeVerificationEmail']
        user = AdminRegistration.objects.get(email=request.session['OneTimeVerificationEmail'])
        LoginWithEmail = LoginWithEmailBackend.authenticate(request, request.session['OneTimeVerificationEmail'], user.password)
        print("LoginWithEmail", LoginWithEmail)
        if user is not None:
            logout(request)
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            login(request, user, backend='Accounts.backends.LoginWithEmailBackend')
            if request.user.is_authenticated:
                AdminRegistration.objects.filter(email=user.email).update(is_verified=True, is_active=True, is_login=True, token=token.key)
                request.session['AakritiMARTusername'] = user.email
                request.session['AakritiMARTpassword'] = True
                request.session['AakritiMARTuser'] = user.pk
                request.session['AakritiMARTrole'] = 'user'
                request.session['token'] = token.key
                print(f"Welcome [ {user.fname} ] Login Success")
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print("USER_ACCESS_GRANTED_ERROR ==============>", e)
        return False
    
    