from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello Bitch....') 

def contact(request):
    return HttpResponse("the contact")

def about(request):
    return HttpResponse("dis da about hoe")

def blog(request):
    return HttpResponse("the blog")