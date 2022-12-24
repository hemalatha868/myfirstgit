from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hema(request):
    return HttpResponse('<i><marquee>Hema is a good girl</marquee></i>')
    
