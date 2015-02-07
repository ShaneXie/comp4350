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

    print "line 0"
    user = User.objects.create_user(username, email, pwd)
    #user = User(username=username,email=email,password=pwd,first_name=fName,last_name=lName)
    user.first_name = fName
    user.last_name = lName
    user.save()
    print "line 1"
    profile = UserProfile(user=user,weight=weight,height=height,gender=gender)
    profile.save()

    #todo add new user
    return True
