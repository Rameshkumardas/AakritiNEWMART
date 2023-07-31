from django.urls import path

from Message import AJAXRequest, announcement, contactedUS, feedback, newsletter, replywithEMAIL
from . import views, notification
# from Message.api import feedbackAPI, contactUSAPI
 
urlpatterns = [

    # =============================MESSAGE-API-SECTION=================================
    # =============================MESSAGE-API-SECTION=================================
    # =============================MESSAGE-API-SECTION=================================
    # =============================MESSAGE-API-SECTION=================================
    # =============================MESSAGE-API-SECTION=================================
    # =============================MESSAGE-API-SECTION=================================
    # =============================MESSAGE-API-SECTION=================================
    # path('applicationFEEDBACK/<pNumber>/', feedbackAPI.applicationFEEDBACK, name='applicationFEEDBACK'),    
    # path('contactStrikeIndia/', contactUSAPI.contactStrikeIndia.as_view(), name='contactStrikeIndia'),    
    # =============================announcement.ContactedList=================================
    # =============================announcement.ContactedList=================================
    # =============================announcement.ContactedList=================================
    # =============================announcement.ContactedList=================================
    # =============================announcement.ContactedList=================================
    # =============================announcement.ContactedList=================================
    # =============================announcement.ContactedList=================================
    path('Announcements/', announcement.Announcement, name='Announcements'),    
    path('AnnouncementList/', announcement.AnnouncementList, name='AnnouncementList'),    
    path('addNEWAnnouncement/', announcement.addNEWAnnouncement, name='addNEWAnnouncement'),    
    path('commonOPERATIONSFORAnnouncement/', announcement.commonOPERATIONSFORAnnouncement, name='commonOPERATIONSFORAnnouncement'),    
    path('Announcements/', announcement.Announcement, name='Announcements'),    
    path('Announcements/', announcement.Announcement, name='Announcements'),    
    # =============================newsletter.ContactedList=================================
    # =============================newsletter.ContactedList=================================
    # =============================newsletter.ContactedList=================================
    # =============================newsletter.ContactedList=================================
    # =============================newsletter.ContactedList=================================
    # =============================newsletter.ContactedList=================================
    # =============================newsletter.ContactedList=================================
    path('Newsletter/', newsletter.NewsletterList, name='NewsletterList'),    
    path('sendMESSAGEWITHEMAIL/', newsletter.sendMESSAGEWITHEMAIL, name='sendMESSAGEWITHEMAIL'),    
    path('sendMESSAGEWITHNumber/', newsletter.sendMESSAGEWITHNumber, name='sendMESSAGEWITHNumber'),    
    # =============================feedback.ContactedList=================================
    # =============================feedback.ContactedList=================================
    # =============================feedback.ContactedList=================================
    # =============================feedback.ContactedList=================================
    # =============================feedback.ContactedList=================================
    # =============================feedback.ContactedList=================================
    # =============================feedback.ContactedList=================================
    path('feedbackLIST/', feedback.feedbackLIST, name='feedbackLIST'),   
    path('allFEEDBACKLIST/deleteFEEDBACK/<int:pk>/', feedback.deleteFEEDBACK, name="deleteFEEDBACK"),
    path('allFEEDBACKLIST/activatedFEEDBACK/<int:pk>/', feedback.activatedFEEDBACK, name="activatedFEEDBACK"),
    path('allFEEDBACKLIST/deactivatedFEEDBACK/<int:pk>/', feedback.deactivatedFEEDBACK, name="deactivatedFEEDBACK"),
    path('allFEEDBACKLIST/rejectedFEEDBACK/<int:pk>/', feedback.rejectedFEEDBACK, name="rejectedFEEDBACK"),
    
    
    



 
    # =============================contactedUS.ContactedList=================================
    # =============================contactedUS.ContactedList=================================
    # =============================contactedUS.ContactedList=================================
    # =============================contactedUS.ContactedList=================================
    # =============================contactedUS.ContactedList=================================
    # =============================contactedUS.ContactedList=================================
    # =============================contactedUS.ContactedList=================================
    path('closedCONTACTEDLIST/', contactedUS.DeactiveContactedList, name='DeactiveContactedList'),    
    path('pendingCONTACTEDLIST/', contactedUS.ContactedList, name='ContactedList'),    
    path('acceptedCONTACTEDLIST/', contactedUS.ActiveContactedList, name='ActiveContactedList'),    
    path('closedCONTACTEDLIST/', contactedUS.DeactiveContactedList, name='DeactiveContactedList'),    

    path('allCONTACTEDLIST/deleteCONTACTED/<int:pk>/', contactedUS.deleteCONTACTED, name="deleteCONTACTED"),
    path('allCONTACTEDLIST/activatedCONTACTED/<int:pk>/', contactedUS.activatedCONTACTED, name="activatedCONTACTED"),
    path('allCONTACTEDLIST/deactivatedCONTACTED/<int:pk>/', contactedUS.deactivatedCONTACTED, name="deactivatedCONTACTED"),

    path('allCONTACTEDLIST/rejectedCONTACTED/<int:pk>/', contactedUS.rejectedCONTACTED, name="rejectedCONTACTED"),
    
    
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # =============================contactedUS.withWEB.ContactedList=================================
    # path('withAJAXSERVICE/ContactUSFORQuery/', AJAXRequest.ContactUSFORQuery, name="ContactUSFORQuery"),
    path('withAJAXSERVICE/GENERATE_CONTACT_REQUEST/', AJAXRequest.GENERATE_CONTACT_REQUEST, name="GENERATE_CONTACT_REQUEST"),
    path('withAJAXSERVICE/SAVE_CONTACT_US_REQUEST_SEND_EMAIL/', AJAXRequest.SAVE_CONTACT_US_REQUEST_SEND_EMAIL, name="SAVE_CONTACT_US_REQUEST_SEND_EMAIL"),
    # 

    path('NotificationList/', notification.NotificationList, name='NotificationList'),   

    path('withAJAXSERVICE/SUBSCRIBE_NEWSLETTER/', AJAXRequest.SUBSCRIBE_NEWSLETTER, name="SUBSCRIBE_NEWSLETTER"),




]

