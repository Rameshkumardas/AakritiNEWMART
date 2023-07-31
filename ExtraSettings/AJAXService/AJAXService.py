from AdminAuthentication.decorators import superadmin_required
from django.http import JsonResponse
from django.conf import settings
import os

from ExtraSettings.models import PROJECTInformation
# ==============================================================================
# CREATE AND UPDATE  PROJECT CONTENTS SETTINGS
# ==============================================================================
@superadmin_required
def UpdateDetails(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.POST['Terms_Condition']!='':
                description = request.POST['Terms_Condition']
                target = request.POST['target']
            else:
                return JsonResponse({'status':1, 'message':'Details Data Empty'}) 
            try:
                if (target == 'terms'):
                    try:
                        add = TermCondition.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'Terms Successfully Updated'})
                    except TermCondition.DoesNotExist:
                        TermCondition.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Terms Successfully Created'})

                elif (target == 'privacy-policy'):
                    try:
                        add = PrivacyPolicy.objects.get(pk=1)
                        add.description=description
                        add.save()
                        
                        return JsonResponse({'status':1, 'message':'Privacy Policy Successfully Updated'})
                    except PrivacyPolicy.DoesNotExist:
                        PrivacyPolicy.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Privacy Policy Successfully Created'})

                elif (target == 'CopyrightPolicy'):
                    try:
                        add = CopyrightPolicy.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'Copyright Policy Successfully Updated'})
                    except CopyrightPolicy.DoesNotExist:
                        CopyrightPolicy.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Copyright Policy Successfully Created'})

                elif (target == 'aboutus'):
                    try:
                        add = AboutUS.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'About Us Successfully Updated'})
                    except AboutUS.DoesNotExist:
                        AboutUS.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'About Us Successfully Created'})

                elif (target == 'HowitWorks'):
                    try:
                        add = HowitWorks.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'How it Works Successfully Updated'})
                    except HowitWorks.DoesNotExist:
                        HowitWorks.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'How it Works Successfully Created'})

                elif (target == 'Security'):
                    try:
                        add = Security.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'Security Successfully Updated'})
                    except Security.DoesNotExist:
                        Security.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Security Successfully Created'})
                    
                elif (target == 'Disclaimer'):
                    try:
                        add = Disclaimer.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'Disclaimer Successfully Updated'})
                    except Disclaimer.DoesNotExist:
                        Disclaimer.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Disclaimer Successfully Created'})

                elif (target == 'RCRPolicy'):
                    try:
                        add = RCRPolicy.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'RCRPolicy Successfully Updated'})
                    except RCRPolicy.DoesNotExist:
                        RCRPolicy.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'RCRPolicy Successfully Created'})

                elif (target == 'CookiesPolicy'):
                    try:
                        add = CookiesPolicy.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'CookiesPolicy Successfully Updated'})
                    except CookiesPolicy.DoesNotExist:
                        CookiesPolicy.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'CookiesPolicy Successfully Created'})

                elif (target == 'maintenance'):
                    try:
                        add = Maintenance.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':'Maintenance Successfully Updated'})
                    except Maintenance.DoesNotExist:
                        Maintenance.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Maintenance Successfully Created'})
                    
                
                
                elif (target == 'HowToShopOnline'):
                    try:
                        add = HowToShopOnline.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':' Successfully Updated'})
                    except HowToShopOnline.DoesNotExist:
                        HowToShopOnline.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Successfully Created'})
                    
                            
                elif (target == 'HowToShopOnline'):
                    try:
                        add = HowToShopOnline.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':' Successfully Updated'})
                    except HowToShopOnline.DoesNotExist:
                        HowToShopOnline.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Successfully Created'})

                elif (target == 'OurFabrics'):
                    try:
                        add = OurFabrics.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':' Successfully Updated'})
                    except OurFabrics.DoesNotExist:
                        OurFabrics.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Successfully Created'})
                    

                elif (target == 'OurGarmentQuality'):
                    try:
                        add = OurGarmentQuality.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':' Successfully Updated'})
                    except OurGarmentQuality.DoesNotExist:
                        OurGarmentQuality.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Successfully Created'})
                    
                elif (target == 'PerfectFitGuarantee'):
                    try:
                        add = PerfectFitGuarantee.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':' Successfully Updated'})
                    except PerfectFitGuarantee.DoesNotExist:
                        PerfectFitGuarantee.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Successfully Created'})
                    
                elif (target == 'Weddings'):
                    try:
                        add = Weddings.objects.get(pk=1)
                        add.description=description
                        add.save()
                        return JsonResponse({'status':1, 'message':' Successfully Updated'})
                    except Weddings.DoesNotExist:
                        Weddings.objects.create(description = description)
                        return JsonResponse({'status':1, 'message':'Successfully Created'})
            except Exception:
                return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
    
    
# ==============================================================================
# CREATE AND UPDATE PROJECT INFORMATIONS
# ==============================================================================
@superadmin_required
def UpdatePROJECTInformation(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method=='POST':
                name = request.POST['name']
                title = request.POST['title']
                baseURL = request.POST['baseURL']

                mail = request.POST['mail']
                contact = request.POST['contact']
                address = request.POST['address']

                SECRET_KEY = request.POST['SECRET_KEY']
                DEBUG = request.POST['DEBUG']
            
                if (DEBUG == 'on'):
                    DEBUG = False
                else:
                    DEBUG = True
                print("DEBUG",DEBUG)
                ALLOWED_HOSTS = request.POST['ALLOWED_HOSTS']
                description = request.POST['description']            
            try:
                project = PROJECTInformation.objects.last()
                project.DEBUG = DEBUG
                if (name):
                    project.name = name
                    project.save()
                if (title):
                    project.title = title                  
                    project.save() 

                if (baseURL):
                    project.baseURL = baseURL                  
                    project.save() 
                                        
                if (mail):
                    project.mail = mail                  
                    project.save()
                if (contact):
                    project.contact = contact                  
                    project.save()
                if (address):
                    project.address = address                  
                    project.save()
                if (SECRET_KEY):
                    project.SECRET_KEY = SECRET_KEY
                    project.save()
                if (ALLOWED_HOSTS):
                    project.ALLOWED_HOSTS = ALLOWED_HOSTS
                    project.save()
                if (description):
                    project.description = description
                    project.save()       
      
                return JsonResponse({'status':1, 'message':'Setup & Config Updated'})
            except PROJECTInformation.DoesNotExist:
                PROJECTInformation.objects.create(name=name, title= title, baseURL=baseURL, mail=mail, contact=contact, address=address, mode=mode, SECRET_KEY=SECRET_KEY, DEBUG=DEBUG, ALLOWED_HOSTS=ALLOWED_HOSTS, description=description)
                return JsonResponse({'status':1, 'message':'Setup & Config Created'})
            
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# CREATE AND UPDATE LOGO & ICONS SETTINGS
# ==============================================================================
@superadmin_required
def UpdateLOGOANDICONS(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                headerLogo = request.FILES.get('headerLogo')
                footerLogo = request.FILES.get('footerLogo')
                favicon = request.FILES.get('favicon')             
            try:
                project = PROJECTInformation.objects.last()
                if (headerLogo):
                    project.headerLogo = headerLogo
                    project.save()
                if (footerLogo):
                    project.footerLogo = footerLogo
                    project.save()
                if (favicon):
                    project.favicon = favicon
                    project.save()
                return JsonResponse({'status':1, 'message':'Logo & Icons Updated'})
            except PROJECTInformation.DoesNotExist:
                PROJECTInformation.objects.create(headerLogo=headerLogo, footerLogo= footerLogo, favicon=favicon)
                return JsonResponse({'status':1, 'message':'Logo & Icons Created'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
    
# ==============================================================================
# CREATE AND UPDATE LOGO & ICONS SETTINGS
# ==============================================================================
@superadmin_required
def UpdatePROJECPAYWithPAYPAL(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                PAYPAL_KEY = request.POST.get('PAYPAL_KEY')
                PAYPAL_API_SECRET = request.POST.get('PAYPAL_SECRET')
                PAYPAL_PAY_ACTIVE = request.POST.get('PAYPAL_PAY_STATUS')
                if (PAYPAL_PAY_ACTIVE == 'on'):
                    PAYPAL_PAY_ACTIVE = True
                else:
                    PAYPAL_PAY_ACTIVE = False
            try:
                project = PROJECTInformation.objects.last()                
                if (PAYPAL_KEY):
                    project.PAYPAL_API_KEY = PAYPAL_KEY
                    project.save()
                if (PAYPAL_API_SECRET):
                    project.PAYPAL_API_SECRET = PAYPAL_API_SECRET
                    project.save()
                project.PAYPAL_PAY_ACTIVE = PAYPAL_PAY_ACTIVE
                project.save()
                return JsonResponse({'status':1, 'message':'Paypal Updated'})
            except PROJECTInformation.DoesNotExist:
                PROJECTInformation.objects.create(PAYPAL_API_KEY=PAYPAL_KEY, PAYPAL_API_SECRET= PAYPAL_API_SECRET)
                return JsonResponse({'status':1, 'message':'Paypal Created'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# ==============================================================================
# CREATE AND UPDATE LOGO & ICONS SETTINGS
# ==============================================================================
@superadmin_required
def UpdatePROJECPAYWithRAZORPAY(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                RAZORPAY_KEY = request.POST.get('RAZORPAY_KEY')
                RAZORPAY_SECRET = request.POST.get('RAZORPAY_SECRET')
                RAZORPAY_PAY_ACTIVE = request.POST.get('RAZORPAY_PAY_STATUS')
                if (RAZORPAY_PAY_ACTIVE == 'on'):
                    RAZORPAY_PAY_ACTIVE = True
                else:
                    RAZORPAY_PAY_ACTIVE = False
            try:
                project = PROJECTInformation.objects.last()                
                if (RAZORPAY_KEY):
                    project.RAZORPAY_API_KEY = RAZORPAY_KEY
                    project.save()
                if (RAZORPAY_SECRET):
                    project.RAZORPAY_API_SECRET = RAZORPAY_SECRET
                    project.save()
                project.RAZORPAY_PAY_ACTIVE = RAZORPAY_PAY_ACTIVE
                project.save()
                return JsonResponse({'status':1, 'message':'Razorpay Updated'})
            except PROJECTInformation.DoesNotExist:
                PROJECTInformation.objects.create(RAZORPAY_API_KEY=RAZORPAY_KEY, RAZORPAY_API_SECRET= RAZORPAY_SECRET)
                return JsonResponse({'status':1, 'message':'Razorpay Created'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# CREATE AND UPDATE SMTP SETTINGS
# ==============================================================================
@superadmin_required
def UpdateSMTPSettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method=='POST':
                EMAIL_USE_TLS = request.POST['EMAIL_USE_TLS']
                EMAIL_HOST = request.POST['EMAIL_HOST']
                EMAIL_HOST_USER = request.POST['EMAIL_HOST_USER']
                EMAIL_HOST_PASSWORD = request.POST['EMAIL_HOST_PASSWORD']
                EMAIL_PORT = request.POST['EMAIL_PORT']

                if (EMAIL_USE_TLS == 'on'):
                    EMAIL_USE_TLS = True
                else:
                    EMAIL_USE_TLS = False

            try:
                project = PROJECTInformation.objects.last()
                if (EMAIL_HOST):
                    project.EMAIL_HOST = EMAIL_HOST
                    project.save()
                if (EMAIL_HOST_USER):
                    project.EMAIL_HOST_USER = EMAIL_HOST_USER
                    project.save()
                if (EMAIL_HOST_PASSWORD):
                    project.EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
                    project.save()
                if (EMAIL_PORT):
                    project.EMAIL_PORT = EMAIL_PORT
                    project.save()
                project.EMAIL_USE_TLS = EMAIL_USE_TLS
                project.save()
                return JsonResponse({'status':1, 'message':'SMTP Updated'})
            except PROJECTInformation.DoesNotExist:
                PROJECTInformation.objects.create(EMAIL_HOST=EMAIL_HOST, EMAIL_HOST_USER= EMAIL_HOST_USER, EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD, EMAIL_PORT=EMAIL_PORT, EMAIL_USE_TLS=EMAIL_USE_TLS)
                return JsonResponse({'status':1, 'message':'SMTP Created'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# CREATE AND UPDATE NO REPLY SMTP SETTINGS
# ==============================================================================
@superadmin_required
def UpdateNOReplySMTPSettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method=='POST':
                EMAIL_USE_TLS_NO_REPLY = request.POST['EMAIL_USE_TLS_NO_REPLY']
                EMAIL_HOST_NO_REPLY = request.POST['EMAIL_HOST_NO_REPLY']
                EMAIL_HOST_USER_NO_REPLY = request.POST['EMAIL_HOST_USER_NO_REPLY']
                EMAIL_HOST_PASSWORD_NO_REPLY = request.POST['EMAIL_HOST_PASSWORD_NO_REPLY']
                EMAIL_PORT_NO_REPLY = request.POST['EMAIL_PORT_NO_REPLY']            
                if (EMAIL_USE_TLS_NO_REPLY == 'on'):
                    EMAIL_USE_TLS_NO_REPLY = True
                else:
                    EMAIL_USE_TLS_NO_REPLY = False
            try:
                project = PROJECTInformation.objects.filter(pk=1).last()
                if (EMAIL_HOST_NO_REPLY):
                    project.EMAIL_HOST_NO_REPLY = EMAIL_HOST_NO_REPLY
                    project.save()
                if (EMAIL_HOST_USER_NO_REPLY):
                    project.EMAIL_HOST_USER_NO_REPLY = EMAIL_HOST_USER_NO_REPLY
                    project.save()
                if (EMAIL_HOST_PASSWORD_NO_REPLY):
                    project.EMAIL_HOST_PASSWORD_NO_REPLY = EMAIL_HOST_PASSWORD_NO_REPLY
                    project.save()
                if (EMAIL_PORT_NO_REPLY):
                    project.EMAIL_PORT_NO_REPLY = EMAIL_PORT_NO_REPLY
                    project.save()
                project.EMAIL_USE_TLS_NO_REPLY = EMAIL_USE_TLS_NO_REPLY
                project.save()
                return JsonResponse({'status':1, 'message':'SMTP Updated'})
            except PROJECTInformation.DoesNotExist:
                PROJECTInformation.objects.create(EMAIL_HOST_NO_REPLY=EMAIL_HOST_NO_REPLY, EMAIL_HOST_USER_NO_REPLY= EMAIL_HOST_USER_NO_REPLY, EMAIL_HOST_PASSWORD_NO_REPLY=EMAIL_HOST_PASSWORD_NO_REPLY, EMAIL_PORT_NO_REPLY=EMAIL_PORT_NO_REPLY, EMAIL_USE_TLS_NO_REPLY=EMAIL_USE_TLS_NO_REPLY)
                return JsonResponse({'status':1, 'message':'SMTP Created'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# CREATE AND UPDATE SOCIAL MEDIA SETTINGS
# ==============================================================================
@superadmin_required
def UpdateSocailMedia(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                linkedin = request.POST['linkedin']
                twitter = request.POST['twitter']
                facebook = request.POST['facebook']
                youtube = request.POST['youtube']
                pintrest = request.POST['pintrest']
                instagram = request.POST['instagram']
            try:
                    project = PROJECTInformation.objects.last()
                    if (linkedin):
                        project.linkedin = linkedin
                        project.save()
                    if (facebook):
                        project.facebook = facebook
                        project.save()
                    if (youtube):
                        project.youtube = youtube
                        project.save()
                    if (pintrest):
                        project.pintrest = pintrest
                        project.save()
                    if (instagram):
                        project.instagram = instagram
                        project.save()
                    if (twitter):
                        project.twitter = twitter
                        project.save()
                    return JsonResponse({'status':1, 'message':'Social Links Successfully Updated'})
            except PROJECTInformation.DoesNotExist:
                PROJECTInformation.objects.create(linkedin=linkedin, facebook= facebook, twitter=twitter, youtube=youtube, pintrest=pintrest, instagram=instagram)
                return JsonResponse({'status':1, 'message':'Social Media Created'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# CREATE AND UPDATE MORE SETTINGS
# ==============================================================================
@superadmin_required
def UpdateGOOGLEPSettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                try:
                    project = PROJECTInformation.objects.last()
                    
                    google_analytics = request.POST.get('google_analytics')
                    if (google_analytics):
                        project.google_analytics = google_analytics
                        project.save()
                    
                    google_meta = request.POST.get('google_meta')
                    if (google_meta):
                        project.google_meta = google_meta
                        project.save() 
                        
                    
                    google_developer_token = request.POST.get('google_developer_token')
                    if (google_developer_token):
                        project.google_developer_token = google_developer_token
                        project.save() 
                        
                    google_client_id = request.POST.get('google_client_id')
                    if (google_client_id):
                        project.google_client_id = google_client_id
                        project.save() 
                        
                    google_secret_key = request.POST.get('google_secret_key')
                    if (google_secret_key):
                        project.google_secret_key = google_secret_key
                        project.save() 
                        
                    google_refresh_token = request.POST.get('google_refresh_token')
                    if (google_refresh_token):
                        project.google_refresh_token = google_refresh_token
                        project.save() 
                        
                    google_login_customer_id = request.POST.get('google_login_customer_id')
                    if (google_login_customer_id):
                        project.google_login_customer_id = google_login_customer_id
                        project.save()      
                        
              

                    return JsonResponse({'status':1, 'message':'Google Code Successfully Updated'})
                except PROJECTInformation.DoesNotExist:
                    PROJECTInformation.objects.create(google_analytics=google_analytics, google_meta= google_meta)
                    return JsonResponse({'status':1, 'message':'Google Code Created'})
                
            return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
    
# ==============================================================================
# CREATE AND UPDATE MORE SETTINGS
# ==============================================================================
@superadmin_required
def UpdateCHATBOTPSettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                tawk = request.POST['tawk']
                try:
                    project = PROJECTInformation.objects.last()
                    if (tawk):
                        project.tawk = tawk
                        project.save()
                    return JsonResponse({'status':1, 'message':'ChatBoat Successfully Updated'})
                except Exception as e:
                    return JsonResponse({'status':1, 'message':'ChatBoat Error Occured'})
                
            return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})

# ==============================================================================
# CHAT GTP API KEY SETTINGS
# ==============================================================================
@superadmin_required
def updateCHATGTPSettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                ChatGTP_API_KEY = request.POST.get('ChatGTP_API_KEY')
                try:
                    project = PROJECTInformation.objects.last()
                    if (ChatGTP_API_KEY):
                        project.ChatGTP_API_KEY = ChatGTP_API_KEY
                        project.save()
                    return JsonResponse({'status':1, 'message':'ChatGTP API KEY Updated'})
                except Exception as e:
                    return JsonResponse({'status':1, 'message':'ChatBoat Error Occured'})
                
            return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})

# ==============================================================================
# ==============================================================================
# CREATE AND UPDATE MORE SETTINGS
# ==============================================================================
@superadmin_required
def UpdateMETASettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            if request.method =='POST':
                
                meta_title = request.POST['meta_title']
                meta_keywords = request.POST['meta_keywords']
                meta_description = request.POST['meta_description']
                try:
                    project = PROJECTInformation.objects.last()
                    if (meta_title):
                        project.meta_title = meta_title
                        project.save()
                    if (meta_keywords):
                        project.meta_keywords = meta_keywords
                        project.save()   
                    if (meta_description):
                        project.meta_description = meta_description
                        project.save()       
                    return JsonResponse({'status':1, 'message':'Meta Successfully Updated'})
                except PROJECTInformation.DoesNotExist:
                    PROJECTInformation.objects.create(meta_title=meta_title, meta_keywords= meta_keywords, meta_description=meta_description)
                    return JsonResponse({'status':1, 'message':'Meta Created'})

            return JsonResponse({'status':0, 'message':'Bad Request'})        
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Access'})

    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
