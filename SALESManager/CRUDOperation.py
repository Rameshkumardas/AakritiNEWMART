from datetime import datetime
from django.http import Http404
from django.shortcuts import render, redirect
from AdminAuthentication.models import AdminRegistration
from django.contrib import messages
import random
from SALESManager.models import ProductOrderList
from PRODUCTManager.models import ProductList, ProductMyCart, OfferList

def MoveToTrash(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.is_deleted = True
                order.is_confirmed = False

                order.save()
                messages.success(request, 'Move To Trash')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404    


def RestoreFromTrash(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.is_deleted = False
                order.is_confirmed = True
                order.save()
                messages.success(request, 'Restore From Trash')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404 
def deleteORDER(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.delete()
                messages.success(request, 'Order Deleted')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404


def confirmORDER(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.is_confirmed = True
                order.save()
                messages.success(request, 'Order Confirmed')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404


def shippedORDER(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.is_shipped = True
                order.track = 'https://www.aakriticms.com/'
                # order.track = 'https://www.hubneticstore.com/track'
                order.save()
                messages.success(request, 'Order Shipped - D')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404


def CancelORDER(request, pk):
    if request.session.has_key('KHANTAILORusername') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.is_cancel = True
                order.save()
                messages.success(request, 'Order Cancel')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Order DoesNotExist')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Order DoesNotExist')
        return redirect(request.META.get('HTTP_REFERER'))
    



def OnTheWayORDER(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.is_way = True
                order.save()
                messages.success(request, 'Order Cancel')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
    

def deliveredORDER(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            try:
                order = ProductOrderList.objects.get(pk=pk)
                order.is_delivered = True
                order.on_delivered = datetime.now().strftime("%d/%m/%Y %H:%M %p")
                order.save()
                messages.success(request, 'Order Cancel')
                return redirect(request.META.get('HTTP_REFERER'))
            except ProductOrderList.DoesNotExist:
                messages.error(request, 'Order DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404

