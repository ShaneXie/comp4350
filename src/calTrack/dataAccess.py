__author__ = 'An'

from calTrack.models import Foods,UserProfile
from django.contrib.auth.models import User


def getAllFoods():
    return Foods.objects.all()
def login(post):
    #todo login logic
    #post['loginEmailName']
    return True

def add_user(post):
    email = post['regEmailName']
    username = email
    pwd = post['regPwdName']
    fName = post['regFirstName']
    lName = post['regLastName']
    height = post['regHgtName']
    weight = post['regWgtName']
    gender = post['genName']

    if User.objects.filter(username=username).exists():
        return "emailTaken"
    else:
        user = User.objects.create_user(username, email, pwd)
        user.first_name = fName
        user.last_name = lName
        user.save()
        profile = UserProfile(user=user,weight=weight,height=height,gender=gender)
        profile.save()
        return 'success'