__author__ = 'anx and Nitesh'


from calTrack.models import Foods, UserProfile
from django.core import serializers

def foodQueryToDict(queryset):
	dic = {}
	arr = [{'fName':food['fName'],'fCalorie':food['fCalorie'],'fType':food['fType']} for food in queryset]
	dic["foods"]=arr
	return dic

def allFoodsJson():
    raw_data = Foods.objects.all().values('fName','fCalorie','fType')
    return foodQueryToDict(raw_data)


def userProfile(req):
	username = req.user
	profile = UserProfile.objects.filter(user__username=username).values('weight','height','gender','user')
	dic = {}
	arr = [{'weight':d['weight'],'height':d['height'],'gender':d['gender'],'user':d['user']} for d in profile]
	dic["profile"]=arr
	return dic