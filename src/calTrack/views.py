from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, Loader
from django.views import generic
from calTrack.models import Foods
from django.http import HttpResponse

# Create your views here.

def index(request):
    food_list = Foods.objects.all()
    t = Loader.get.template('index.html')
    c = Context({'food_list':food_list,})
#return render_to_response(,context_instance=RequestContext(request))
    return HttpResponse(t.render(c))

