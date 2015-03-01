__author__ = 'An and Nitesh'

from calTrack.models import Foods,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser


def getAllFoods():
    return Foods.objects.all()


def foodCount():
    return Foods.objects.count()

def checkUserProfileExists(req):
    username = req.user
    profile =  UserProfile.objects.filter(user__username=username).count()
    return profile

def getUserProfile(req):
    username = req.user
    profile =  UserProfile.objects.filter(user__username=username)[0]
    return profile


def login(req):
    post = req.POST
    usr = post['loginEmailName']
    pwd = post['loginPwdName']
    ret = ""
    user = authenticate(username=usr, password=pwd)
    if user is not None:
        if user.is_active:
            loginUser(req, user)
            ret="success"
        else:
            ret="disabled"
    else:
        ret = "wrongPwd"
    return ret

def logout(req):
    logoutUser(req)
    return "success"

def add_user(req):
    post= req.POST
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

        #login the new user
        theUser = authenticate(username=username, password=pwd)
        if theUser is not None:
            if theUser.is_active:
                loginUser(req, user)

        return 'success'

def add_Food(req):
    if req.user.is_authenticated():
        data = req.POST
        fName = data['foodName']
        fCal = data['foodCal']
        fType = data['foodType']

        food = Foods(fName=fName,fCalorie=fCal,fType=fType)
        food.save()
        return 'success'
    else:
        return 'noLogin'