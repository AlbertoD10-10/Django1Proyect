from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to home Page</h1>')
    return render(request,'home.html',{'name':'Alberto Diaz'})

def About(request):
    #return HttpResponse('<h1>Welcome to home Page</h1>')
    return render(request,'About.html',{'name':'Alberto Andres Diaz Mejia'})     
