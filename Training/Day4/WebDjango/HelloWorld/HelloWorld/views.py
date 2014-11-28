'''
Created on 27 Nov 2014

@author: b8605521
'''
from django.core.context_processors import request
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello world.")