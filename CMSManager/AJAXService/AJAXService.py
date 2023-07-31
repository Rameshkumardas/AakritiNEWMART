from django.http import Http404, JsonResponse
from AdminAuthentication.models import AdminActivity
from ..models import SECTIONList
from django.contrib.auth.decorators import login_required
from AdminAuthentication.decorators import superadmin_required
# ==============================================================================
# DELETE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def DELETESECTION(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                if request.POST.get('targetOBJ'):
                    obj = SECTIONList.objects.get(pk=request.POST.get('targetOBJ'))
                    obj.delete()
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {obj.name} ] - Section Deleted<span>')
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
