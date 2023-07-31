from AdminAuthentication.decorators import accountant_required, admin_required
from CommonModules.models import SHIPPINGList
from django.http import JsonResponse
import datetime
# ==============================================================================
# CREATE NEW SHIPPING
# ==============================================================================  
@admin_required
def createSHIPPING(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                if request.method =="POST":
                    if request.POST['type']!='':
                        type = request.POST['type']
                    else:
                        return JsonResponse({'status':0, 'message':'Type is Empty'})
                    if request.POST['kg_min_range']!='':
                        kg_min_range = request.POST['kg_min_range']
                    else:
                        return JsonResponse({'status':0, 'message':'KG Min is Empty'})
                    if request.POST['kg_max_range']!='':
                        kg_max_range = request.POST['kg_max_range']
                    else:
                        return JsonResponse({'status':0, 'message':'KG Max is Empty'})
                    if request.POST['local']!='':
                        local = request.POST['local']
                    else:
                        return JsonResponse({'status':0, 'message':'Local is Empty'})
                
                    if request.POST['regional']!='':
                        regional = request.POST['regional']
                    else:
                        return JsonResponse({'status':0, 'message':'Regional is Empty'})
                    if request.POST['national']!='':
                        national = request.POST['national']
                    else:
                        return JsonResponse({'status':0, 'message':'National is Empty'})
                    if request.POST['special']!='':
                        special = request.POST['special']
                    else:
                        return JsonResponse({'status':0, 'message':'Special is Empty'})
                    KG_Range = kg_min_range,kg_max_range
                    print(KG_Range)
                    if SHIPPINGList.objects.filter(type=type,kg_range =KG_Range,local=local,regional=regional,national=national,special=special).exists():
                        return JsonResponse({'status':0, 'message':'Shipping Already Exists'})
                    else:
                        SHIPPINGList.objects.create(type=type,kg_range =KG_Range,local=local,regional=regional,national=national,special=special)
                        return JsonResponse({'status':1, 'message':'Shipping Added', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except Exception as e:
                return JsonResponse({'status':0, 'message': f'{e} - Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# UPDATE SHIPPING
# ==============================================================================  
@admin_required      
def updateSHIPPINGAJAX(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                target = request.POST.get('target')
                shipping = SHIPPINGList.objects.get(pk=target)
                if request.method =="POST":
                    if request.POST.get('type')!='':
                        shipping.type = request.POST.get('type')
                        shipping.save()
                    else:
                        return JsonResponse({'status':0, 'message':'Type is Empty'})
                    if request.POST.get('kg_min_range')!='':
                        kg_min_range = request.POST.get('kg_min_range')
                    else:
                        return JsonResponse({'status':0, 'message':'KG Min is Empty'})
                    if request.POST.get('kg_max_range')!='':
                        kg_max_range = request.POST.get('kg_max_range')
                    else:
                        return JsonResponse({'status':0, 'message':'KG Max is Empty'})
                    if request.POST.get('local')!='':
                        shipping.local = request.POST.get('local')
                        shipping.save()
                    else:
                        return JsonResponse({'status':0, 'message':'Local is Empty'})
                
                    if request.POST.get('regional')!='':
                        shipping.regional = request.POST.get('regional')
                    else:
                        return JsonResponse({'status':0, 'message':'Regional is Empty'})
                    if request.POST.get('national')!='':
                        shipping.national = request.POST.get('national')
                        shipping.save()
                    else:
                        return JsonResponse({'status':0, 'message':'National is Empty'})
                    if request.POST.get('special')!='':
                        shipping.special = request.POST.get('special')
                        shipping.save()
                    else:
                        return JsonResponse({'status':0, 'message':'Special is Empty'})
                    KG_Range = kg_min_range, kg_max_range
                    shipping.kg_range = KG_Range
                    shipping.last_update = datetime.datetime.today()
                    shipping.save()
                    return JsonResponse({'status':1, 'message':'Update Shipping', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except Exception as e:
                # name 'local' is not defined - Error Occured
                return JsonResponse({'status':0, 'message': f'{e} - Error Occured'}) 
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# ACTIVATED SHIPPING HERE
# ============================================================================== 
@admin_required
def activatedSHIPPING(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            target = request.POST.get('target')
            try:
                SHIPPINGList.objects.filter(pk=target).update(is_active=True)
                return JsonResponse({'status':1, 'message':'Activated Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except SHIPPINGList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'SHIPPING DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DEACTIVATED SHIPPING HERE
# ==============================================================================
@admin_required 
def deactivatedSHIPPING(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            target = request.POST.get('target')
            try:
                SHIPPINGList.objects.filter(pk=target).update(is_active=False)
                return JsonResponse({'status':1, 'message':'Deactivated Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except SHIPPINGList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'SHIPPING DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DELETE SHIPPING HERE
# ==============================================================================   
@admin_required     
def deleteSHIPPING(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                target = request.POST.get('target')
                SHIPPINGList.objects.filter(pk=target).delete()
                return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except SHIPPINGList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'SHIPPING DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# MORE MANAGER SETTINGS
# ============================================================================== 

