from django.db import models

class Users(models.Model):

    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)
    weight = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    amtOfExc = models.FloatField(default=0.0)
    gender = models.CharField(max_length=1)

    def __unicode__(self):
        return self.firstName
