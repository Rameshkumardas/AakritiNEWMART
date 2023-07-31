
from django.http import Http404, JsonResponse
from AdminAuthentication.models import AdminActivity
from EVENTManager.models import EVENTMainCat, EVENTSubCat
from django.contrib.auth.decorators import login_required
from AdminAuthentication.decorators import superadmin_required
# ==============================================================================
# DELETE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def DELETEEVENTMainCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                if request.POST.get('targetMainCat'):
                    mainCat = EVENTMainCat.objects.get(pk=request.POST.get('targetMainCat'))
                    mainCat.delete()
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {mainCat.name} ] - EVENTMainCat Deleted<span>')
                    return JsonResponse({'status':1, 'message':'Permanently Deleted Successfully', 'Reload':request.META.get('HTTP_REFERER')})
                else:
                    return JsonResponse({'status':0, 'message':'Target Required*'})
            except Exception:
                return JsonResponse({'status':0, 'message':'BError Occured'})
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# MORE ACCTIONS
# ==============================================================================
@superadmin_required
def DELETEEVENTSubCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                if request.POST.get('targetSubCat'):
                    mainCat = EVENTSubCat.objects.get(pk=request.POST.get('targetSubCat'))
                    mainCat.delete()
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {mainCat.name} ] - EVENTSubCat Deleted<span>')
                    return JsonResponse({'status':1, 'message':'Permanently Deleted Successfully', 'Reload':request.META.get('HTTP_REFERER')})
                else:
                    return JsonResponse({'status':0, 'message':'Target Required*'})
            except Exception:
                return JsonResponse({'status':0, 'message':'BError Occured'})
        else:
            raise Http404
    else:
        raise Http404
