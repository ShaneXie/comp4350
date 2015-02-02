from django.db import models

# Create your models here.

class Foods(models.Model):

    fName = models.CharField(max_length = 50)
    fCalorie = models.IntegerField (default=0)
    fType = models.CharField (max_length = 1, blank = True)

    def __unicode__(self):
        return "{0} {1} {2}".format(self.fName, self.fCalorie, self.fType)
