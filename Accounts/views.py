from SALESManager.HELPERS import OrderPriceDetails, get_orders
from SALESManager.models import ProductOrderList
from Accounts.access import user_login_required
from django.shortcuts import render, redirect
from RCRManager.models import RCRREQUESTList
from django.contrib import messages

@user_login_required()
def ViewConfirmOrder(request, orderId):
    try:
        if request.user.token == request.session['token']:
            status, objs = get_orders(request, orderId)
            if status =="single":
                context = {
                    'obj':objs ,
                    'status':"single" ,
                }
            else:
                subtotal, shipping, discount, total, all_orders= OrderPriceDetails(request, objs)
                context = {
                    'all_orders':all_orders ,
                    'date':all_orders[0].date,
                    'orderId':all_orders[0].orderId,
                    'subtotal': subtotal,
                    'ShippingTotal': shipping,
                    'discount': discount,
                    'total': total,
                    'status':"miltiple" ,
                }
            return render(request,"./template/ViewConfirmOrder.html", context )
        else:
            messages.error(request, 'Please Login First')
            return redirect("/")
    except Exception as e:
        print("Error===========>", e)
        messages.error(request, 'Please Login First')
        return redirect("LOGOUTUSER")
