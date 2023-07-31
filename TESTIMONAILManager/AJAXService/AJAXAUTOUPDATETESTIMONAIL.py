from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminActivity
from EVENTManager.models import EVENTList
from django.http import JsonResponse
from django.utils import timezone
# ==============================================================================
# UPDATE AUTOUPDATEEVENT
# ==============================================================================
@accountant_required
def AUTOUPDATEEVENT(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method == "POST":
                target = request.POST.get('target')
                try:
                    EVENT = EVENTList.objects.get(pk=target)

                 

# 
                    slug = request.POST.get('slug')
                    if slug and slug!=EVENT.slug:
                        if EVENTList.objects.filter(slug=slug).exists():
                            pass
                        else:
                            EVENT.slug = slug
                            EVENT.save()

                    name = request.POST.get('name')
                    if name:
                        EVENT.name = name
                        EVENT.save()

                    img = request.FILES.get('img')
                    if img:
                        EVENT.img = img
                        EVENT.save()

                    intro = request.POST.get('intro') 
                    if intro:
                        EVENT.intro = intro
                        EVENT.save()
                        

                    
                    description = request.POST.get('description')
                    if description:
                        EVENT.description = description
                        EVENT.save()
                        
                        
                    summary = request.POST.get('summary')
                    if summary:
                        EVENT.summary = summary
                        EVENT.save()
                        


                    reference = request.POST.get('references')
                    if reference:
                        EVENT.reference = reference

                    meta_title = request.POST.get('meta_title')
                    if meta_title:
                        EVENT.meta_title = meta_title
                        EVENT.save()

                    meta_keywords = request.POST.get('meta_keywords')
                    if meta_keywords:
                        EVENT.meta_keywords = meta_keywords
                        EVENT.save()

                    meta_description = request.POST.get('meta_description')
                    if meta_description:
                        EVENT.meta_description = meta_description
                        EVENT.save()

                    EVENT.last_update = timezone.now()
                    EVENT.save()
                    return JsonResponse({'status':1, 'message':'Successfully Updated'})                   
                except Exception as e:
                    print(e)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> Error Occured EVENT Updating: [ {e} ]<span>')
                    return JsonResponse({'status':0, 'message':f'Error Occured'})
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})