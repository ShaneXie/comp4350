from django.db import models

# Create your models here.

class Foods(models.Model):

    fName = models.CharField(max_length = 50)
    fCalorie = models.IntegerField (default=0)
    fType = models.CharField (max_length = 1)

class Users(models.Model):

    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)
    weight = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    amtOfExc = models.FloatField(default=0.0)
    gneder = models.CharField(max_length=1)