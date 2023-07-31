from django.contrib.auth.decorators import login_required
from PRODUCTManager.models import ProductMyCart, ProductMyWishlist




def allWISHCOUNT(request):
    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
        allMyWish = ProductMyWishlist.objects.select_related('product', 'user').filter(user_id=request.user.pk).count()
        context = {
            'allWISHCOUNT': allMyWish
            }
        return context
    else:
        context = {
            'allWISHCOUNT': 0
            }
        return context

def allCARTCOUNT(request):
    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
        allMyCART = ProductMyCart.objects.select_related('product', 'user').filter(user_id=request.user.pk).count()
        context = {            
            'allCARTCOUNT': allMyCART
            }
        return context
    else:
        context = {            
            'allCARTCOUNT': 0
            }
        return context

def allCARTList(request):
    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
        allCART = ProductMyCart.objects.select_related('product', 'user').filter(user_id=request.user.pk)
        context = {            
            'allCART': allCART
            }
        return context
    else:
        context = {            
            }
        return context
    

