
from PRODUCTManager.models import ProductMyCart
from Accounts.access import user_login_required

def MyCartList(request):
    if request.session.has_key('KHANTAILORusername'):
        return {'mycartlist': ProductMyCart.objects.filter(user_id=request.user.pk) }
    else:
        return {'mycartlist': '404' }

def CountMyCart(request):
    if request.session.has_key('KHANTAILORusername'):
        return {'countMyCart': ProductMyCart.objects.filter(user_id=request.user.pk).count()}
    else:
        return {'countMyCart': '' }
        

