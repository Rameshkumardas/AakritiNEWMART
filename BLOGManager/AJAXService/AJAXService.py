
from django.http import Http404, JsonResponse
from AdminAuthentication.models import AdminActivity
from BLOGManager.models import BlogMainCat, BlogSubCat, allBLOGCOMMENTS, replyBLOGCOMMENTS, replyCHILDBLOGCOMMENTS
from django.contrib.auth.decorators import login_required
from AdminAuthentication.decorators import superadmin_required
# ==============================================================================
# DELETE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def DELETEBLOGMainCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                if request.POST.get('targetMainCat'):
                    mainCat = BlogMainCat.objects.get(pk=request.POST.get('targetMainCat'))
                    mainCat.delete()
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {mainCat.name} ] - BLOGMainCat Deleted<span>')
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
def DELETEBLOGSubCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                if request.POST.get('targetSubCat'):
                    mainCat = BlogSubCat.objects.get(pk=request.POST.get('targetSubCat'))
                    mainCat.delete()
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {mainCat.name} ] - BLOGSubCat Deleted<span>')
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
@login_required
def ReplyCommentRequest(request):
    try:
        if request.method == "POST":
            comment_for = request.POST.get('comment_for')
            comment_id = request.POST.get('targetVAL')
            reply_comment = request.POST.get('replyComment') 
            if comment_for == "parents":
                replyBLOGCOMMENTS.objects.create(comment_id=comment_id, author_id=request.user.pk, description=reply_comment)
            elif comment_for == "child":
                replyCHILDBLOGCOMMENTS.objects.create(comment_id=comment_id, author_id=request.user.pk, description=reply_comment)
            else:
                pass         
            return JsonResponse({'status':1, 'message':'Reply Comment Added', 'AFTERTask':request.META.get('HTTP_REFERER')})
        else:
            return JsonResponse({'status':0, 'message':'Not Valid Request'})
    except Exception:
        return JsonResponse({'status':0, 'message':'BError Occured'})

# ==============================================================================
# MORE ACCTIONS
# ==============================================================================
@login_required
def DELETECommentRequest(request):
    try:
        if request.method == "POST":
            comment_for = request.POST.get('comment_for')
            comment_id = request.POST.get('targetVAL')            
            if comment_for == "parents":
                try:
                    comment = allBLOGCOMMENTS.objects.get(pk=comment_id, user_id=request.user.pk)
                    comment.delete()
                    return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'{e} Error Occured'})
            elif comment_for == "child":
                try:
                    comment = replyBLOGCOMMENTS.objects.get(pk=comment_id, author_id=request.user.pk)
                    comment.delete()
                    return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'{e} Error Occured'})
            elif comment_for == "subchild":
                try:
                    comment = replyCHILDBLOGCOMMENTS.objects.get(pk=comment_id, author_id=request.user.pk)
                    comment.delete()
                    return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'{e} Error Occured'})

            else:
                return JsonResponse({'status':0, 'message':'Not Valid Request'})         
        else:
            return JsonResponse({'status':0, 'message':'Not Valid Request'})
    except Exception:
        return JsonResponse({'status':0, 'message':'BError Occured'})
