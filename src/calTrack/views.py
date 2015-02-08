from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, loader
from django.views import generic
from django.http import HttpResponse
import dataAccess


# Create your views here.

def loadAjaxData(request, query):
    errMsg="Ajax Error Message"
    if query == 'getAllFood':
        foodList = dataAccess.getAllFoods()
        if foodList:
            return  render_to_response('foodlist.html', {'foodList':foodList}, context_instance=RequestContext(request))
        else:
            errMsg="Get food list Error Message"
    elif query == 'getLoginItem':
        return render_to_response('loginNavItem.html', context_instance=RequestContext(request))
    elif query == 'login':
        return HttpResponse(dataAccess.login(request))
    elif query == 'logout':
        return HttpResponse(dataAccess.logout(request))
    elif query == 'register':
        return HttpResponse(dataAccess.add_user(request))
    elif query == 'addFood':
        return HttpResponse(dataAccess.add_Food(request))
    else:
        errMsg="Unknown Request"

    return HttpResponse(errMsg)

def index(request):
    return  render_to_response('index.html', context_instance=RequestContext(request))
