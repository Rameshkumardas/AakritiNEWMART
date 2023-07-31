from AdminAuthentication.decorators import superadmin_required
from django.http import Http404, JsonResponse
from ..models import MainCategory
# ==============================================================================
# BUKL ACTIVATE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def BULK_ACTIVATE_MAIN_CATEGORY(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            bulk_target = request.POST.get('id')
            if bulk_target:
                for target in bulk_target.split(","):
                    try:
                        obj = MainCategory.objects.get(pk=target)
                        obj.is_active = True
                        obj.save()
                    except Exception:
                        return JsonResponse({'status':0, 'message': f'Error Occured'})
                return JsonResponse({'status':1, 'message':'Successfully Activated', 'AFTERTask':request.META.get('HTTP_REFERER')})
            else:
                return JsonResponse({'status':0, 'message':'Target Required*'})
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# BUKL ACTIVATE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def BULK_DEACTIVATE_MAIN_CATEGORY(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            bulk_target = request.POST.get('id')
            print(bulk_target)
            if bulk_target:
                for target in bulk_target.split(","):
                    try:
                        obj = MainCategory.objects.get(pk=target)
                        obj.is_active = False
                        obj.save()
                    except Exception:
                        return JsonResponse({'status':0, 'message': f'Error Occured'})
                return JsonResponse({'status':1, 'message':'Successfully Deactivated', 'AFTERTask':request.META.get('HTTP_REFERER')})
            else:
                return JsonResponse({'status':0, 'message':'Target Required*'})
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# BUKL ACTIVATE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def BULK_DELETE_MAIN_CATEGORY(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            bulk_target = request.POST.get('id')
            if bulk_target:
                for target in bulk_target.split(","):
                    try:
                        obj = MainCategory.objects.get(pk=target)
                        obj.delete()
                    except Exception:
                        return JsonResponse({'status':0, 'message': f'Error Occured'})
                return JsonResponse({'status':1, 'message':'Successfully Deleted', 'AFTERTask':request.META.get('HTTP_REFERER')})
            else:
                return JsonResponse({'status':0, 'message':'Target Required*'})
        else:
            raise Http404
    else:
        raise Http404




