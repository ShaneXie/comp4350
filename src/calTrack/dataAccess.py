__author__ = 'An and Nitesh'

from calTrack.models import Foods,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser

def foodCount():
    return Foods.objects.count()

def checkUserProfileExists(req):
    username = req.user
    profile =  UserProfile.objects.filter(user__username=username).count()
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
            ret="Your account is inactive"
    else:
        ret = "Wrong username or password."
    return ret

def logout(req):
    logoutUser(req)
    return "success"

def add_user(req):
    post = req.POST
    email = post['regEmailName']
    username = email
    pwd = post['regPwdName']
    fName = post['regFirstName']
    lName = post['regLastName']
    height = post['regHgtName']
    weight = post['regWgtName']
    gender = post['genName']

    if User.objects.filter(username=username).exists():
        return "This email address has been used. Please use another one."
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
                loginUser(req, theUser)

        return 'success'

def add_Food(req):
    if req.user.is_authenticated():
        data = req.POST
        fName = data['foodName']
        fCal = data['foodCal']
        fType = data['foodType']

        if Foods.objects.filter(fName=fName).exists():
            return "Food already exists."

        food = Foods(fName=fName,fCalorie=fCal,fType=fType)
        food.save()
        return 'success'
    else:
        return 'You need login to add new food.'

def update_profile(req):
    if req.user.is_authenticated():
        data = req.POST
        userWeight = data['weight']
        userHeight = data['height']
        userGender = data['gender']
        userId = data['user']

        UserProfile.objects.filter(user_id=userId).update(weight=userWeight, height=userHeight, gender=userGender);
        return 'success'
    else:
        return 'Updating user profile failed.'