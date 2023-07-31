from django.conf import settings
from AdminAuthentication.decorators import accountant_required, superadmin_required 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminActivity
from django.shortcuts import render, redirect
from BLOGManager.models import BlogMainCat
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.urls import reverse
import random
import os

from ExtraSettings.models import PROJECTInformation
file = '../settings.ini'
FilePath = os.path.join(settings.BASE_DIR, file)
isPath = os.path.isfile(FilePath)
# ==============================================================================
# DEACTIVATED BLOG MAIN CATEGORY
# ==============================================================================
@superadmin_required
def CREATESettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            try:
                project = PROJECTInformation.objects.last()
                if isPath:
                    print('isPath')
                    f = open(FilePath, "w")
                    f.write('[settings]')
                    f.write('\n\n{}={}'.format('PROJECT_NAME', project.name))
                    f.write('\n{}={}'.format('DEBUG', project.DEBUG))
                    f.write('\n{}={}'.format('ALLOWED_HOSTS', project.ALLOWED_HOSTS))
                    f.write('\n{}={}'.format('SECRET_KEY', project.SECRET_KEY.replace('%', 'AakritiCMS')))  
                    
                    f.write('\n\n{}={}'.format('DB_NAME', project.name))
                    f.write('\n{}={}'.format('DB_USER', 'root'))
                    f.write('\n{}={}'.format('DB_PASSWORD', ''))
                                  
                    f.write('\n\n{}={}'.format('PAYPAL_API_KEY', project.PAYPAL_API_KEY))
                    f.write('\n{}={}'.format('PAYPAL_API_SECRET', project.PAYPAL_API_SECRET))
                    f.write('\n{}={}'.format('PAYPAL_PAY_ACTIVE', project.PAYPAL_PAY_ACTIVE))
                    
                    f.write('\n\n{}={}'.format('RAZORPAY_API_KEY', project.RAZORPAY_API_KEY))
                    f.write('\n{}={}'.format('RAZORPAY_API_SECRET', project.RAZORPAY_API_SECRET))
                    f.write('\n{}={}'.format('RAZORPAY_PAY_ACTIVE', project.RAZORPAY_PAY_ACTIVE))

                    # f.write('\n\n{}={}'.format('HOME_PAGE', project.baseURL))
                    # f.write('\n{}={}'.format('AFTERLogin', project.baseURL))
                    f.close()
                    
                else:
                    f = open(FilePath, "x")
                    f.write('[settings]')
                    f.write('\n\n{}={}'.format('PROJECT_NAME', project.name))
                    f.write('\n{}={}'.format('DEBUG', project.DEBUG))
                    f.write('\n{}={}'.format('SECRET_KEY', project.SECRET_KEY.replace('%', 'AakritiCMS')))
                    f.write('\n\n{}={}'.format('PAYPAL_API_KEY', project.PAYPAL_API_KEY))
                    f.write('\n{}={}'.format('PAYPAL_API_SECRET', project.PAYPAL_API_SECRET))
                    f.write('\n{}={}'.format('PAYPAL_PAY_ACTIVE', project.PAYPAL_PAY_ACTIVE))
                    f.write('\n\n{}={}'.format('RAZORPAY_API_KEY', project.RAZORPAY_API_KEY))
                    f.write('\n{}={}'.format('RAZORPAY_API_SECRET', project.RAZORPAY_API_SECRET))
                    f.write('\n{}={}'.format('RAZORPAY_PAY_ACTIVE', project.RAZORPAY_PAY_ACTIVE))

                    f.write('\n\n{}={}'.format('DB_NAME', project.name))
                    f.write('\n{}={}'.format('DB_USER', 'root'))
                    f.write('\n{}={}'.format('DB_PASSWORD', ''))
                                  
                    # f.write('\n\n{}={}'.format('HOME_PAGE', project.baseURL))
                    # f.write('\n{}={}'.format('AFTERLogin', project.baseURL))
                    
                    
                    f.close()  
                 
                messages.success(request, 'Settings Created Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except Exception as e:
                f = open(FilePath, "x")
                f.write('[settings]')
                f.write('\n\n{}={}'.format('PROJECT_NAME', 'AakritiCMS'))
                f.write('\n{}={}'.format('DEBUG', True))
                f.write('\n{}={}'.format('ALLOWED_HOSTS', '*'))
                f.write('\n{}={}'.format('SECRET_KEY', 'project.SECRET_KEY'))
                f.write('\n\n{}={}'.format('PAYPAL_API_KEY', 'project.PAYPAL_API_KEY'))
                f.write('\n{}={}'.format('PAYPAL_API_SECRET', 'project.PAYPAL_API_SECRET'))
                f.write('\n{}={}'.format('PAYPAL_PAY_ACTIVE', 'project.PAYPAL_PAY_ACTIVE'))
                f.write('\n\n{}={}'.format('RAZORPAY_API_KEY', 'project.RAZORPAY_API_KEY'))
                f.write('\n{}={}'.format('RAZORPAY_API_SECRET', 'project.RAZORPAY_API_SECRET'))
                f.write('\n{}={}'.format('RAZORPAY_PAY_ACTIVE', 'project.RAZORPAY_PAY_ACTIVE'))
                f.write('\n\n{}={}'.format('DB_NAME', ''))
                f.write('\n{}={}'.format('DB_USER', ''))
                f.write('\n{}={}'.format('DB_PASSWORD', ''))
                # f.write('\n\n{}={}'.format('HOME_PAGE', 'project.baseURL'))
                # f.write('\n{}={}'.format('AFTERLogin', 'project.baseURL'))
                
                f.close()   
                print(e)
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")