from .models import PROJECTInformation

class PROJECTInformationMiddleWare:
    def __init__(self, get_response):
        try:
            PROJECT = PROJECTInformation.objects.last()
            print('===========================================================================================')
            print('===========================================================================================')
            print("PROJECT NAME ->> ", PROJECT.name)
            print("PROJECT TITLE ->> ", PROJECT.title)
            print("PROJECT DEBUG ->> ", PROJECT.DEBUG)
            if PROJECT.DEBUG:
                print("PROJECT MODE ->> ", 'Development & Debug Server')
            else:
                print("PROJECT MODE ->> ", '[ Live & Secure Server ]')
            print('===========================================================================================')
        except Exception:
            print('PROJECT NOT UPDATE BY ADMIN')
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
    
class MRDasDeveloper:
    def __init__(self, get_response):
        self.get_response = get_response
        print('********************=================RAMESH KUMAR DAS===============***********************')
        print("I'm Ramesh Kuamr Das Belong to Nepal Contac No +91 7322057677 & Email Id das82916@gmail.com ")
        print("WhatApps No +91 7322057677")
        print("Kindly Visit Once https://www.linkedin.com/in/mɽ-das/")
        print('********************=================RAMESH KUMAR DAS===============***********************')
        print('===========================================================================================')
        print('===========================================================================================')
        # One-time configuration and initialization.
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print('********************=================RAMESH KUMAR DAS===============***********************')
        # print("I'm Ramesh Kuamr Das Belong to Nepal Contac No +91 7322057677 & Email Id das82916@gmail.com ")
        # print("WhatApps No +91 7322057677")
        # print("Kindly Visit Once https://www.linkedin.com/in/mɽ-das/")
        # print('********************=================RAMESH KUMAR DAS===============***********************')
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
    
    # def process_request(self, request):
    #     print("I'm Ramesh Kuamr Das Belong to Nepal Contac No +91 7322057677 and Email Id das82916@gmail.com ")
        