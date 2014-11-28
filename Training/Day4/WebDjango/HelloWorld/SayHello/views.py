from django.shortcuts import render
from django.http.response import HttpResponse
from SayHello.models import Contact

# Create your views here.
def sayHello(request):
    return HttpResponse("we are saying Hello to you!")

def contacts():
    allContacts = Contact.objects().get()
    return HttpResponse(allContacts)