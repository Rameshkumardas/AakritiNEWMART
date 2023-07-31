from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminActivity
from BLOGManager.models import BLOGList
from django.http import JsonResponse
from django.utils import timezone
# ==============================================================================
# UPDATE AUTOUPDATEBLOG
# ==============================================================================
@accountant_required
def AUTOUPDATEBLOG(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method == "POST":
                target = request.POST.get('target')
                try:
                    blog = BLOGList.objects.get(pk=target)

                    mainCat = request.POST.get('mainCat')
                    print("mainCat", mainCat)
                    if mainCat and mainCat!=blog.mainCat_id:
                        blog.mainCat_id = mainCat
                        blog.save()

                    subCat = request.POST.get('subCat')
                    if subCat and subCat!=blog.SubCat_id:
                        blog.SubCat_id = subCat
                        blog.save()
                        
                    slug = request.POST.get('slug')
                    if slug and slug!=blog.slug:
                        if BLOGList.objects.filter(slug=slug).exists():
                            pass
                        else:
                            blog.slug = slug
                            blog.save()

                    name = request.POST.get('name')
                    if name and subCat!=blog.name:
                        blog.name = name
                        blog.save()

                    img = request.FILES.get('img')
                    if img:
                        blog.img = img
                        blog.save()

                    intro = request.POST.get('intro') 
                    if intro and subCat!=blog.intro:
                        blog.intro = intro
                        blog.save()
                        
                    description = request.POST.get('description')
                    if description and subCat!=blog.description:
                        blog.description = description
                        blog.save()
                        
                        
                    summary = request.POST.get('summary')
                    if summary and subCat!=blog.summary:
                        blog.summary = summary
                        blog.save()
                        
                    reference = request.POST.get('references')
                    if reference and subCat!=blog.reference:
                        blog.reference = reference

                    meta_title = request.POST.get('meta_title')
                    if meta_title and subCat!=blog.meta_title:
                        blog.meta_title = meta_title
                        blog.save()

                    meta_keywords = request.POST.get('meta_keywords')
                    if meta_keywords and subCat!=blog.meta_keywords:
                        blog.meta_keywords = meta_keywords
                        blog.save()

                    meta_description = request.POST.get('meta_description')
                    if meta_description and subCat!=blog.meta_description:
                        blog.meta_description = meta_description
                        blog.save()

                    blog.last_update = timezone.now()
                    blog.save()
                    return JsonResponse({'status':1, 'message':'Successfully Updated'})                   
                except Exception as e:
                    print(e)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> Error Occured BLOG Updating: [ {e} ]<span>')
                    return JsonResponse({'status':0, 'message':f'Error Occured'})
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})