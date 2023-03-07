from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def first_app1(request):
    return HttpResponse('<h1>First function of App1</h1>')

def Second_app1(request):
    return HttpResponse('<h1><marquee>Second function of App1</marquee></h1>')

