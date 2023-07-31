from django.contrib.auth.decorators import login_required
from AdminAuthentication.models import AdminRegistration
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TestimonialCatList, TestimonialList
from django.http import Http404
import datetime
import random
# ==============================================================================
# CREATETestimonial Category  
# ==============================================================================
@login_required
def CreateTestimonailCategory(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            TestimonailCat = TestimonialCatList.objects.all()
            if request.method=="POST":
                try:
                    if request.POST['mainCat']!='':
                        name = request.POST['mainCat']
                    else:
                        messages.error(request, 'Testimonial Category Required')
                        return redirect(request.META.get('HTTP_REFERER'))
                    TestimonialCatList.objects.create(name=name)
                    messages.success(request, 'Testimonial Category Created')
                    return redirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                'TestimonailManager':'menu-open', 
                'tCategory': 'active', 
                'TestimonailCat':TestimonailCat,
            }
            return render(request,"./template/tCat/TestimonailCategory.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# UPDATETestimonial Category 
# ==============================================================================
@login_required
def UpdateTestimonailCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            data = TestimonialCatList.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    mainCat = TestimonialCatList.objects.get(pk=pk)
                    if request.POST['maincatName']!='':
                        if len(request.POST['maincatName'])<50:
                            name = request.POST['maincatName']
                            newname = name.lower()
                            mainCat.name = request.POST['maincatName']
                            mainCat.slug = newname.replace(" ", "-")
                            mainCat.save()
                        else:
                            messages.error(request, 'Category Name Less 50 Char')
                            return redirect(request.META.get('HTTP_REFERER'))
                        if request.FILES['img']!='':
                            mainCat.img = request.FILES['img']
                            mainCat.last_update = datetime.date.today()
                            mainCat.save()
                            messages.success(request, 'Update successfully')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, 'Category Name is Empty')
                        return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    mainCat.img = TestimonialCatList.objects.get(pk=pk).img
                    mainCat.last_update = datetime.date.today()
                    mainCat.save()
                    messages.success(request, 'Update successfully')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                'Category':'menu-open', 
                'TestimonailCategory': 'active', 
                'data':data
                }
            return render(request,"./template/update-TestimonialCatList.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETETestimonial Category 
# ==============================================================================
@login_required
def DeleteTestimonailCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialCatList.objects.filter(pk=pk).delete()
                messages.success(request, 'Delete successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404

# ==============================================================================
# ACTIVATETestimonial Category 
# ==============================================================================
@login_required
def ActivatedTestimonailCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialCatList.objects.filter(pk=pk).update(is_active = True)
                messages.success(request, 'Activated successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DEACTIVATEDTestimonial Category 
# ==============================================================================
@login_required
def DeactivatedTestimonailCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialCatList.objects.filter(pk=pk).update(is_active = False)
                messages.error(request, 'Deactivated successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# MORE ACCTIONS
# ==============================================================================