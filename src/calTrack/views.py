from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, loader
from django.views import generic
from django.http import HttpResponse
import dataAccess

# Create your views here.

def loadAjaxData(request, query):
    if query == 'getAllFood':
        foodList = dataAccess.getAllFoods()
        return  render_to_response('foodlist.html', {'foodList':foodList}, context_instance=RequestContext(request))
    elif query == 'login':
        return HttpResponse("Logged in for:"+request.POST['loginEmailName'] + " Pwd:" +request.POST['loginPwdName'])
    elif query == 'register':
        return HttpResponse("Registered for:"+request.POST['loginEmailName'] + " Pwd:" +request.POST['loginPwdName'])
    else:
        return HttpResponse("Ajax Error")

def index(request):
    return  render_to_response('index.html', context_instance=RequestContext(request))
