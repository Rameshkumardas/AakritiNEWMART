from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminActivity
from BULKEMAILManager.models import EMAILList
from django.http import JsonResponse
from django.utils import timezone

# ==============================================================================
# UPDATE AUTOUPDATEEMAIL
# ==============================================================================
@accountant_required
def AUTOUPDATEEMAIL(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method == "POST":
                target = request.POST.get('target')
                try:
                    email = EMAILList.objects.get(pk=target)

                    name = request.POST.get('name')
                    if name:
                        email.name = name

                    email = request.POST.get('email')
                    if email:
                        email.email = email
                        email.save()

                    contact = request.POST.get('contact')
                    if contact:
                        email.contact = contact

                    email.last_update = timezone.now()
                    email.save()
                    return JsonResponse({'status':1, 'message':'Successfully Updated'})                   
                except Exception as e:
                    print(e)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> Error Occured EMAIL Updating: [ {e} ]<span>')
                    return JsonResponse({'status':0, 'message':f'Error Occured'})
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})