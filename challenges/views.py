from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse('Try to sleepa t least 8 hours a day')

def february(request):
    return HttpResponse('Walk 20 minutes everyday')