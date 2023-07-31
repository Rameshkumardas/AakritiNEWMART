from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminRegistration
from BLOGManager.models import BLOGList, BlogMainCat, BlogSubCat, allBLOGCOMMENTS
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q


def ALLBLOGS(request):
    try:
        q = request.GET.get('q')
        if q:
            post_list = BLOGList.objects.select_related('author').filter(is_active=True, is_verified=True).filter(Q(name__icontains=q))
        else:
            post_list = BLOGList.objects.filter(is_active=True, is_verified=True)
        try:
            page = request.GET.get('page', 1)
            paginator = Paginator(post_list, 10)
            allBLOG = paginator.page(page)  
        except PageNotAnInteger:
            allBLOG = paginator.page(1)
        except EmptyPage:
            allBLOG = paginator.page(paginator.num_pages)            
        popularBLOGS = BLOGList.objects.select_related('author').filter(is_active=True, is_verified=True).order_by('-views')[:5]
        context = {
            'dashboard':'menu-open', 
            'default': 'active',
            'BLOGList':allBLOG,
            'popularBLOGS':popularBLOGS,
        }
        return render(request,"./template/home/BLOGindex.html", context )

    except Exception as e:
        print("Ops AllBlogs", e)
        return redirect(request.META.get('HTTP_REFERER'))


def ALLMAINCATBLOGS(request, slug):
    try:
        allTRENDBLOG = BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(mainCat__slug__startswith=slug).order_by('-views')[:10]
        allNEWBLOG = BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(mainCat__slug__startswith=slug).order_by('-last_update')[:10]
        
        context = {
            'dashboard':'menu-open', 
            'default': 'active',
            'allTRENDBLOG':allTRENDBLOG,
            'allNEWBLOG':allNEWBLOG,

        }
        return render(request,"./template/home/allMAINCATBLOGS.html", context )

    except Exception as e:
        print("Ops AllBlogs", e)
        return redirect(request.META.get('HTTP_REFERER'))



def ALLSUBCATBLOGS(request, main_slug, slug):
    try:
        allTRENDBLOG = BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(SubCat__slug__startswith=slug).order_by('-views')[:10]
        allNEWBLOG = BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(SubCat__slug__startswith=slug).order_by('-last_update')[:10]
        
        context = {
            'dashboard':'menu-open', 
            'default': 'active',
            'allTRENDBLOG':allTRENDBLOG,
            'allNEWBLOG':allNEWBLOG,

        }
        return render(request,"./template/home/allMAINCATBLOGS.html", context )

    except Exception as e:
        print("Ops AllBlogs", e)
        return redirect(request.META.get('HTTP_REFERER'))






def BLOG(request, slug=None):
    try:
        BLOG = BLOGList.objects.get(slug=slug)
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            comment = request.POST.get('comment')
            if request.session.has_key('AakritiMARTusername'):
                allBLOGCOMMENTS.objects.create(blog_id=BLOG.pk, user_id=request.user.pk, description=comment)
            else:
                try:
                    user = AdminRegistration.objects.get(email=email)
                except Exception:
                    user = AdminRegistration.objects.create(email=email, fname=fname, lname=lname,)

                allBLOGCOMMENTS.objects.create(blog_id=BLOG.pk, user_id=user.pk, description=comment)

        # if request.user.is_accountant:
        if BLOG.mainCat:
            # .select_related('mainCat', 'SubCat', 'author')
            allBLOG = BLOGList.objects.select_related('mainCat', 'SubCat', 'author').filter(mainCat_id=BLOG.mainCat.pk).exclude(slug=slug).order_by('id')[:3]
        else:
            # is_active=True, is_verified=True
            allBLOG = BLOGList.objects.select_related('mainCat', 'SubCat', 'author').filter(is_active=True, is_verified=True).order_by('-last_update')[:3]

        prevBLOG = BLOGList.objects.filter(mainCat=BLOG.mainCat, pk=int(BLOG.pk-1))
        nextBLOG = BLOGList.objects.filter(mainCat=BLOG.mainCat, pk=int(BLOG.pk+1))
        allCOMMENTS = allBLOGCOMMENTS.objects.filter(blog_id=BLOG.pk)
        BLOG.views = BLOG.views +1
        BLOG.comment =  allCOMMENTS.count()
        BLOG.save()

        context = {
            'dashboard':'menu-open', 
            'default': 'active',
            'allCOMMENTS':allCOMMENTS,
            'prevBLOG':prevBLOG,
            'nextBLOG':nextBLOG,

            'allRELATEDBLOGS':allBLOG,

            'blog':BLOG,
        }
        return render(request,"./template/home/readBLOG.html", context )
    except Exception as e:
        print(e)
        return redirect(request.META.get('HTTP_REFERER'))
    
def searchBLOG(request):
    try:
        q = request.GET.get('q')
        if q:
            allBLOG = BLOGList.objects.select_related('author').filter(is_active=True, is_verified=True).filter(Q(name__icontains=q))
            try:
                page = request.GET.get('page', 1)
                paginator = Paginator(allBLOG, 15)
                allBLOGs = paginator.page(page)  
            except PageNotAnInteger:
                allBLOGs = paginator.page(1)
            except EmptyPage:
                allBLOGs = paginator.page(paginator.num_pages)
            context = {
                'dashboard':'menu-open', 
                'default': 'active',
                'BLOGList':allBLOGs,
            }
            return render(request,"./template/home/searchBLOGS.html", context )
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return redirect(request.META.get('HTTP_REFERER'))
