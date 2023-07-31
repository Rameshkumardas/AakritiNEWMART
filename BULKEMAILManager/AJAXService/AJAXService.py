from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminActivity
from BULKEMAILManager.models import EMAILList
from django.http import JsonResponse
from django.utils import timezone
import re

valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
# ==============================================================================
# UPDATE AUTOUPDATEEMAIL
# ==============================================================================
@accountant_required
def addEMAIL(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method == "POST":
                AFTERLogin = f"{request.META.get('HTTP_REFERER')}"  
                try:
                    name = request.POST.get('name')
                    if name:
                        name = name
                    else:
                        return JsonResponse({'status':0, 'message':'Name Required*', 'AFTERLogin':AFTERLogin})                   

                    email = request.POST.get('email')
                    if email:
                        if(re.search(valid_email, email)):   
                            email = email
                        else:   
                            return JsonResponse({'status':0, 'message':'Email is Not Valid'})                   
                    else:
                        return JsonResponse({'status':0, 'message':'Email Required*'})                   


                    contact = request.POST.get('contact')
                    if contact:
                        contact = contact
                    else:
                        contact = ''
                        
                    author = request.user
                    EMAILList.objects.create(name=name, email=email, contact=contact, author=author)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {name} ] - EMAIL Created<span>')
                    
                    return JsonResponse({'status':1, 'message':'Successfully Updated','AFTERLogin':AFTERLogin})                   
                except Exception as e:
                    print(e)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> Error Occured EMAIL Updating: [ {e} ]<span>')
                    return JsonResponse({'status':0, 'message':f'{e} Error Occured'})
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})