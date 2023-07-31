from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, OperationalError
from django.shortcuts import render, redirect
from AdminAuthentication.models import AdminRegistration
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from AdminAuthentication.models import AdminRegistration
from django.core.mail import send_mail

from Message.models import ContactUS, ContactUSwithWEB
# =========================Reply With Email========================
# =========================Reply With Email========================
# =========================Reply With Email========================
# =========================Reply With Email========================
# =========================Reply With Email========================
# =========================Reply With Email========================
# =========================Reply With Email========================
# =========================Reply With Email========================
@login_required
def replyWithEmail(request, pk, user_id, query):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        reply_email = AdminRegistration.objects.get(user_id=user_id).mail
        updateSTATUS = ContactUS.objects.get(pk=pk)
        updateSTATUS.status = 'accepted'
        updateSTATUS.save()
        if request.method=="POST":
            if request.POST['reply_description']!='':
                answer = request.POST['reply_description']                    
            else:
                messages.error(request, 'Reply Description is Empty')
                return redirect(request.META.get('HTTP_REFERER'))
            try:
                html_content = render_to_string("./template/email/sendEMAIL.html", {'replyDESCRIPTION':answer})
                SendEmail = EmailMultiAlternatives(query, strip_tags(html_content), 'support@voicefreedom.org', [reply_email])
                SendEmail.attach_alternative(html_content, "text/html")
                SendEmail.send()
                messages.success(request, 'Email Sent Success')
                return redirect('https://sg2plmcpnl492240.prod.sin2.secureserver.net:2096/cpsess7317820701/3rdparty/roundcube/?_task=mail&_mbox=INBOX.Sent')
            except Exception:
                messages.error(request, 'Email Sending Error')
                return redirect(request.META.get('HTTP_REFERER'))
        context = {
            'Message': 'menu-open', 
            'Contacted': 'active', 
            'query':query,
            'email':reply_email
            }
        return render(request,"./template/contactedUS/replyWITHEmail.html", context)
    else:
        return redirect("AdminLogOut")


@login_required
def webreplyWithEmail(request, phone, email, description):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        updateSTATUS = ContactUSwithWEB.objects.get(status='pending', email=email, satisfied=0, phone=phone, description=description)
        updateSTATUS.status = 'accepted'
        updateSTATUS.save()
        if request.method=="POST":
            if request.POST['reply_description']!='':
                answer = request.POST['reply_description']                    
            else:
                messages.error(request, 'Reply Description is Empty')
                return redirect(request.META.get('HTTP_REFERER'))
            try:
                html_content = render_to_string("./template/email/sendEMAIL.html", {'replyDESCRIPTION':answer})
                SendEmail = EmailMultiAlternatives(description, strip_tags(html_content), 'support@voicefreedom.org', [email])
                SendEmail.attach_alternative(html_content, "text/html")
                SendEmail.send()
                messages.success(request, 'Email Sent Success')
                return redirect('https://sg2plmcpnl492240.prod.sin2.secureserver.net:2096/cpsess7317820701/3rdparty/roundcube/?_task=mail&_mbox=INBOX.Sent')
            except Exception:
                messages.error(request, 'Email Sending Error')
                return redirect(request.META.get('HTTP_REFERER'))
        context = {
            'Message': 'menu-open', 
            'Contacted': 'active', 
            'query':description,
            'email':email
            }
        return render(request,"./template/contactedUS/replyWITHEmail.html", context)
    else:
        return redirect("AdminLogOut")
    