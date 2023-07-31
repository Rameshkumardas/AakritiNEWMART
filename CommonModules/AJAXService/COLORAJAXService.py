
from AdminAuthentication.decorators import admin_required
from CommonModules.models import COLORList
from django.http import JsonResponse
import datetime
# ==============================================================================
# CREATE NEW COLOR
# ============================================================================== 
@admin_required 
def createCOLOR(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            if request.method=="POST":
                try:
                    if request.POST['name']!='':
                        name0 = request.POST['name']
                        name = name0.replace(' ', '')
                    else:
                        return JsonResponse({'status':0, 'message':'Name is Empty'}) 

                    if request.POST['code']!='':
                        code = request.POST['code']
                    else:
                        return JsonResponse({'status':0, 'message':'Color Code is Empty'}) 

                    if COLORList.objects.filter(name=name).exists():
                        return JsonResponse({'status':1, 'message':'URL Already Exists'}) 
                    else:
                        COLORList.objects.create(name=name, code=code)
                        return JsonResponse({'status':1, 'message':'Color Created'}) 
                except Exception:
                     return JsonResponse({'status':0, 'message':'Error Occured'}) 
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'}) 
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# UPDATE COLOR
# ==============================================================================    
@admin_required    
def updateCOLORAJAX(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            if request.method=="POST":
                target = request.POST.get('target')
                try:
                    COLOR = COLORList.objects.get(pk=target)
                    if request.POST.get('name')!='':
                        COLOR.name = request.POST.get('name')
                        print(request.POST.get('name'))
                        COLOR.save()
                    else:
                        return JsonResponse({'status':0, 'message':'Name is Empty'}) 

                    if request.POST.get('code')!='':
                        COLOR.code = request.POST.get('code')
                        print(request.POST.get('code'))

                        COLOR.last_update = datetime.datetime.now()
                        COLOR.save()
                        return JsonResponse({'status':1, 'message':'Update Successfull'}) 
                    else:
                        return JsonResponse({'status':0, 'message':'Color is Empty'}) 
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'{e} Error Occured'}) 
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'}) 
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# ACTIVATED COLOR HERE
# ==============================================================================
@admin_required
def activatedCOLOR(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            target = request.POST.get('target')
            try:
                COLORList.objects.filter(pk=target).update(is_active=True)
                return JsonResponse({'status':1, 'message':'Activated Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except COLORList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'COLOR DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DEACTIVATED COLOR HERE
# ============================================================================== 
@admin_required
def deactivatedCOLOR(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            target = request.POST.get('target')
            try:
                COLORList.objects.filter(pk=target).update(is_active=False)
                return JsonResponse({'status':1, 'message':'Deactivated Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except COLORList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'COLOR DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DELETE COLOR HERE
# ==============================================================================   
@admin_required     
def deleteCOLOR(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                target = request.POST.get('target')
                COLORList.objects.filter(pk=target).delete()
                return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
            except COLORList.DoesNotExist:
                return JsonResponse({'status':0, 'message':'COLOR DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# MORE MANAGER SETTINGS
# ============================================================================== 

