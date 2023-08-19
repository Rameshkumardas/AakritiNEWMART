import datetime
from django.conf import settings
from Accounts.HELPERS import GENERATE_ONE_TIME_VERIFICATION_CODE

from django.http import JsonResponse
from django.shortcuts import redirect
from Accounts.models import shippingADDRESS
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from AdminAuthentication.Thread import EmailThread
from AdminAuthentication.models import AdminRegistration
from django.utils import timezone
from ExtraSettings.models import PROJECTInformation
from Message.models import MobileNewslatters, EmailNewslatters
from Accounts.HELPERS import GENERATEOTP, USER_ACCESS_GRANTED, SYSTEMGENERATEPASSWORD
from django.contrib.auth import authenticate, login, logout
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
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
valid_phone = '^\\+?[1-9][0-9]{7,14}$'
# ==============================================================================
# REQUEST FOR ONETIME VERIFICATION CODE 
# ==============================================================================
def GetOneTimeVerificationCode(request):
    userid = request.POST['userid']
    if userid == "":
        return JsonResponse({'status':0, 'message':'User Id Required*'})
    else:
        is_generated = GENERATE_ONE_TIME_VERIFICATION_CODE(request, userid)
        if is_generated:
            return JsonResponse({'status':1, 'message': 'Sent Verification Code'})
        else:
            return JsonResponse({'status':0, 'message': 'Email Not Valid'})
# ==============================================================================
# ONETIME VERIFICATION CODE
# ==============================================================================
def VerifyOneTimeVerificationCode(request):
    vCode = request.POST.get('vCode')
    if vCode == "" or vCode == None or vCode == "undefined":
        return JsonResponse({'status':0, 'message':'Verification Code Required*'})
    else:
        try:
            if(vCode == request.session['OneTimeVerificationCode']): 
                #AdminRegistration.objects.filter().exclude(is_accountant=True).delete()
                is_login = USER_ACCESS_GRANTED(request)
                if is_login:
                    AFTERLogin = f"{request.META.get('HTTP_REFERER')}"
                    return JsonResponse({'status':1, 'message': 'Login Success', 'AFTERLogin':f'{AFTERLogin}'})
                else:
                    return JsonResponse({'status':0, 'message':'Login Issue*'})
            else:
                return JsonResponse({'status':0, 'message': 'OTP Not Valid*'})
        except Exception as e:
            print("Verification Error", e)
            return JsonResponse({'status':0, 'message': 'Verification Error - {e}'})

# ==============================================================================
# UPDATE USER IMG SUSING AJAX METHOD 
# ==============================================================================
def updateIMG(request):
    if request.user.token == request.session['token']:
        img = request.FILES.get('img')
        if img == '' or img ==None:
            return JsonResponse({'status':0, 'message':'Image Required'})
        else:
            try:
                user = AdminRegistration.objects.get(pk=request.user.pk)
                user.img = img
                user.save()
                return JsonResponse({"status":1, "message":"IMG Updated", "AFTERTask":f"{request.META.get('HTTP_REFERER')}"})
            except Exception:
                return JsonResponse({'status':0, 'message':f'Error Occured'})
    else:
        return JsonResponse({'status':0, 'message':'You dont Have Permission'})
# ==============================================================================
# UPDATE USER INFORMATION SUSING AJAX METHOD 
# ==============================================================================
def updateINFORMATION(request):
    if request.user.token == request.session['token']:        
        if request.method == "POST":
            try:
                user = AdminRegistration.objects.get(pk=request.user.pk)
                fname = request.POST.get('fname')
                if fname:
                    user.fname = fname
                    user.save()
                
                lname = request.POST.get('lname')
                if lname:
                    user.lname = lname
                    user.save()
                    
                contact = request.POST.get('contact')
                if contact:
                    user.phone = contact
                    user.save()
                    
                gender = request.POST.get('gender')
                if gender:
                    user.gender = gender
                    user.save()
                    
                return JsonResponse({"status":1, "message":" Update Successfully", "AFTERTask":f"{request.META.get('HTTP_REFERER')}"})
            except Exception as e:
                print(e)
                return JsonResponse({'status':0, 'message':f'{e}Error Occured'})   
        else:
            return JsonResponse({'status':0, 'message':'Not Valid Request'})
    else:
        return JsonResponse({'status':0, 'message':'You dont Have Permission'})
# ==============================================================================
# UPDATE PASSWORD USING AJAX METHOD 
# ==============================================================================
def updatePASSWORD(request):
    if request.user.token == request.session['token']:        
        if request.method == "POST":
            try:
                updateOBJ = AdminRegistration.objects.get(pk=request.user.pk)
                old_password = request.POST.get('old_password')
                password = request.POST.get('password')
                repassword = request.POST.get('repassword')
                if old_password and old_password !='new':
                    user = authenticate(request, email=request.user.email, password=old_password)
                    if user is not None:
                        if password == repassword:                            
                            updateOBJ.password = make_password(password)
                            updateOBJ.save()
                            return JsonResponse({"status":1, "message":f"Password Updated", "AFTERTask":f"{request.META.get('HTTP_REFERER')}"})   
                        else:
                            return JsonResponse({'status':0, 'message':f'Password Not Match'})   
                    else:
                        return JsonResponse({"status":0, "message":f"Informations is Not Valid"})   
                else:
                    if password == repassword:                            
                        updateOBJ.password = make_password(password)
                        updateOBJ.save()
                        return JsonResponse({"status":1, "message":f"Password Updated", "AFTERTask":f"{request.META.get('HTTP_REFERER')}"})   
                    else:
                        return JsonResponse({"status":0, "message":f"Password Not Match"})   
          
            except Exception as e:
                print(e)
                return JsonResponse({"status":0, "message":f"{e}Error Occured"})   
        else:
            return JsonResponse({"status":0, "message":"Not Valid Request"})
    else:
        return JsonResponse({"status":0, "message":"You dont Have Permission"})
# ==============================================================================
# USER LOGIN AJAX METHOD 
# ==============================================================================
def USERLOGINRequest(request):
    userid = request.POST['userid']
    userpassword = request.POST['password']
    email = re.compile(valid_email)
    phone = re.compile(valid_phone)
    if userid == "":
        return JsonResponse({'status':0, 'message':'Email Id Required*'})
    elif userpassword == "":
        return JsonResponse({'status':0, 'message':'Password Required*'})
    else:        
        if(re.search(email, userid)):
            try:
                # .exclude(is_accountant=True)
                if AdminRegistration.objects.filter(email=userid).exists():
                    try:
                        admin = AdminRegistration.objects.get(email=userid, login_block=False, is_verified=True, is_active=True)
                        user = authenticate(request, email=userid, password=userpassword)                    
                        if user is not None:

                            Token.objects.filter(user=admin).delete()
                            token = Token.objects.create(user=admin)
                            login(request, user)

                            if request.user.is_authenticated:
                                # try:
                                #     access = SUBSCRIBEDUSERList.objects.get(user=user)
                                #     if timezone.now() > access.expire_date:
                                #         AdminRegistration.objects.filter(email=userid).exclude(is_accountant=True).update(is_access=False, is_access_days=0, is_login=True, token=token.key)
                                # except (SUBSCRIBEDUSERList.DoesNotExist):
                                #     AdminRegistration.objects.filter(email=userid).update(is_access=False, is_access_days=0, is_login=True, token=token.key)
                        
                                AdminRegistration.objects.filter(email=userid).exclude(is_accountant=True).update(is_login=True, token=token.key)
                                request.session['AakritiMARTusername'] = userid
                                request.session['AakritiMARTpassword'] = True
                                request.session['AakritiMARTUser'] = admin.pk
                                request.session['AakritiMARTrole'] = 'user'
                                request.session['token'] = token.key
                                project = PROJECTInformation.objects.last()
                                AFTERLogin = f"{request.META.get('HTTP_REFERER')}"
                                return JsonResponse({'status':1, 'message': 'Login Success', 'AFTERLogin':f'{AFTERLogin}'})
                            else:
                                return JsonResponse({'status':0, 'message': 'Error Occured'})
                        else:
                            return JsonResponse({'status':0, 'message': 'Credentials Not Match'})
                    except Exception as e:
                        return JsonResponse({'status':0, 'message': f'Please Activate Your Account From Email.'})
                else:
                    return JsonResponse({'status':0, 'message': 'Account Not Exists.'})
            except Exception as e:
                return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
        # elif(re.search(phone, userid)):  
        #     try:
        #         user = AdminRegistration.objects.get(mobileN=userid)
        #         if pbkdf2_sha256.verify(userpassword, user.password):
        #             AdminRegistration.objects.filter(username=username).update( is_login=True)
        #             request.session['AakritiMARTusername'] = userid
        #             request.session['AakritiMARTpassword'] = True
        #             request.session['AakritiMARTUser'] = user.pk
        #             request.session['AakritiMARTrole'] = 'user'
                    # Project = PROJECTInformation.objects.last()
                    # AFTERLogin = f"{Project.baseURL}STUDENTDASHBOARD/{userid}/"
        #             return JsonResponse({'status':1, 'message':'Login Success', 'AFTERLogin':f'{AFTERLogin}'})
        #         else:
        #             return JsonResponse({'status':0, 'message': 'Error Occured'})                 
        #     except Exception:
        #         return JsonResponse({'status':0, 'message': f'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'Email Not Valid'})
              
            # try:
                
            #     user = AdminRegistration.objects.get(email=userid)
            #     user = authenticate(request, email=email, password=userpassword)
            #     if user is not None:
            #         login(request, user)
            #     else:
            #         messages.error(request, 'Credentials Not Match')
            #         return redirect(request.META.get('HTTP_REFERER'))
            #     if request.user.is_authenticated:
            #         AdminRegistration.objects.filter(email=userid).update( is_login=True)
            #         request.session['AakritiMARTusername'] = userid
            #         request.session['AakritiMARTpassword'] = True
            #         request.session['AakritiMARTrole'] = 'user'
            #         request.session['AakritiMARTUser'] = user.pk
            #         Project = PROJECTInformation.objects.last()
            #         AFTERLogin = f"{Project.baseURL}STUDENTDASHBOARD/{userid}/"
            #         return JsonResponse({'status':1, 'message':'Login Success', 'AFTERLogin':f'{AFTERLogin}'})
            #     else:
            #         return JsonResponse({'status':0, 'message': 'Error Occured'})                    
            # except Exception:
            #     return JsonResponse({'status':0, 'message':'Error Occured'})   
# ==============================================================================
# SAVE & CHANGE PASSWORD USING AJAX REQUEST 
# ==============================================================================
def SaveAndChangePassword(request):
    if request.session.has_key('OneTimeVerificationCode'):
        email = request.POST.get('email')
        vCode = request.POST.get('vCode')
        userpassword = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')        
        if userpassword != confirmpassword:
            return JsonResponse({'status':0, 'message':'Password Not Match'})
        else:
            if(email==request.session['OneTimeVerificationUser'] and vCode == request.session['OneTimeVerificationCode']):
                try:
                    admin = AdminRegistration.objects.get(email=email)
                    admin.password = make_password(userpassword)
                    admin.save()
                    logout(request)
                    return JsonResponse({'status':1, 'message': 'Password Successfully Changed'})
                except Exception:
                    return JsonResponse({'status':0, 'message':'User Not Valid'})
            else:
                return JsonResponse({'status':0, 'message': 'Email Not Valid*'})
    else:
        return JsonResponse({'status':0, 'message':'Error Occured'})        
# ==============================================================================
# USER PASSWORD FORGOT AJAX REQUEST 
# ==============================================================================
def USERFORGOTRequest(request):
    userid = request.POST['userid']
    email = re.compile(valid_email)
    phone = re.compile(valid_phone)
    if userid == "":
        return JsonResponse({'status':0, 'message':'User Id Required*'})
    else:
        OneTimeVerificationCode = GENERATEOTP(request, userid)        
        if(re.search(email, userid)):
            try:
                user = AdminRegistration.objects.get(email=userid)
                project = PROJECTInformation.objects.last()
                context = {
                    'user':user,
                    'project':project,
                    'code':OneTimeVerificationCode,
                    'date': timezone.now(),
                }     
                CONFIG_SMTP_NO_REPLY()           
                html_content = render_to_string("./template/account/email/OneTimeVerificationCode.html", context)
                recipient_list = [userid,]
                EmailThread(f'OneTime Verification Code | {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                return JsonResponse({'status':1, 'message': 'Sent Verification Code'})
            except Exception as e:
                print(e)
                return JsonResponse({'status':0, 'message': 'Error Occured'})
        
        elif(re.search(phone, userid)):  
            try:
                user = AdminRegistration.objects.get(mobileN=userid)
                try:    
                    project = PROJECTInformation.objects.last()
                except Exception:
                    pass
                context = {
                    'user':user,
                    'project':project,
                    'date': timezone.now(),
                    'code':OneTimeVerificationCode,
                }
                CONFIG_SMTP_NO_REPLY() 
                html_content = render_to_string("./template/account/email/OneTimeVerificationCode.html", context)
                recipient_list = [user.email,]
                EmailThread(f'OneTime Verification Code || {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                
                return JsonResponse({'status':1, 'message': f'{settings.EMAIL_HOST_USER} Sent Verification Code'})
            except Exception:
                return JsonResponse({'status':0, 'message': f'Error Occured'})
        else:  
            try:
                username = userid.split('@')[0]
                user = AdminRegistration.objects.get(username=username)
                context = {
                    'code':OneTimeVerificationCode,
                }
                CONFIG_SMTP_NO_REPLY() 
                html_content = render_to_string("./template/account/email/OneTimeVerificationCode.html", context)
                recipient_list = [user.email,]
                EmailThread(f'OneTime Verification Code | {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                return JsonResponse({'status':1, 'message': 'Sent Verification Code'})
            except Exception:
                return JsonResponse({'status':0, 'message':'Error Occured'})      
# ==============================================================================
# USER PASSWORD FORGOT AJAX REQUEST 
# ==============================================================================
def USERVERIFYFORGOTRequest(request):
    vCode = request.POST['vCode']
    if vCode == request.session['OneTimeVerificationCode']:        
        userid = request.session['OneTimeVerificationUser']
        email = re.compile(valid_email)
        phone = re.compile(valid_phone)
        sys_password = SYSTEMGENERATEPASSWORD(request)
        if userid == "" or userid == None:
            return JsonResponse({'status':0, 'message':'User Id Required*'})
        else:        
            if(re.search(email, userid)):                
                try:
                    user = AdminRegistration.objects.get(email=userid)
                    user.password = make_password(sys_password)
                    user.save()
                    project = PROJECTInformation.objects.last()
                    context = {
                        'project':project,
                        'user':user,
                        'password':sys_password,                    
                        'date': timezone.now(),
                    }
                    CONFIG_SMTP_NO_REPLY() 
                    html_content = render_to_string("./template/account/email/ForgotPassword.html", context)
                    recipient_list = [user.email,]
                    EmailThread(f'Hi, {user.fname} Your - Password Updated || {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                    del request.session['OneTimeVerificationCode']
                    del request.session['OneTimeVerificationUser']
                    return JsonResponse({'status':1, 'message': f'{user.fname} - Password Updated'})
                except Exception as e:
                    print(e)
                    return JsonResponse({'status':0, 'message': 'Error Occured'})
            elif(re.search(phone, userid)):  
                try:
                    user = AdminRegistration.objects.get(mobileN=userid)
                    user.password = make_password(sys_password)
                    user.save()
                    context = {
                        'project':project,
                        'user':user,
                        'password':sys_password,                    
                        'date': timezone.now(),
                    }

                    html_content = render_to_string("./template/account/email/ForgotPassword.html", context)
                    recipient_list = [userid,]
                    EmailThread(f'{user.fname} - Password Updated | {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                    
                    del request.session['OneTimeVerificationCode']
                    del request.session['OneTimeVerificationUser']
                    return JsonResponse({'status':1, 'message': f'{user.fname} - Password Updated'})
                except Exception:
                    return JsonResponse({'status':0, 'message': 'Error Occured'})
            else:  
                try:
                    username = userid.split('@')[0]
                    user = AdminRegistration.objects.get(username=username)
                    user.password = make_password(sys_password)
                    user.save()
                    context = {
                        'project':project,
                        'user':user,
                        'password':sys_password,                    
                        'date': timezone.now(),
                    }
                    html_content = render_to_string("./template/account/email/ForgotPassword.html", context)
                    recipient_list = [userid,]
                    EmailThread(f'{user.fname} - Password Updated | {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                    del request.session['OneTimeVerificationCode']
                    del request.session['OneTimeVerificationUser']
                    return JsonResponse({'status':1, 'message': f'{user.fname} - Password Updated'})
                except Exception:
                    return JsonResponse({'status':0, 'message': 'Error Occured'})
    else: 
        return JsonResponse({'status':0, 'message':'OTP Not Valid**'})
# ==============================================================================
# CRUD OPERATION ON PRODUCT 
# ==============================================================================
def GetVerificationCode(request):     
    target = request.POST['target']
    email = re.compile(valid_email)
    phone = re.compile(valid_phone)
    if target == '':
        return JsonResponse({'status':0, 'message':'Input Field Required!'})
    else:        
        OneTimeVerificationCode = GENERATEOTP(request, target)
        if(re.search(email, target)):
            if EmailNewslatters.objects.filter(email=target).exists():
                pass
            else:
                EmailNewslatters.objects.create(email=target)
            try:    
                project = PROJECTInformation.objects.get(pk=1)
            except Exception:
                pass            
            context = {
                'code': OneTimeVerificationCode,
                'email':email,
                'PROJECT': project,
            }
            CONFIG_SMTP_NO_REPLY() 
            html_content = render_to_string("./template/account/email/OneTimeVerificationCode.html", context)
            recipient_list = [target,]
            EmailThread(f"OneTime Verification Code || {project.name}", settings.EMAIL_HOST_USER, html_content, recipient_list).start()   
            return JsonResponse({'status':1, 'message': f'Sent Verification Code'})
        elif(re.search(phone, target)):  
            if MobileNewslatters.objects.filter(number=target).exists():
                pass
            else:
                MobileNewslatters.objects.create(number=target)
            # requests.get(f"http://www.smsalert.co.in/api/push.json?apikey=62b2af4c1a5d7&route=transactional&sender=VOFREE&mobileno={target}&text=Thanks%20for%20choosing%20Voicefreedom%20{OneTimeVerificationCode}%20Click%20Here.")
            return JsonResponse({'status':1, 'message':'Sent Verification Code'})
        else:   
            return JsonResponse({'status':0, 'message': f'Sorry Youre Input Not Valid'})
# ==============================================================================
# CRUD OPERATION ON PRODUCT 
# ==============================================================================
def VerifyCode(request):     
    vCode = request.POST['vCode']
    email = re.compile(valid_email)
    phone = re.compile(valid_phone)
    if vCode == request.session['OneTimeVerificationCode']:
        request.session['AAKRITICMSusername'] = request.session['OneTimeVerificationUser']
        request.session['AAKRITICMSpassword'] = True
        request.session['AAKRITICMSrole'] = 'user'
        if AdminRegistration.objects.filter(email=request.session['OneTimeVerificationUser']).exists():
            request.session['AAKRITICMSUser'] = AdminRegistration.objects.get(email=request.session['OneTimeVerificationUser']).pk
            return JsonResponse({'status':1, 'message':'Login Success', 'home':f'{settings.HOME_PAGE}'})

        elif AdminRegistration.objects.filter(mobileN=request.session['OneTimeVerificationUser']).exists():
            request.session['AAKRITICMSUser'] = AdminRegistration.objects.get(mobileN=request.session['OneTimeVerificationUser']).pk

            return JsonResponse({'status':1, 'message':'Login Success', 'home':f'{settings.HOME_PAGE}'})
        
        elif AdminRegistration.objects.filter(username=request.session['OneTimeVerificationUser']).exists():
            request.session['AAKRITICMSUser'] = AdminRegistration.objects.get(username=request.session['OneTimeVerificationUser']).pk

            return JsonResponse({'status':1, 'message':'Login Success', 'home':f'{settings.HOME_PAGE}'})
        else:
            if(re.search(phone, request.session['OneTimeVerificationUser'])):  
                try:
                    password = request.session['OneTimeVerificationCode']
                    context = {
                        'code': request.session['OneTimeVerificationCode'],
                        'email':"No Email",
                        'username':"No Username",
                        'password':request.session['OneTimeVerificationCode'],
                    }
                    
                    AdminRegistration.objects.create(mobileN=request.session['OneTimeVerificationUser'], password=password)
                    user = AdminRegistration.objects.get(mobileN=request.session['OneTimeVerificationUser'])
                    request.session['AAKRITICMSUser'] = user.pk
                    return JsonResponse({'status':1, 'message':'Registered & Login Success', 'home':f'{settings.HOME_PAGE}'})
                except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'})
            elif(re.search(email, request.session['OneTimeVerificationUser'])):
                try:  
                    username = request.session['OneTimeVerificationUser'].split('@')[0]
                    password = request.session['OneTimeVerificationCode'],
                    context = {
                        'code': request.session['OneTimeVerificationCode'],
                        'email':request.session['OneTimeVerificationUser'],
                        'phone':"No mobileN",
                        'username':username,
                        'password':request.session['OneTimeVerificationCode'],
                    }
                    AdminRegistration.objects.create(email=request.session['OneTimeVerificationUser'],username=username, password=password)
                    user = AdminRegistration.objects.get(email=request.session['OneTimeVerificationUser'])
                    request.session['AAKRITICMSUser'] = user.pk
                    html_content = render_to_string("./template/account/email/UserSuccessfullyRegistered.html", context)
                    recipient_list = [request.session['OneTimeVerificationUser'],]
                    EmailThread(f'User Successfully Registered | {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
                    return JsonResponse({'status':1, 'message':'Registered & Login Success', 'home':f'{settings.HOME_PAGE}'})
                except Exception as e:
                    return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
            else:
                return JsonResponse({'status':0, 'message':'Error Occured'})
    else: 
        return JsonResponse({'status':0, 'message':'OTP Not Valid**'})
# ==============================================================================
# LOGOUT USER NOW 
# ==============================================================================
def LOGOUTUSER(request): 
    try:
        AdminRegistration.objects.filter(pk=request.user.pk).update(is_login=False, last_update=timezone.now())     
        logout(request)
        messages.success(request, 'LogOut Success')
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        logout(request)      
        messages.error(request, f'{e} Error Occured & LogOut Success')
        return redirect('/')
# ==============================================================================
# UPDATE BILLING ADDRESS
# ==============================================================================
def updateUSERPROFILE(request): 
    if request.session.has_key('AakritiMARTusername') and request.session.has_key('AakritiMARTpassword') and request.session.has_key('AakritiMARTUser'):
        target = request.POST.get('target')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        headline = request.POST.get('headline')
        intro = request.POST.get('intro')
        if target == "":
            return JsonResponse({'status':0, 'message':'Target Required*'})
        elif fname == "" and lname=="":
            return JsonResponse({'status':0, 'message':'Name Required*'})
        elif headline == "":
            return JsonResponse({'status':0, 'message':'Headline Required*'})
        elif intro == "":
            return JsonResponse({'status':0, 'message':'Intro Required*'})
        else: 
            try:
                if AdminRegistration.objects.filter(pk=target).exists():
                    AdminRegistration.objects.filter(pk=target).update(fname=fname, lname=lname, designation=headline, intro=intro)
                    return JsonResponse({'status':1, 'message':'Successfully Updated'})
                else:
                    return JsonResponse({'status':0, 'message':'Not Exists'})
            except Exception as e:
                return JsonResponse({'status':0, 'message': f'Error Occured'})
    else:
        return JsonResponse({'status':0, 'message': 'You Dont Have Access'})
# ==============================================================================
# ADD BILLING ADDRESS
# ==============================================================================
def BILLINGAddress(request):  
    target = request.POST.get('target')
    pincode = request.POST.get('pincode')
    houseno = request.POST.get('houseno')
    landmark = request.POST.get('landmark')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    more = request.POST.get('more')
    if target == "":
        return JsonResponse({'status':0, 'message':'Target Required*'})
    elif pincode == "":
        return JsonResponse({'status':0, 'message':'PinCode Required*'})
    elif city == "":
        return JsonResponse({'status':0, 'message':'City Required*'})
    elif state == "":
        return JsonResponse({'status':0, 'message':'State Required*'})
    else: 
        try:
            print(target)
            if billingADDRESS.objects.filter(user_id=request.user.pk, bcode = pincode, bhouse_no=houseno, blandmark=landmark, bcity=city, bstate=state, bcountry=country, more=more).exists():
                return JsonResponse({'status':0, 'message':'Alreday Exists'})
            else:
                billingADDRESS.objects.create(user_id=request.user.pk, bcode = pincode, bhouse_no=houseno, blandmark=landmark, bcity=city, bstate=state, bcountry=country, more=more)
                return JsonResponse({"status":1, "message":"Successfully Created", "AFTERTask":f"{request.META.get('HTTP_REFERER')}"})
        except Exception as e:
            return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
# ==============================================================================
# UPDATE BILLING ADDRESS
# ==============================================================================
def updateBILLINGAddress(request):  
    target = request.POST.get('target')
    pincode = request.POST.get('pincode')
    houseno = request.POST.get('houseno')
    landmark = request.POST.get('landmark')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    more = request.POST.get('more')
    if target == "":
        return JsonResponse({'status':0, 'message':'Target Required*'})
    elif pincode == "":
        return JsonResponse({'status':0, 'message':'PinCode Required*'})
    elif city == "":
        return JsonResponse({'status':0, 'message':'City Required*'})
    elif state == "":
        return JsonResponse({'status':0, 'message':'State Required*'})
    else: 
        try:
            if billingADDRESS.objects.filter(pk=target).exists():
                billingADDRESS.objects.filter(pk=target).update(bcode = pincode, bhouse_no=houseno, blandmark=landmark, bcity=city, bstate=state, bcountry=country, more=more)
                return JsonResponse({'status':1, 'message':'Successfully Updated'})
            else:
                return JsonResponse({'status':0, 'message':'Not Exists'})
        except Exception as e:
            return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
# ==============================================================================
# ADD BILLING ADDRESS
# ==============================================================================
def deleteBILLINGAddress(request, pk):  
    if pk == "":
        messages.success(request, 'Target Required*')
        return redirect(request.META.get('HTTP_REFERER'))
    else: 
        try:
            if billingADDRESS.objects.filter(pk=pk).exists():
                billingADDRESS.objects.filter(pk=pk).delete()
                messages.success(request, 'Successfully Deleted')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Not Exists')
                return redirect(request.META.get('HTTP_REFERER'))
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META.get('HTTP_REFERER'))       
# ==============================================================================
# ADD SHIPPING ADDRESS
# ==============================================================================
def SHIPPINGAddress(request):  
    target = request.POST.get('target')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    emailId = request.POST.get('emailId')
    contactNo = request.POST.get('contactNo')

    pincode = request.POST.get('pincode')
    houseno = request.POST.get('houseno')
    landmark = request.POST.get('landmark')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    more = request.POST.get('more')

    if target == "":
        return JsonResponse({'status':0, 'message':'Target Required*'})
    elif pincode == "":
        return JsonResponse({'status':0, 'message':'PinCode Required*'})
    elif city == "":
        return JsonResponse({'status':0, 'message':'City Required*'})
    elif state == "":
        return JsonResponse({'status':0, 'message':'State Required*'})
    else: 
        try:
            if shippingADDRESS.objects.filter(user_id=request.user.pk, fname=fname, lname=lname, email=emailId, contact=contactNo, code = pincode, house_no=houseno, landmark=landmark, city=city, state=state, country=country).exists():
                return JsonResponse({'status':0, 'message':'Alreday Exists'})
            else:
                shippingADDRESS.objects.create(user_id=request.user.pk, fname=fname, lname=lname, email=emailId, contact=contactNo, code = pincode, house_no=houseno, landmark=landmark, city=city, state=state, country=country)
                AFTERTask = request.META.get('HTTP_REFERER')
                return JsonResponse({'status':1, 'message':'Successfully Created', 'AFTERTask':AFTERTask})
        except Exception:
            return JsonResponse({'status':0, 'message':'Error Occured'})
# ==============================================================================
# UPDATE SHIPPING ADDRESS
# ==============================================================================
def updateSHIPPINGAddress(request):  
    target = request.POST.get('target')
    pincode = request.POST.get('pincode')
    houseno = request.POST.get('houseno')
    landmark = request.POST.get('landmark')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    more = request.POST.get('more')
    if target == "":
        return JsonResponse({'status':0, 'message':'Target Required*'})
    elif pincode == "":
        return JsonResponse({'status':0, 'message':'PinCode Required*'})
    elif city == "":
        return JsonResponse({'status':0, 'message':'City Required*'})
    elif state == "":
        return JsonResponse({'status':0, 'message':'State Required*'})
    else: 
        try:
            if shippingADDRESS.objects.filter(pk=target).exists():
                shippingADDRESS.objects.filter(pk=target).update(scode = pincode, shouse_no=houseno, slandmark=landmark, scity=city, sstate=state, scountry=country, more=more)
                return JsonResponse({'status':1, 'message':'Successfully Updated'})
            else:
                return JsonResponse({'status':0, 'message':'Not Exists'})
        except Exception as e:
            return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
# ==============================================================================
# ADD SHIPPING ADDRESS
# ==============================================================================
def deleteSHIPPINGAddress(request, pk):  
    if pk == "":
        messages.success(request, 'Target Required*')
        return redirect(request.META.get('HTTP_REFERER'))
    else: 
        try:
            if shippingADDRESS.objects.filter(pk=pk).exists():
                shippingADDRESS.objects.filter(pk=pk).delete()
                messages.success(request, 'Successfully Deleted')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Not Exists')
                return redirect(request.META.get('HTTP_REFERER'))
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# MORE SETTINGS
# ============================================================================== 

