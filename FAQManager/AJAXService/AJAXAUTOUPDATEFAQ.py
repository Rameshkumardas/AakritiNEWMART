from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminActivity
from ..models import FAQList
from django.http import JsonResponse
from django.utils import timezone
# ==============================================================================
# UPDATE AUTOUPDATESOLUTION
# ==============================================================================
@accountant_required
def AUTOUPDATESOLUTION(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method == "POST":
                target = request.POST.get('target')
                try:
                    SOLUTION = FAQList.objects.get(pk=target)

                    mainCat = request.POST.get('mainCat')
                    if mainCat and mainCat!=SOLUTION.mainCat_id:
                        SOLUTION.mainCat_id = mainCat
                        SOLUTION.save()

                    subCat = request.POST.get('subCat')
                    if subCat and subCat!=SOLUTION.SubCat_id:
                        SOLUTION.SubCat_id = subCat
                        SOLUTION.save()
# 
                    slug = request.POST.get('slug')
                    if slug and slug!=SOLUTION.slug:
                        if FAQList.objects.filter(slug=slug).exists():
                            pass
                        else:
                            SOLUTION.slug = slug
                            SOLUTION.save()

                    name = request.POST.get('name')
                    if name and subCat!=SOLUTION.name:
                        SOLUTION.name = name
                        SOLUTION.save()

                
                    is_url = request.POST.get('PAGE_TYPE')
                    if is_url == 'is_url':
                        is_url = True
                    else:
                        is_url = False
                        
                    
                    redirect_to = request.POST.get('slug')
                    if redirect_to and is_url:
                        SOLUTION.redirect_to = redirect_to
                        SOLUTION.save()

                    
                    img = request.FILES.get('img')
                    if img:
                        SOLUTION.img = img
                        SOLUTION.save()

                    intro = request.POST.get('intro') 
                    if intro and subCat!=SOLUTION.intro:
                        SOLUTION.intro = intro
                        SOLUTION.save()
                        
                    
                    description = request.POST.get('description')
                    if description and subCat!=SOLUTION.description:
                        SOLUTION.description = description
                        SOLUTION.save()
                        
                        
                    summary = request.POST.get('summary')
                    if summary and subCat!=SOLUTION.summary:
                        SOLUTION.summary = summary
                        SOLUTION.save()
                        


                    reference = request.POST.get('references')
                    if reference and subCat!=SOLUTION.reference:
                        SOLUTION.reference = reference

                    meta_title = request.POST.get('meta_title')
                    if meta_title and subCat!=SOLUTION.meta_title:
                        SOLUTION.meta_title = meta_title
                        SOLUTION.save()

                    meta_keywords = request.POST.get('meta_keywords')
                    if meta_keywords and subCat!=SOLUTION.meta_keywords:
                        SOLUTION.meta_keywords = meta_keywords
                        SOLUTION.save()

                    meta_description = request.POST.get('meta_description')
                    if meta_description and subCat!=SOLUTION.meta_description:
                        SOLUTION.meta_description = meta_description
                        SOLUTION.save()

                    SOLUTION.mainCat_id = SOLUTION.SubCat.mainCat.pk
                    SOLUTION.last_update = timezone.now()
                    SOLUTION.save()
                    return JsonResponse({'status':1, 'message':'Successfully Updated'})                   
                except Exception as e:
                    print(e)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> Error Occured SOLUTION Updating: [ {e} ]<span>')
                    return JsonResponse({'status':0, 'message':f'Error Occured'})
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})