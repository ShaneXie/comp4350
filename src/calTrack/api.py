__author__ = 'anx and Nitesh'


from calTrack.models import Foods,UserProfile
from django.contrib.auth.models import User
from django.core import serializers
import json


def allFoodsJson():
    raw_data = serializers.serialize("json", Foods.objects.all())
    return raw_data



def userProfile(req):
	username = req.user
	profile =  UserProfile.objects.filter(user__username=username)
	raw_data = serializers.serialize("json", profile)
	return raw_data