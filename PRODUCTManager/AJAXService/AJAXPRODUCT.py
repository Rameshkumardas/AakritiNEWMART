from PRODUCTManager.models import ATTRIBUTEProductList, ProductList, ProductMyCart, ProductMyWishlist, ProductRatting, SIMILARPRODUCTSList
from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminActivity
from CommonModules.models import COLORList
from django.http import JsonResponse
import datetime

# ==============================================================================
# ADD NEW PRODUCT
# ==============================================================================
@accountant_required
def AddProduct(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            name = request.POST.get('name')
            mainCat = request.POST.get('mainCat')
            print("mainCat", mainCat)
            if mainCat:
                mainCat = mainCat
            else:
                return JsonResponse({'status':0, 'message':f'Main Category Required'})
            
            subCat = request.POST.get('subCat')
            if subCat:
                subCat = subCat
            else:
                return JsonResponse({'status':0, 'message':f'Sub Category Required'})
            
            SubSubCat = request.POST.get('SubSubCat')
            if SubSubCat:
                SubSubCat = SubSubCat
            else:
                SubSubCat = ''
                # return JsonResponse({'status':0, 'message':f'Sub Sub Category Required'})

            try:
                ProductList.objects.create(author_id=request.user.pk, mainCat_id=mainCat, subCat_id=subCat, SubSubCat_id=SubSubCat, name=name, is_draft=True) 
                AFTERTask = f"{request.META['HTTP_REFERER']}"
                return JsonResponse({'status':1, 'message':'Product Successfully Created', 'AFTERTask':AFTERTask})
            except Exception as e:
                print(e)
                return JsonResponse({'status':0, 'message':f'{e} Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# UPDATE PRODUCT
# ==============================================================================
@accountant_required
def UPDATEGeneralInformation(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST.get('target')
            print(target)
            try:
                product = ProductList.objects.get(pk=target)
                if (request.POST.get('name')):
                    product.name = request.POST.get('name')
                    product.save()

                mainCat = request.POST.get('mainCat')
                if mainCat:
                    product.mainCat_id = mainCat
                    product.save()
                
                subCat = request.POST.get('subCat')
                if subCat:
                    product.subCat_id = subCat
                    product.save()

                # SubSubCat = request.POST.get('SubSubCat')
                # if SubSubCat:
                #     product.SubSubCat_id = SubSubCat
                #     product.save()

                product_type = request.POST.get('product_type')
                if product_type:
                    product.product_type = product_type
                    product.save()
                
                attribute = request.POST.get('attribute')
                if attribute:
                    product.attributes = attribute
                    product.save()

                    
                brand = request.POST.get('brandname')
                if brand:
                    product.brand_id = brand
                    product.save()                 

                color = request.POST.get('color')
                if color:
                    product.color_id = color
                    product.save()

                if request.POST.get('attribute'):
                    product.attribute = request.POST.get('attribute')
                    product.save()

                if request.POST.get('CashOnDelivery'):
                    product.is_cash_on_delivery = request.POST.get('CashOnDelivery')
                    product.save()

                if(request.POST.get('Refundable')):
                    product.is_refundable = request.POST.get('Refundable')
                    product.save()

                if (request.POST.get('description')):
                    product.description = request.POST.get('description')
                    product.save()                   

                return JsonResponse({'status':1, 'message':'Update Successfully'})
            except Exception:
                return JsonResponse({'status':0, 'message': 'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# UPDATE PRODUCT

# ==============================================================================
@accountant_required
def UPDATEPriceStockGSTSHIPPING(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']: 
            target = request.POST.get('target')
            if target == '':
                return JsonResponse({'status':0, 'message':'Target Required*'})
            else:
                try:
                    product = ProductList.objects.get(pk=target)
                    ProductType = request.POST.get('ProductType')
                    if ProductType:
                        if ProductType == "Arrivals":
                            product.is_arrivals = True

                            product.is_trending = False
                            product.is_deal = False
                            product.is_discount = False
                            product.is_featured = False
                            product.is_selling = False
                                
                            product.label = "New Arrivals"
                        elif ProductType == "Trending":
                            TrendingType = request.POST.get('TrendingType')
                            if TrendingType:
                                product.is_trending = True
                                product.is_arrivals = False
                                product.is_deal = False
                                product.is_discount = False
                                product.is_featured = False
                                product.is_selling = False
                                
                                if TrendingType == "New":
                                    product.is_trending_new = True
                                    product.label = "Hot"
                                elif TrendingType == "Featured":
                                    product.is_trending_featured = True
                                    product.label = "Trending"
                                elif TrendingType == "Top Sales":
                                    product.is_trending_top_sale = True
                                    product.label = "Sale"
                            
                        elif ProductType == "Deal":
                            product.is_deal = True                            
                            product.is_discount = False
                            product.is_selling = False
                            product.is_trending = False
                            product.is_arrivals = False
                            product.is_featured = False
                            
                            product.label = ""
                        elif ProductType == "Discount":                        
                            product.is_discount = True

                            product.is_selling = False
                            product.is_trending = False
                            product.is_arrivals = False
                            product.is_deal = False
                            product.is_featured = False

                            
                            product.label = "Offer"
                        elif ProductType == "Featured":
                            product.is_featured = True
                            
                            product.is_selling = False
                            product.is_trending = False
                            product.is_arrivals = False
                            product.is_deal = False
                            product.is_discount = False
                            
                            product.label = "Featured"
                        elif ProductType == "Selling":
                            product.is_selling = True
                            product.is_trending = False
                            product.is_arrivals = False
                            product.is_deal = False
                            product.is_discount = False
                            product.is_featured = False
                                
                            product.label = "Selling"
                  
                    mrp = request.POST.get('mrp')
                    if mrp:
                        product.mrp = mrp
                    
                    sp = request.POST.get('sp')
                    if sp:
                        product.sp = sp
                    
                    total_qty = request.POST.get('totalSTOCKS')
                    if total_qty:
                        product.total_qty = total_qty
                        
                    lsw = request.POST.get('lsw')
                    if lsw:
                        product.low_stock_warning = lsw
                        
                    hsncode = request.POST.get('hsncode')
                    if hsncode:
                        product.HSNCode = hsncode
                        
                    igst = request.POST.get('igst')
                    if igst:
                        product.igst = igst
                    
                    cgst = request.POST.get('cgst')
                    if cgst:
                        product.cgst = cgst
                    
                    sgst = request.POST.get('sgst')
                    if sgst:
                        product.sgst = sgst
                        
                    dimension = request.POST.get('type')
                    if dimension:
                        product.dimension = dimension                        
                        if (dimension == 'Dimensions'):
                            product.length = request.POST.get('length')
                            product.width = request.POST.get('width')
                            product.hight = request.POST.get('hight')
                            product.weight = 0.0
                        elif (dimension == 'Weight'):
                            product.length = 0.0
                            product.width = 0.0
                            product.hight = 0.0
                            product.weight = request.POST.get('weightGM')
                    product.save()
                    return JsonResponse({'status':1, 'message': 'Updated Successfull'})
                except Exception as e:
                    print(e)
                    return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# DIR SETTINGS
# ==============================================================================
@accountant_required
def UPDATEImage(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:   
            target = request.POST['target']     
            if target == '' or target == None:
                return JsonResponse({'status':0, 'message':'Target is Not Define'})
            else:
                try:
                    product = ProductList.objects.get(pk=target)
                    img = request.FILES.get('img')
                    if (img != None and img !='undefined'):
                        product.img =img  
                    
                    img1 = request.FILES.get('img1')
                    if (img1 != None and img1 !='undefined'):
                        product.img1 =img1
                    
                    img2 = request.FILES.get('img2')
                    if (img2 != None and img2 !='undefined'):
                        product.img2 =img2
                    
                    img3 = request.FILES.get('img3')
                    if (img3 != None and img3 !='undefined'):
                        product.img3 =img3
                    
                    img4 = request.FILES.get('img4')
                    if (img4 != None and img4 !='undefined'):
                        product.img4 =img4
                    product.save()
                    return JsonResponse({'status':1, 'message': 'Updated Images'})
                except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# DIR SETTINGS
# ==============================================================================
@accountant_required
def UPDATEMetaTag(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:   
            target = request.POST['target']     
            if target == '' or target == None:
                return JsonResponse({'status':0, 'message':'Target is Not Define'})
            else:
                try:
                    product = ProductList.objects.get(pk=target)
                    
                    meta_title = request.POST.get('meta_title')
                    meta_description = request.POST.get('meta_description')
                    meta_tags = request.POST.get('meta_tags')
                    meta_img = request.FILES.get('meta_img')
                    if (meta_img != None and meta_img !='undefined'):
                        product.meta_img =meta_img                 
                    product.meta_title = meta_title
                    product.meta_description = meta_description
                    product.meta_tags = meta_tags
                    product.last_update = datetime.datetime.today()
                    product.save()
                    return JsonResponse({'status':1, 'message': 'Updated Meta'})
                except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# UPDATE PRODUCT
# ==============================================================================
@accountant_required
def saveAsADraft(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST['target']  
            if target=="":
                return JsonResponse({'status':0, 'message':'Target Not Define'})
            else:
                try:
                    ProductList.objects.filter(pk=target).update(is_active=False, is_verified=False, is_draft=True)
                    return JsonResponse({'status':1, 'message':'Save as a Draft'})
                except ProductList.DoesNotExist:
                    return JsonResponse({'status':1, 'message':'Product DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# UPDATE PRODUCT
# ==============================================================================
@accountant_required
def saveANDunpublish(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST['target']  
            if target=="":
                return JsonResponse({'status':0, 'message':'Target Not Define'})
            else:
                try:
                    ProductList.objects.filter(pk=target).update(is_active=False, is_verified=True, is_draft=False)
                    return JsonResponse({'status':1, 'message':'Save and Unpublish'})
                except ProductList.DoesNotExist:
                    return JsonResponse({'status':1, 'message':'Product DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# UPDATE PRODUCT
# ==============================================================================
@accountant_required
def saveANDPublishNow(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST['target']  
            if target=="":
                return JsonResponse({'status':0, 'message':'Target Not Define'})
            else:
                try:
                    ProductList.objects.filter(pk=target).update(is_active=True, is_verified=True, is_draft=False)
                    return JsonResponse({'status':1, 'message':'Save & Publish Now'})
                except ProductList.DoesNotExist:
                    return JsonResponse({'status':1, 'message':'Product DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# UPDATE PRODUCT
# ==============================================================================

# ==============================================================================
# DELETE PRODUCT
# ==============================================================================
@accountant_required
def ACTIVATEProduct(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST['targetPRODCUT']  
            if target=="":
                return JsonResponse({'status':0, 'message':'Target Not Define'})
            else:
                try:
                    obj = ProductList.objects.get(pk=target)
                    obj.is_draft=False
                    obj.is_verified=True
                    obj.is_active=True
                    obj.save()
                    return JsonResponse({"status":1, "message":"Product Activated","AFTERTask":f"{request.META['HTTP_REFERER']}"})
                except ProductList.DoesNotExist:
                    return JsonResponse({'status':0, 'message':'Product - DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DELETE PRODUCT
# ==============================================================================
@accountant_required
def DEACTIVATEProduct(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST['targetPRODCUT']  
            if target=="":
                return JsonResponse({'status':0, 'message':'Target Not Define'})
            else:
                try:
                    ProductList.objects.filter(pk=target).update(is_active=False)
                    return JsonResponse({"status":1, "message":"Product Deactivated","AFTERTask":f"{request.META['HTTP_REFERER']}"})
                except ProductList.DoesNotExist:
                    return JsonResponse({'status':0, 'message':'Product - DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DELETE PRODUCT
# ==============================================================================
@accountant_required
def CLOSEDProduct(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST['targetPRODCUT']  
            if target=="":
                return JsonResponse({'status':0, 'message':'Target Not Define'})
            else:
                try:
                    ProductList.objects.filter(pk=target).update(is_deleted=True, is_active=False, is_verified=True)
                    return JsonResponse({"status":1, "message":"Product Deleted","AFTERTask":f"{request.META['HTTP_REFERER']}"})
                except ProductList.DoesNotExist:
                    return JsonResponse({'status':0, 'message':'Product - DoesNotExist'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# DELETE PRODUCT
# ==============================================================================
@accountant_required
def DELETEProduct(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            target = request.POST['targetPRODCUT']  
            if target=="":
                return JsonResponse({'status':0, 'message':'Target Not Define'})
            else:
                try:
                    ProductList.objects.get(pk=target, is_draft=False, is_verified=True, is_active=True)
                    return JsonResponse({"status":0, "message":"Product Is Active", "AFTERTask":f"{request.META['HTTP_REFERER']}"})
                except ProductList.DoesNotExist:
                    ProductList.objects.filter(pk=target).delete()
                    return JsonResponse({'status':1, 'message':'Product Deleted'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
# ==============================================================================
# MORE OPERATION
# ==============================================================================
@accountant_required
def BOOSTREQUESTFORTHISPRODUCT(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method == "POST":
                target = request.POST['targetPRODCUT']  
                if target=="":
                    return JsonResponse({'status':0, 'message':'Target Not Define'})
                else:
                    try:
                        product = ProductList.objects.get(pk=target)
                        Best_Selling = request.POST.get('Best_Selling')
                        print("Best_Selling", Best_Selling)
                        if Best_Selling !="true":
                            print('Best_Selling', Best_Selling)
                            product.is_Best = True
                            product.save()
                        else:
                            product.is_Best = False
                            product.save()
                            
                        New_Arrivals = request.POST.get('New_Arrivals')
                        print("New_Arrivals", New_Arrivals)
                        if New_Arrivals != "true":
                            product.is_Arrivals = True
                            product.save()
                        else:
                            product.is_Arrivals = False
                            product.save()
                        
                        print(product.is_Arrivals)
                        print(product.is_Best)
                        

                        return JsonResponse({"status":1, "message":"Product Boosted","AFTERTask":f"{request.META['HTTP_REFERER']}"})
                    except ProductList.DoesNotExist:
                        return JsonResponse({'status':0, 'message':'DoesNotExist'})
            else:
                return JsonResponse({'status':0, 'message':'Bad Request'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})


@accountant_required
def AddFeedBack(request):
    if request.session.has_key('AAKRITICMSusername'):
        targetPRODUCT = request.POST.get('targetPRODUCT')
        targetUSER = request.POST.get('targetUSER')
        ratting = request.POST.get('ratting')
        message = request.POST.get('message')
        if targetPRODUCT=="" or targetPRODUCT==None:
            return JsonResponse({'status':0, 'message':'PRODUCT Required*'})
        elif targetUSER=="" or targetUSER==None:
            return JsonResponse({'status':0, 'message':'USER Required*'})
        elif ratting=="" or ratting==None:
            return JsonResponse({'status':0, 'message':'Ratting Required*'})
        elif message=="" or message==None:
            return JsonResponse({'status':0, 'message':'Message Required*'})
        else:
            try:
                # ratting
                ProductRatting.objects.create(product_id=targetPRODUCT, user_id=targetUSER, Ratting=ratting, message=message)
                totalReviewer = ProductRatting.objects.filter(product_id=targetPRODUCT).count()
                totalRatting = ProductRatting.objects.filter(product_id=targetPRODUCT)
                print(totalRatting.count())
                subTotal = sum([totalReviewer.Ratting for totalReviewer in totalRatting])
                print(totalReviewer)
                print(subTotal)

                return JsonResponse({'status':1, 'message':'Feedback Shared'})
            except Exception as e:
                return JsonResponse({'status':0, 'message': f'{e} Error Occured'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})


from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from django.http import Http404



# ==============================================================================
# PRODUCT ADD CART 
# ==============================================================================
def addTOCart(request):
    if request.session.has_key('KHANTAILORusername'):
        target = request.POST.get('target')
        qty = request.POST.get('qty')
        attribute = request.GET.get('attribute')
        if attribute:
            attribute = attribute
        else:
            attribute = ''
            
        if(target == ""):
            return JsonResponse({'status':0, 'message':'Target Required*'})
        else:
            try:
                if ProductMyCart.objects.filter(user_id=request.user.pk, product_id=target, attribute=attribute).exists():
                    return JsonResponse({'status':0, 'message':'Already Exists'})
                else:
                    ProductMyCart.objects.create(user_id=request.user.pk, product_id=target, attribute=attribute, qty=qty) 
                    return JsonResponse({'status':1, 'message':'Added To Cart '})
            except Exception as e:
                print(e)
                return JsonResponse({'status':0, 'message':f'{e} Error Occured'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================


# ==============================================================================
# PRODUCT ADD Wishlist 
# ==============================================================================
@accountant_required
def addToWishlist(request):
    if request.session.has_key('AAKRITICMSusername') and request.session.has_key('AAKRITICMSpassword') and request.session.has_key('AAKRITICMSrole') and request.session.has_key('AAKRITICMSUser'):
        target = request.POST.get('target')
        if(target == ""):
            return JsonResponse({'status':0, 'message':'Target Required*'})
        else:
            try:
                if ProductMyWishlist.objects.filter(user_id=request.user.pk, product_id=target).exists():
                    return JsonResponse({'status':0, 'message':'Already Exists Wishlist'})
                else:
                    ProductMyWishlist.objects.create(user_id=request.user.pk, product_id=target) 
                    return JsonResponse({'status':1, 'message':'Added To Wishlist '})
            except Exception:
                return JsonResponse({'status':0, 'message':f'Error Occured'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================



# ==============================================================================
# SEARCHPRODUCTAJAXService ADD Wishlist 
# ==============================================================================
from django.db.models import Q
@accountant_required
def SEARCHPRODUCTAJAXService(request):
    try:
        query = request.POST.get('query')
        products = ProductList.objects.filter(is_active=True).filter(Q(name__icontains=query))
        Count = ProductList.objects.filter(is_active=True).filter(Q(name__icontains=query)).count()
        context = {
            'ProductList': products,
            'ResultFound': Count,
            'query': query,
        }
        return render(request, './template/search/singlePRODUCT.html', context)
    except Exception:
        products = ProductList.objects.filter(is_active=True)[:10]
        context = {
            'ProductList': products
        }
        return render(request, './template/search/singlePRODUCT.html', context)
# ==============================================================================
# attrname
# attrcolor
# attrsize
# attrmrp
# attrsp
# attrimg
# attrimg1
# attrimg2
# attrimg3
# attrimg4
# ==============================================================================
# DIR SETTINGS
# ==============================================================================
@accountant_required
def createATTRIBUTEPRODUCT(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:   
            target = request.POST['target']     
            if target == '' or target == None:
                return JsonResponse({'status':0, 'message':'Target is Not Define'})
            else:
                try:
                    product = ProductList.objects.get(pk=target)

                    if (request.POST['attrcolor']):
                        attrcolor = request.POST.get('attrcolor')                    
                    if (request.POST['attrsize']):
                        attrsize = request.POST.get('attrsize')
                    if (request.POST['attrmrp']):
                        attrmrp = request.POST.get('attrmrp')
                    if (request.POST['attrsp']):
                        attrsp = request.POST.get('attrsp')

                    if (request.POST['attrname']):
                        attrname = request.POST.get('attrname')

                    img = request.FILES.get('attrimg')
                    img1 = request.FILES.get('attrimg1')
                    img2 = request.FILES.get('attrimg2')
                    img3 = request.FILES.get('attrimg3')
                    img4 = request.FILES.get('attrimg4')

                    if (img != None and img !='undefined'):
                        product.img =img                 
                    if (img1 != None and img1 !='undefined'):
                        product.img1 =img1
                    if (img2 != None and img2 !='undefined'):
                        product.img2 =img2
                    if (img3 != None and img3 !='undefined'):
                        product.img3 =img3
                    if (img4 != None and img4 !='undefined'):
                        product.img4 =img4
                    ATTRIBUTEProductList.objects.create(product_id=target, name=attrname, img=img, img1=img1,img2=img2,img3=img3,img4=img4,color=attrcolor,size=attrsize,mrp=attrmrp,sp=attrsp)
                    return JsonResponse({'status':1, 'message': 'Successfully Attr Created'})
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'{e} - Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})
# ==============================================================================
# SIMILARPRODUCTSList
# ==============================================================================
# CREATE SIMILAR PRODUCT
# ==============================================================================
@accountant_required
def createSIMILARRODUCT(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:   
            target = request.POST['target']     
            if target == '' or target == None:
                return JsonResponse({'status':0, 'message':'Target is Not Define'})
            else:
                try:

                    attrmrp = request.POST.get('attrmrp')
                    if attrmrp:
                        attrmrp = attrmrp
                        
                    attrsp = request.POST.get('attrsp')
                    if attrsp:
                        attrsp = attrsp
                        
                    attributes = request.POST.get('attributes')
                    if attributes:
                        attributes = attributes
                        
                    SIMILARPRODUCTSList.objects.create(product_id=target, mrp=attrmrp, sp=attrsp, attributes=attributes)
                    return JsonResponse({'status':1, 'message': 'Successfully Attr Created'})
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'{e} - Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You dont Have Permission'})
    else:
        return JsonResponse({'status':0, 'message':' Register Account & Login First'})