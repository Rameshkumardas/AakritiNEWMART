


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from AdminAuthentication.models import AdminRegistration
from django.core.mail import BadHeaderError, send_mail
import threading
from threading import Thread

from BULKEMAILManager.models import EMAILList
from ExtraSettings.models import PROJECTInformation

class EmailThread(threading.Thread):
    def __init__(self, subject, emailHOST, html_content, recipient_list):
        self.subject = subject
        self.emailHOST = emailHOST
        self.recipient_list = tuple(recipient_list)
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        project = PROJECTInformation.objects.last()        

        for email in self.recipient_list:
            SendEmail = EmailMultiAlternatives(self.subject, strip_tags(self.html_content), self.emailHOST, to=[email, ], reply_to=[project.mail, ])
            SendEmail.attach_alternative(self.html_content, "text/html")
            SendEmail.send() 
            EMAILList.objects.filter(email=email).update(is_sent=True)
            print("self.recipient_list", self.recipient_list)
            
            
            
