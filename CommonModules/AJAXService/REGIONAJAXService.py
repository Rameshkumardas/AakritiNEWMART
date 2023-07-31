
from AdminAuthentication.decorators import admin_required
from CommonModules.models import REGIONList
from django.http import JsonResponse
import datetime
# ==============================================================================
# CREATE NEW REGION
# ============================================================================== 
@admin_required 
def createREGION(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            if request.method=="POST":
                try:
                    if request.POST.get('name')!='':
                        name = request.POST.get('name')
                    else:
                        return JsonResponse({'status':0, 'message':'Region Required*'}) 

                    if request.POST.get('pincode')!='':
                        code = request.POST.get('pincode')
                    else:
                        return JsonResponse({'status':0, 'message':'PinCode Required*'}) 

                    if REGIONList.objects.filter(name=name, pcode=code).exists():
                        return JsonResponse({'status':0, 'message':'URL Already Exists'}) 
                    else:
                  
                        REGIONList.objects.create(name=name, pcode=code)
                        return JsonResponse({'status':1, 'message':'Region Created', 'AFTERTask':request.META.get('HTTP_REFERER')}) 
                except Exception:
                    
                    return JsonResponse({'status':0, 'message':'Error Occured'}) 
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'}) 
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# UPDATE REGION
# ==============================================================================    
@admin_required    
def updateREGIONAJAX(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            if request.method=="POST":
                target = request.POST.get('target')
                try:
                    Region = REGIONList.objects.get(pk=target)
                    if request.POST.get('name')!='':
                        Region.name = request.POST.get('name')
                        Region.save()
                    else:
                        return JsonResponse({'status':0, 'message':'Name is Empty'}) 

                    if request.POST.get('pincode')!='':
                        Region.pcode = request.POST.get('pincode')
                        Region.last_update = datetime.datetime.now()
                        Region.save()
                        return JsonResponse({'status':1, 'message':'Update Successfull', 'AFTERTask':request.META.get('HTTP_REFERER')}) 
                    else:
                        return JsonResponse({'status':0, 'message':'Color is Empty'}) 
                except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'}) 
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'}) 
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# ACTIVATED REGION HERE
# ============================================================================== 
@admin_required
def activatedREGION(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            target = request.POST.get('target')
            try:
                REGIONList.objects.filter(pk=target).update(is_active=True)
                return JsonResponse({'status':1, 'message':'Activated Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except REGIONList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'REGION DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DEACTIVATED REGION HERE
# ============================================================================== 
@admin_required
def deactivatedREGION(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            target = request.POST.get('target')
            try:
                REGIONList.objects.filter(pk=target).update(is_active=False)
                return JsonResponse({'status':1, 'message':'Deactivated Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except REGIONList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'REGION DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DELETE REGION HERE
# ==============================================================================   
@admin_required     
def deleteREGION(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                target = request.POST.get('target')
                REGIONList.objects.filter(pk=target).delete()
                return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except REGIONList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'REGION DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# MORE MANAGER SETTINGS
# ============================================================================== 

