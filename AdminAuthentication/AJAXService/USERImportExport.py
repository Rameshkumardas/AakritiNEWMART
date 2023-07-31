from AdminAuthentication.decorators import admin_required, manager_required, superadmin_required
from AdminAuthentication.models import AdminActivity, AdminRegistration
from ..utils import USERListResource
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from tablib import Dataset
@superadmin_required
def USERImport(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            try:
                if request.method == 'POST':
                    file_format = request.POST.get('fileformatIMPORT')
                    USER = USERListResource()                
                    dataset = Dataset()
                    getIMPORT_DATA = request.FILES.get('importData')                
                    if file_format == 'CSV':
                        data = dataset.load(getIMPORT_DATA.read().decode('utf-8'), format='csv')
                        USER.import_data(data, dry_run=False)   
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ CSV USER LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'CSV Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'JSON':
                        getJSON = dataset.load(getIMPORT_DATA.read().decode('utf-8'),format='json')
                        USER.import_data(getJSON, dry_run=False) 
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ JSON USER LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'JSON Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'XLS (Excel)':
                        data = dataset.load(getIMPORT_DATA.read())
                        USER.import_data(data, dry_run=False)
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ CSV USER LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'Excel Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    else:
                        return JsonResponse({'status':0, 'message':'No Request'})
                else:
                    return JsonResponse({'status':0, 'message':'Bad Request'})
            except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})

@superadmin_required
def USERExport(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            USER = USERListResource()
            if request.method == 'POST':
                queryset = AdminRegistration.objects.filter(is_user=True).exclude(is_accountant=True)        
                dataset = USER.export(queryset)
                file_format = request.POST['fileformat']
                if file_format == 'CSV':
                    response = HttpResponse(dataset.csv, content_type='text/csv')
                    response['Content-Disposition'] = f'attachment; filename="CSV_USER_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.csv"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ CSV USER LIST ] - Exported<span>')
                    return response

                elif file_format == 'JSON':
                    response = HttpResponse(dataset.json, content_type='application/json')
                    response['Content-Disposition'] = f'attachment; filename="JSON_USER_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON USER LIST ] - Exported<span>')
                    return response                
                elif file_format == 'XLS (Excel)':
                    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
                    response['Content-Disposition'] = f'attachment; filename="EXCEL_USER_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.xls"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ EXCEL USER LIST ] - Exported<span>')
                    return response  
                else:
                    response = HttpResponse(dataset.json, content_type='application/json')
                    response['Content-Disposition'] = f'attachment; filename="JSON_USER_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON USER LIST ] - Exported<span>')
                    return response
            else:
                response = HttpResponse(dataset.json, content_type='application/json')
                response['Content-Disposition'] = f'attachment; filename="JSON_USER_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON USER LIST ] - Exported<span>')
                return response   
        else:
            return HttpResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return HttpResponse({'status':0, 'message':'Bad Request'})
    



