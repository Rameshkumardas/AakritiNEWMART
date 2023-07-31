from AdminAuthentication.decorators import admin_required, manager_required
from AdminAuthentication.models import AdminActivity
from ..utils import COLORListResource
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from tablib import Dataset

@manager_required
def COLORImport(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                if request.method == 'POST':
                    file_format = request.POST.get('fileformatIMPORT')
                    COLOR = COLORListResource()                
                    dataset = Dataset()
                    getIMPORT_DATA = request.FILES.get('importData')                
                    if file_format == 'CSV':
                        data = dataset.load(getIMPORT_DATA.read().decode('utf-8'), format='csv')
                        COLOR.import_data(data, dry_run=False)
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ CSV  COLOR LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'CSV Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'JSON':
                        getJSON = dataset.load(getIMPORT_DATA.read().decode('utf-8'),format='json')
                        COLOR.import_data(getJSON, dry_run=False) 
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ JSON  COLOR LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'JSON Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'XLS (Excel)':
                        data = dataset.load(getIMPORT_DATA.read())
                        COLOR.import_data(data, dry_run=False)
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ EXCEL  COLOR LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'Excel Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})

                    else:
                        getJSON = dataset.load(getIMPORT_DATA.read().decode('utf-8'),format='json')
                        COLOR.import_data(getJSON, dry_run=False) 
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ JSON  COLOR LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'JSON Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                else:
                    return JsonResponse({'status':0, 'message':'Bad Request'})
            except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})

@admin_required
def COLORExport(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin and request.user.token == request.session['token']:
            dataset = COLORListResource().export()
            if request.method == 'POST':
                file_format = request.POST['fileformat']
                if file_format == 'CSV':
                    response = HttpResponse(dataset.csv, content_type='text/csv')
                    response['Content-Disposition'] = f'attachment; filename="CSV__COLOR_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.csv"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ CSV  COLOR LIST ] - Exported<span>')
                    return response
                elif file_format == 'JSON':
                    response = HttpResponse(dataset.json, content_type='application/json')
                    response['Content-Disposition'] = f'attachment; filename="JSON__COLOR_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ CSV  COLOR LIST ] - Exported<span>')
                    return response                
                elif file_format == 'XLS (Excel)':
                    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
                    response['Content-Disposition'] = f'attachment; filename="EXCEL__COLOR_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.xls"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ EXCEL  COLOR LIST ] - Exported<span>')
                    return response   
                else:
                    response = HttpResponse(dataset.json, content_type='application/json')
                    response['Content-Disposition'] = f'attachment; filename="JSON__COLOR_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ CSV  COLOR LIST ] - Exported<span>')
                    return response   
            else:
                response = HttpResponse(dataset.json, content_type='application/json')
                response['Content-Disposition'] = f'attachment; filename="JSON__COLOR_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ CSV  COLOR LIST ] - Exported<span>')
                return response   
        else:
            return HttpResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return HttpResponse({'status':0, 'message':'Bad Request'})
    



