from django.contrib.auth.decorators import login_required
from AdminAuthentication.models import AdminRegistration
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TestimonialCatList, TestimonialList
from django.http import Http404
import datetime
import random
import datetime
from django.contrib.auth.decorators import login_required
from AdminAuthentication.models import AdminRegistration
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.http import Http404
import random
from django.urls import reverse
from urllib.parse import urlencode

@method_decorator(login_required, name='dispatch')
class ALLTestimonialList(ListView):
    paginate_by = 5
    template_name = './template/testimonail/testimonailSTATUS.html'
    ordering = ['id'] 
    extra_context = { 'TestimonailManager':'menu-open', 'TestimonailListActive': 'active'}
    context_object_name = 'TestimonailList'

    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')
        if is_draft == 'True':
            return TestimonialList.objects.filter(is_active=False, is_verified=False, is_draft=True)
        elif is_verified == 'True':
            print('is_verified', is_verified)
            return TestimonialList.objects.filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False)
        elif is_active == 'False':
            return TestimonialList.objects.filter(is_active=False, is_verified=True, is_draft=False).exclude(is_deleted=True)
        elif is_deleted == 'True':
            print('is_deleted', is_deleted)
            return TestimonialList.objects.filter(is_deleted=True)
        else:
            return TestimonialList.objects.all()

# ==============================================================================
# CREATETestimonial Category  
# ==============================================================================
@login_required
def CreateTestimonail(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            TestimonailCat = TestimonialCatList.objects.filter(is_active=True)
            if request.method=="POST":
                try:
                    if request.POST.get('name')!='':
                        name = request.POST.get('name')
                    else:
                        messages.error(request, 'Testimonial Category Required')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.POST.get('ratting')!='':
                        ratting = request.POST.get('ratting')
                    else:
                        messages.error(request, 'Ratting Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                
                    if request.FILES.get('img')!='':
                        img = request.FILES.get('img')
                    else:
                        messages.error(request, 'IMG Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.POST.get('description')!='':
                        description = request.POST.get('description')
                        TestimonialList.objects.create(name=name, ratting=ratting, img=img, description=description)
                        messages.success(request, 'Testimonial Created')
                        # messages.success(request, 'Created Successfully')
                        base_url = reverse('TestimonailList')  
                        query_string =  urlencode({'is_draft': True}) 
                        url = '{}?{}'.format(base_url, query_string) 
                        return redirect(url)
                
                    else:
                        messages.error(request, 'Description Required*')             
                        return redirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                'TestimonailManager':'menu-open', 
                'CreateTestimonail': 'active', 
                'TestimonailCat':TestimonailCat,
            }
            return render(request,"./template/testimonail/createTestimonail.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# UPDATETestimonial Category 
# ==============================================================================
@login_required
def updateTestimonail(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonailCat = TestimonialCatList.objects.filter(is_active=True)
                Testimonail = TestimonialList.objects.get(pk=pk)
                if request.method=="POST":
                    if request.POST.get('mainCat')!='':
                        Testimonail.tCat_id = request.POST.get('mainCat')
                        Testimonail.save()
                    else:
                        messages.error(request, 'Testimonial Category Required')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.POST.get('name')!='':
                        Testimonail.name = request.POST.get('name')
                        Testimonail.save()
                    else:
                        messages.error(request, 'Testimonial Category Required')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.POST.get('ratting')!='':
                        Testimonail.ratting = request.POST.get('ratting')
                        Testimonail.save()
                    else:
                        messages.error(request, 'Ratting Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                
                    if request.FILES.get('img'):
                        Testimonail.img = request.FILES.get('img')
                        Testimonail.save()

                    if request.POST.get('description')!='':
                        Testimonail.description = request.POST.get('description')
                        Testimonail.save()
                        messages.success(request, 'Updated Successfully')
                        # return redirect(request.META.get('HTTP_REFERER'))
                        base_url = reverse('TestimonailList')  
                        query_string =  urlencode({'is_active': False}) 
                        url = '{}?{}'.format(base_url, query_string) 
                        return redirect(url)
                
                    else:
                        messages.error(request, 'Description Required*')             
                        return redirect(request.META.get('HTTP_REFERER'))
                context = {
                    'TestimonailManager':'menu-open', 
                    'Testimonail': 'active', 
                    'TestimonailCat':TestimonailCat,
                    'Testimonial':Testimonail,
                    }
                return render(request,"./template/testimonail/updateTestimonail.html", context)
            except Exception:
                messages.error(request, 'Error Occured*')             
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETETestimonial Category 
# ==============================================================================
@login_required
def DeleteTestimonail(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialList.objects.filter(pk=pk).update(is_deleted = True, is_active=False, is_draft=False)
                messages.success(request, 'Deleted Successfully')
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
def ActivatedTestimonail(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialList.objects.filter(pk=pk).update(is_active = True,is_verified=True, is_draft=False)
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
def DeactivatedTestimonail(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialList.objects.filter(pk=pk).update(is_active = False, is_draft=False)
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
# DEACTIVATEDTestimonial Category 
# ==============================================================================
@login_required
def PermanentlyDeleteTestimonail(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialList.objects.filter(pk=pk).delete()
                messages.success(request, 'Permanently Deleted')
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
def RestoreTestimonail(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                TestimonialList.objects.filter(pk=pk).update(is_deleted = False, is_active=False, is_draft=False)
                messages.success(request, 'Restore Successfully')
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