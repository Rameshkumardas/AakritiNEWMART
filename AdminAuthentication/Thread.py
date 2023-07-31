


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from AdminAuthentication.models import AdminRegistration
from django.core.mail import BadHeaderError, send_mail
import threading
from threading import Thread

class EmailThread(threading.Thread):
    def __init__(self, subject, emailHOST, html_content, recipient_list):
        self.subject = subject
        self.emailHOST = emailHOST
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        SendEmail = EmailMultiAlternatives(self.subject, strip_tags(self.html_content), self.emailHOST, self.recipient_list,)
        SendEmail.attach_alternative(self.html_content, "text/html")
        SendEmail.send()  
        