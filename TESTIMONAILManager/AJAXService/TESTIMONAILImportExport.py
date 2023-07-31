from AdminAuthentication.decorators import admin_required, manager_required
from AdminAuthentication.models import AdminActivity
from django.http import HttpResponse, JsonResponse
from TESTIMONAILManager.models import TestimonialList
from ..utils import TESTIMONAILListResource
from django.shortcuts import redirect
from django.contrib import messages
from datetime import datetime
from tablib import Dataset
@manager_required
def TESTIMONAILImport(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                if request.method == 'POST':
                    file_format = request.POST.get('fileformatIMPORT')
                    TESTIMONAIL = TESTIMONAILListResource()                
                    dataset = Dataset()
                    getIMPORT_DATA = request.FILES.get('importData')                
                    if file_format == 'CSV':
                        data = dataset.load(getIMPORT_DATA.read().decode('utf-8'), format='csv')
                        TESTIMONAIL.import_data(data, dry_run=False)   
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ CSV TESTIMONAIL LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'CSV Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'JSON':
                        getJSON = dataset.load(getIMPORT_DATA.read().decode('utf-8'),format='json')
                        TESTIMONAIL.import_data(getJSON, dry_run=False) 
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ JSON TESTIMONAIL LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'JSON Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'XLS (Excel)':
                        data = dataset.load(getIMPORT_DATA.read())
                        TESTIMONAIL.import_data(data, dry_run=False)
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ CSV TESTIMONAIL LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'Excel Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                else:
                    return JsonResponse({'status':0, 'message':'Bad Request'})
            except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})

@admin_required
def TESTIMONAILExport(request, *kwargs):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin and request.user.token == request.session['token']:
            try:
                if request.method == 'POST':
                    is_draft = request.GET.get('is_draft')
                    is_verified = request.GET.get('is_verified')
                    is_active = request.GET.get('is_active')
                    is_deleted = request.GET.get('is_deleted')  
                    if is_draft == 'True':
                        queryset = TestimonialList.objects.filter(is_draft=True).exclude(is_deleted=True)
                    elif is_verified == 'True':
                        queryset = TestimonialList.objects.filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False)
                    elif is_active == 'False':
                        queryset = TestimonialList.objects.filter(is_active=False, is_verified=True, is_draft=False).exclude(is_deleted=True)
                    elif is_deleted == 'True':
                        queryset = TestimonialList.objects.filter(is_deleted=True)
                    else:
                        queryset = TestimonialList.objects.all()
            
                    dataset = TESTIMONAILListResource().export(queryset)

                    file_format = request.POST['fileformat']
                    if file_format == 'CSV':
                        response = HttpResponse(dataset.csv, content_type='text/csv')
                        response['Content-Disposition'] = f'attachment; filename="CSV_TESTIMONAIL_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.csv"'
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ CSV TESTIMONAIL LIST ] - Exported<span>')
                        return response

                    elif file_format == 'JSON':
                        response = HttpResponse(dataset.json, content_type='application/json')
                        response['Content-Disposition'] = f'attachment; filename="JSON_TESTIMONAIL_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON TESTIMONAIL LIST ] - Exported<span>')
                        return response                
                    elif file_format == 'XLS (Excel)':
                        response = HttpResponse(dataset.xls, content_type='application/ms-excel')
                        response['Content-Disposition'] = f'attachment; filename="EXCEL_TESTIMONAIL_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.xls"'
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ EXCEL TESTIMONAIL LIST ] - Exported<span>')
                        return response
                    else:
                        response = HttpResponse(dataset.json, content_type='application/json')
                        response['Content-Disposition'] = f'attachment; filename="JSON_TESTIMONAIL_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON TESTIMONAIL LIST ] - Exported<span>')
                        return response
                else:
                    messages.error(request, 'Select File')
                    return redirect(request.META.get('HTTP_REFERER'))
          
            except Exception as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Access')
        return redirect(request.META.get('HTTP_REFERER'))
    



