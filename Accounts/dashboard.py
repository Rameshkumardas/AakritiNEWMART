from Accounts.models import shippingADDRESS
from SALESManager.models import ProductOrderList
from Accounts.access import user_login_required
from django.shortcuts import render, redirect
from RCRManager.models import RCRREQUESTList
from django.contrib import messages

# ViewConfirmOrder.html

@user_login_required()
def Dashboard(request):
    try:
        if request.user.token == request.session['token']:
            all_my_orders = ProductOrderList.objects.select_related('user', 'product').filter(user=request.user).order_by('-id')
            allSHIPPING = shippingADDRESS.objects.filter(user=request.user)

            context = {
                'dashboard':'menu-open', 
                'all_my_orders':all_my_orders,
                'allSHIPPINGS': allSHIPPING,

            }
            return render(request,"./template/USERDashboard.html", context )
        else:
            messages.error(request, 'Please Login First')
            return redirect("/")
    except Exception as e:
        print(e)
        messages.error(request, 'Please Login First')
        return redirect("LOGOUTUSER")


@user_login_required()
def Address(request):
    try:
        if request.user.token == request.session['token']:
            
            allSHIPPING = shippingADDRESS.objects.filter(user=request.user)
            context = {
                'allSHIPPINGS': allSHIPPING,
                'address': 'active'
            }
            return render(request,"./template/account/dashboard/address.html", context )
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    
    except Exception as e:
        print(e)
        messages.error(request, 'Please Login First')
        return redirect("LOGOUTUSER")

@user_login_required()
def Orders(request):
    try:
        if request.user.token == request.session['token']:
            
            allORDERList = ProductOrderList.objects.filter(user=request.user)
            context = {
                'ODERList': allORDERList,
                'orders': 'active'
            }
            return render(request,"./template/account/dashboard/orders.html", context )
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    
    except Exception as e:
        print(e)
        messages.error(request, 'Please Login First')
        return redirect("LOGOUTUSER")


@user_login_required()
def OrderConfirm(request, OrderId):
    try:
        if request.user.token == request.session['token']:
            allORDERList = ProductOrderList.objects.filter(user=request.user)
            context = {
                'ODERList': allORDERList,
                'orders': 'active'
            }
            return render(request,"./template/account/dashboard/orders.html", context )
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    
    except Exception as e:
        print(e)
        messages.error(request, 'Please Login First')
        return redirect("LOGOUTUSER")


@user_login_required()
def cancelORDER(request, pk):
    if request.user.token == request.session['token']:
        try:
            order = ProductOrderList.objects.get(pk=pk)
            order.is_cancel=True
            order.is_confirmed=False
            order.save()
            
            RCRREQUESTList.objects.create(order_id=pk, is_cancel=True)

            # RCRREQUESTList.objects.create(product_id=order.product.pk, user=order.user, is_cancel=True)
            messages.success(request, 'Order Cancel Successfully')
            return redirect(request.META.get('HTTP_REFERER'))
        except ProductOrderList.DoesNotExist:
            messages.error(request, 'Order DoesNotExist')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Access')
        return redirect(request.META.get('HTTP_REFERER'))
 
 
@user_login_required()
def returnORDER(request, pk):
    if request.user.token == request.session['token']:
        try:
            order = ProductOrderList.objects.get(pk=pk)
            order.is_confirmed=True
            order.is_shipped=False
            order.save()
            RCRREQUESTList.objects.create(order_id=pk, is_cancel=True)
            messages.success(request, 'Order Cancel Successfully')
            return redirect(request.META.get('HTTP_REFERER'))
        except ProductOrderList.DoesNotExist:
            messages.error(request, 'Order DoesNotExist')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Access')
        return redirect(request.META.get('HTTP_REFERER'))