from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, loader
from django.views import generic
from calTrack.calTrackModels.foods import Foods

# Create your views here.

def loadAjaxData(request, query):
    if query == 'getAllFood':
        foodList = Foods.objects.all()
        return  render_to_response('foodlist.html', {'foodList':foodList}, context_instance=RequestContext(request))
    else:
        return HttpResponse("Ajax Error")

def index(request):
    return  render_to_response('index.html', context_instance=RequestContext(request))
