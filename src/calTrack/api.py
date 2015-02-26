__author__ = 'anx'


from calTrack.models import Foods,UserProfile
from django.core import serializers
import json


def allFoodsJson():
    raw_data = serializers.serialize("json", Foods.objects.all())
    format_data = [d for d in raw_data]
    return raw_data