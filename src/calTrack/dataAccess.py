__author__ = 'An'

from calTrack.calTrackModels.foods import Foods


def getAllFoods():
    return Foods.objects.all()

def login(post):
    #todo login logic
    #post['loginEmailName']
    return True

def add_user(post):
    #todo add new user
    return True
