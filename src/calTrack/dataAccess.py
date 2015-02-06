__author__ = 'An'

from calTrack.calTrackModels.foods import Foods


def getAllFoods():
    return Foods.objects.all()
