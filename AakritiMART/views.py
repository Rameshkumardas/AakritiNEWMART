from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from AakritiMART.shippingGST import getGST, getSHIPPING
from Accounts.models import shippingADDRESS
from BLOGManager.models import BLOGList, allBLOGCOMMENTS
from CommonModules.models import COLORList
from PRODUCTManager.models import COMPAREProducts, PRODUCTQList, ProductList, ProductMyCart, ProductMyWishlist, ProductRatting

from SLIDERManager.models import BANNERList
from CATEGORYManager.models import MainCategory
from django.db.models import Q
# ==============================================================================
# CREATE MAIN Country  
# ==============================================================================

def AakritiMART(request):  
    
    try:
        context = {
            'new_arrivals_20_rows':ProductList.new_arrivals_20_rows(),
            'trending_new_20_rows':ProductList.trending_new_20_rows(),
            'trending_featured_20_rows':ProductList.trending_featured_20_rows(),
            'trending_top_sale_20_rows':ProductList.trending_top_sale_20_rows(),
            'deal_20_rows':ProductList.deal_20_rows(),
            'discount_20_rows':ProductList.discount_20_rows(),
            'featured_20_rows':ProductList.featured_20_rows(),
            'selling_20_rows':ProductList.selling_20_rows(),
        }
        return render(request,"./template/home/index.html", context)

    except Exception as e:
        print(e)
        pass
    
    
    
def allProducts(request):
    q = request.GET.get('q')
    mainCat = request.GET.get('mainCat')
    if q and mainCat:
        posts_list = ProductList.all_product_rows().filter(Q(name__icontains=q)).filter(mainCat_id=mainCat).order_by('-last_update')
    elif q:
        posts_list = ProductList.all_product_rows().filter(Q(name__icontains=q)).order_by('-last_update')
    else:
        posts_list = ProductList.all_product_rows().order_by('-last_update')

    try:
        page = request.GET.get('page', 1)
        filter = request.GET.get('filter')
        if filter:
            paginator = Paginator(posts_list, filter)
        else:
            paginator = Paginator(posts_list, 10)
        allPRODUCTS = paginator.page(page)
    except PageNotAnInteger:
        allPRODUCTS = paginator.page(1)
    except EmptyPage:
        allPRODUCTS = paginator.page(paginator.num_pages)

    context = {
        'ProductList':allPRODUCTS,
    }
    return render(request,"./template/home/productlist.html", context)


def mainCatProductList(request, slug):
    try:
        posts_list = ProductList.objects.select_related('mainCat', 'subCat', 'SubSubCat', 'author', 'brand', 'color').filter(mainCat__slug=slug).filter(is_active=True, is_verified=True)
        
        try:
            page = request.GET.get('page', 1)
            filter = request.GET.get('filter')
            if filter:
                paginator = Paginator(posts_list, filter)
            else:
                paginator = Paginator(posts_list, 10)
            allPRODUCTS = paginator.page(page)
        except PageNotAnInteger:
            allPRODUCTS = paginator.page(1)
        except EmptyPage:
            allPRODUCTS = paginator.page(paginator.num_pages)

        context = {
            'ProductList':allPRODUCTS,
        }
        return render(request,"./template/home/productlist.html", context)
    except Exception as e:
        messages.success(request, "Error occured")
        return redirect('/')


def subCatProductList(request, main_slug=None, slug=None):
    try:
        posts_list = ProductList.objects.select_related('mainCat', 'subCat', 'SubSubCat', 'author', 'brand', 'color').filter(subCat__slug=slug).filter(is_active=True, is_verified=True)
        try:
            page = request.GET.get('page', 1)
            filter = request.GET.get('filter')
            if filter:
                paginator = Paginator(posts_list, filter)
            else:
                paginator = Paginator(posts_list, 10)
            allPRODUCTS = paginator.page(page)
        except PageNotAnInteger:
            allPRODUCTS = paginator.page(1)
        except EmptyPage:
            allPRODUCTS = paginator.page(paginator.num_pages)
        
        context = {
            'ProductList':allPRODUCTS,
        }
        return render(request,"./template/home/productlist.html", context)
    except Exception as e:
        messages.success(request, "Error occured")
        return redirect('/')
    
def SubSubCatProductList(request, main_slug=None, sub_slug=None, slug=None):
    try:
        posts_list = ProductList.objects.select_related('mainCat', 'subCat', 'SubSubCat', 'author', 'brand', 'color').filter(SubSubCat__slug=slug).filter(is_active=True, is_verified=True)
        try:
            page = request.GET.get('page', 1)
            filter = request.GET.get('filter')
            if filter:
                paginator = Paginator(posts_list, filter)
            else:
                paginator = Paginator(posts_list, 10)
            allPRODUCTS = paginator.page(page)
        except PageNotAnInteger:
            allPRODUCTS = paginator.page(1)
        except EmptyPage:
            allPRODUCTS = paginator.page(paginator.num_pages)

        context = {
            'ProductList':allPRODUCTS,
        }
        return render(request,"./template/home/productlist.html", context)
    except Exception as e:
        messages.success(request, "Error occured")
        return redirect('/')
# ==============================================================================
# CREATE MAIN Country  
# ==============================================================================
def OPENProduct(request, slug):
    try:
        product = ProductList.objects.get(slug=slug)
        # ==================================================================================
        # ==================================================================================
        posts_list = ProductRatting.objects.select_related('product', 'user').filter(product_id=product.pk).order_by('-date')
        try:
            page = request.GET.get('page', 1)
            filter = request.GET.get('filter')
            if filter:
                paginator = Paginator(posts_list, filter)
            else:
                paginator = Paginator(posts_list, 5)
            RATTINGList = paginator.page(page)
        except PageNotAnInteger:
            RATTINGList = paginator.page(1)
        except EmptyPage:
            RATTINGList = paginator.page(paginator.num_pages)
            
        _ratting1 = posts_list.select_related('product', 'user').filter(Ratting=1).count()
        _ratting2 = posts_list.select_related('product', 'user').filter(Ratting=2).count()
        _ratting3 = posts_list.select_related('product', 'user').filter(Ratting=3).count()
        _ratting4 = posts_list.select_related('product', 'user').filter(Ratting=4).count()
        _ratting5 = posts_list.select_related('product', 'user').filter(Ratting=5).count()
        _total_ratting = posts_list.select_related('product', 'user').count()
                
        if _total_ratting:
            _total_ratting = _total_ratting
        else:
            _total_ratting = 1
        
        if _ratting1:
            RATTING1 =  (_ratting1/_total_ratting)*100
        else:
            RATTING1 = 0
            
        if _ratting2:
            RATTING2 = (_ratting2/_total_ratting)*100
        else:
            RATTING2 = 0
            
        if _ratting3:        
            RATTING3 = (_ratting3/_total_ratting)*100
        else:
            RATTING3 = 0
            
        if _ratting4:
            RATTING4 = (_ratting4/_total_ratting)*100
        else:
            RATTING4 = 0
            
        if _ratting5:
            RATTING5 = (_ratting5/_total_ratting)*100
        else:
            RATTING5 = 0
        
        if _ratting1+_ratting2+_ratting3+_ratting4+_ratting5:
            Avarage = (5/int(_ratting1+_ratting2+_ratting3+_ratting4+_ratting5))
        else:
            Avarage = 0
        # ==================================================================================
        # ==================================================================================

        # ==================================================================================
        # ==================================================================================
        QA_posts_list = PRODUCTQList.objects.filter(product_id=product.pk).order_by('-date')
        try:
            page = request.GET.get('qa_page', 1)
            paginator = Paginator(QA_posts_list, 5)
            allPRODUCTQlist = paginator.page(page)
        except PageNotAnInteger:
            allPRODUCTQlist = paginator.page(1)
        except EmptyPage:
            allPRODUCTQlist = paginator.page(paginator.num_pages)
        # ==================================================================================
        # ==================================================================================

        
        context = {
            'allQA':QA_posts_list.count(),
            'allPRODUCTQlist':allPRODUCTQlist,
            'total_ratting':_total_ratting,
            'Avarage':Avarage,
            'RATTING1':RATTING1,
            'RATTING1':RATTING1,
            'RATTING2':RATTING2,
            'RATTING3':RATTING3,
            'RATTING4':RATTING4,
            'RATTING5':RATTING5,
            
            'product':product,
            'RATTINGList':RATTINGList,
        }
        return render(request,"./template/home/view.html", context)
    except Exception as e:
        print(e)
        messages.success(request, f"{e} Error occured")
        return redirect('/')

# ==============================================================================
# COMPARE AakritiMART 
# ==============================================================================
@login_required
def CompareMART(request):
    try:
        allCOMPAREProducts = COMPAREProducts.objects.filter(user_id=request.user.pk)
        context = {
            'allCOMPAREProducts':allCOMPAREProducts,
        }
        return render(request,"./template/home/compare.html", context)
    except Exception:
        messages.success(request, "Error occured")
        return redirect('/')
# ==============================================================================
# WISHLIST AakritiMART 
# ==============================================================================
@login_required
def WishlistMART(request):
    try:
        myWishlist = ProductMyWishlist.objects.filter(user_id=request.user.pk)
        context = {
            'myWishlist':myWishlist,
        }
        return render(request,"./template/home/wishlist.html", context)
    except Exception:
        pass

# ==============================================================================
# MY Cart AakritiMART 
# ==============================================================================
@login_required
def MYCart(request):
    try:
        allCART = ProductMyCart.objects.filter(user_id= request.user.pk)
        context = {
            'allCART':allCART,
        }
        return render(request,"./template/home/cart.html", context)
    except Exception:
        pass
# ==============================================================================
# MY Cart AakritiMART 
# ==============================================================================
def CheckOut(request):
    checkoutFor = request.GET.get('checkoutFor')
    print("myCartList", checkoutFor)
    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
        if (checkoutFor == 'singleProduct'):
            try:    
                slug = request.GET.get('product')
                qty = int(request.GET.get('qty'))
                product = ProductList.objects.get(is_active=True, slug=slug)
                # GSTTotal = getGST(request.session['PinCode'], product.pk, qty)
                # ShippingTotal = getSHIPPING(request.session['PinCode'], product.pk, qty)    
                GSTTotal = 10
                ShippingTotal = 10 


                subTotal = (product.sp*qty)
                Total = subTotal+GSTTotal+ShippingTotal
                discount = (product.mrp*qty) - (product.sp*qty)
                
                # if ProductMyCart.objects.filter(user_id=request.user.pk, product_id=product.pk).exists():
                #     update = ProductMyCart.objects.get(user_id=request.user.pk, product_id=product.pk)
                #     update.qty=update.qty + 1
                #     update.save()
                # else:
                #     ProductMyCart.objects.create(user_id=request.user.pk, product_id=product.pk)
                
                context = {                                
                    'allSHIPPINGS':shippingADDRESS.objects.filter(user_id=request.user.pk),
                    'allBILLINGS':billingADDRESS.objects.filter(user_id=request.user.pk),
                    'product': product,
                    'subTotal': subTotal,
                    'GSTTotal': GSTTotal,
                    'ShippingTotal': ShippingTotal,
                    'total': float(Total),
                    'discount': discount,
                }
                return render(request,"./template/home/checkout.html", context)
            except Exception as e:
                print(e)
                messages.error(request, f'PinCode Not Valid')
                return redirect(request.META.get('HTTP_REFERER'))
        elif (checkoutFor == 'myCartList'):
            try:    
                CartList = ProductMyCart.objects.filter(user_id=request.user.pk)                
                SubTotal = []
                grandSHIPING = []
                grandGST = []
                grandDISCOUNT = []

                for cart in CartList:
                    SubTotal.append((cart.product.sp)*int(cart.qty))
                    # totalSHIPPING = getSHIPPING(request.session['PinCode'], cart.product.pk, cart.qty)    
                    # totalGST = getGST(request.session['PinCode'], cart.product.pk, cart.qty)
                    totalSHIPPING = 10
                    totalGST = 10                     
                    grandSHIPING.append(totalSHIPPING)            
                    grandGST.append(totalGST)
                    grandDISCOUNT.append(((cart.product.mrp)*int(cart.qty))-((cart.product.sp)*int(cart.qty)))
                
                context = {                                
                    'allSHIPPINGS':shippingADDRESS.objects.filter(user_id=request.user.pk).order_by('-date'),
                    'CartList': CartList,
                    'subTotal': sum(SubTotal),
                    'GSTTotal': sum(grandGST),
                    'ShippingTotal': sum(grandSHIPING),
                    'total': sum(SubTotal+grandGST+grandSHIPING),
                    'discount': sum(grandDISCOUNT),
                }
                return render(request,"./template/home/checkout.html", context)
            except Exception as e:
                print(e)
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        try:
            slug = request.GET.get('product')
            qty = int(request.GET.get('qty'))

            if qty !=None and  qty!='':
                qty = qty
            else:
                qty=1

            product = ProductList.objects.get(is_active=True, slug=slug)
            request.session['product'] = product.pk
            
            # GSTTotal = getGST(request.session['PinCode'], product.pk, qty)
            # ShippingTotal = getSHIPPING(request.session['PinCode'], product.pk, qty)   
            
            GSTTotal = 10
            ShippingTotal = 10  
                   
            subTotal = (product.sp*qty)
            Total = subTotal+GSTTotal+ShippingTotal
            discount = product.mrp*qty - product.sp*qty
            context = {
                'product': ProductList.objects.filter(is_active=True),
                'product': product,
                'subTotal': subTotal,
                'GSTTotal': GSTTotal,
                'ShippingTotal': ShippingTotal,
                'total': Total,
                'discount': discount,
            }    
            return render(request,"./template/home/checkout.html", context)

        except Exception as e:
            print(e)
            messages.error(request, f'{e}')
            return redirect('/')
        



# ==============================================================================
# DIR SETTINGS
# ==============================================================================
def QUICKView(request):
    target = request.POST.get('targetVAL')
    try:
        product = ProductList.objects.get(pk=target)
        print(product)
        context = {
            'product':product,
        }
        return render(request,"template/includes/quickVIEW.html", context)
    except Exception as e:
        print(e)
        # messages.error(request, 'Error Occured')
        # return redirect(request.META.get('HTTP_REFERER'))







# DIR SETTINGS
# ==============================================================================
def ContactUs(request):
    try:
        return render(request,"template/home/contact-us.html")
    except Exception as e:
        print(e)
        messages.error(request, 'Error Occured')
        return redirect(request.META.get('HTTP_REFERER'))

# ==============================================================
# MORE OPERATION
# ==============================================================
def LoadBLOGSubCatLIST(request):
    context = {
        'product': ProductList.objects.get(mainCat_id=request.POST['mainCat'], is_active=True)
    }
    return render(request, './template/blogSubCategoryList.html', context)

