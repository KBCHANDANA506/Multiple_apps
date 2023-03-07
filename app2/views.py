from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
 

def first_app2(request):
    return HttpResponse('<h1>First function of App2</h1>')



def Second_app2(request):
    return HttpResponse("<h1><marquee>Second Function of App2</marquee></h1>")