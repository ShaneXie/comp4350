from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
import dataAccess
import api

# Create your views here.

def loadAjaxData(request, query):
    errMsg="Ajax Error Message"
    if query == 'getAllFood':
        foodCount = dataAccess.foodCount()
        return render_to_response('foodlist.html', {'foodCount':foodCount}, context_instance=RequestContext(request))
    elif query == 'newRecord':
        foodCount = dataAccess.foodCount()
        return render_to_response('newRecord.html', {'foodCount':foodCount}, context_instance=RequestContext(request))
    elif query == 'getProfile':
        profile = dataAccess.checkUserProfileExists(request)
        return render_to_response('userProfile.html',{'profile':profile}, context_instance=RequestContext(request))
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
    elif query == 'updateProfile':
        return HttpResponse(dataAccess.update_profile(request))
    else:
        errMsg="Unknown Request"

    return HttpResponse(errMsg)


def loadJSON(request, query):
    errMsg="Ajax Error Message"
    if query == 'getAllFood':
        data = api.allFoodsJson()
        if data:
            return JsonResponse(data, safe=True)
        else:
            errMsg="Get food list Error Message,No Food in Database."
    elif query == 'getProfile':
        profileData = api.userProfile(request)
        if profileData:
            return JsonResponse(profileData, safe=True) 
        else:
            errMsg="User Profile Doesn't exists."
    else:
        errMsg="Unknown Request"

    return HttpResponse(errMsg)


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
