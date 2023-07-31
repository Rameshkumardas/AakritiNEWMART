from django.conf import settings
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY, CONFIG_SMTP_SUPPORT
from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.template.loader import render_to_string
from AdminAuthentication.models import AdminActivity
from BULKEMAILManager.BULKEMAILThread import EmailThread
from .models import EMAILList, EMAILList
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from decouple import config
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from models
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
# ==============================================================
# CHAPTER LIST CLASS
# ==============================================================
@method_decorator(accountant_required, name='dispatch')
class ALLEMAILSENDSTATUSList(ListView):
    paginate_by = 50
    template_name = './template/EMAILSENDSTATUS.html'
    context_object_name = 'EMAILList'
    extra_context = { 'EMAILMarketing':'menu-open', 'allEMAILSENDSTATUS': 'active'}
    def get_queryset(self, *args, **kwargs):     
        search = self.request.GET.get('search')        
        if search:
            return EMAILList.objects.select_related('author').filter(is_sent=True).filter(Q(email__icontains=search)).order_by('-id')
        else:
            return EMAILList.objects.select_related('author').filter(is_sent=True).order_by('-id')

