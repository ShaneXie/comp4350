__author__ = 'An'

from calTrack.models import Foods,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginUser


def getAllFoods():
    return Foods.objects.all()

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