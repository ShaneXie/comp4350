from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, loader
from django.views import generic
from calTrack.calTrack_models.foods import Foods
from django.http import HttpResponse

# Create your views here.

def getName(currReq):
    if 'name' in currReq:
        print currReq['name']
        return currReq['name']

def getCalorie(currReq):
    if 'nofc' in currReq:
        print currReq['nofc']
        return currReq['nofc']

def index(request):
    foodList = Foods.objects.all()
    error = False
    if request.method == 'POST':
        currReq = request.POST
        fNameNew = getName(currReq)
        fCalorieNew = getCalorie(currReq)

        if not fNameNew and not fCalorieNew:
                error = True
        else:
                food = Foods(fName = fNameNew, fCalorie = fCalorieNew)
                food.save()
    return  render_to_response('index.html', {'foodList':foodList,'error': error}, context_instance=RequestContext(request))