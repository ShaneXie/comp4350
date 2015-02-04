from django.db import models
from django.core.validators import ValidationError


# Create your models here.

FOOD_TYPE_CHOICES = (
    ('l','Lunch'),
    ('d','Dinner'),
    ('b','Breakfast'),
    ('s','Snacks'),
)

class Foods(models.Model):

    fName = models.CharField(max_length = 50)
    fCalorie = models.PositiveIntegerField (default=1)
    fType = models.CharField (choices=FOOD_TYPE_CHOICES, max_length = 1)

    def getFoodListByType(self, foodType):

    	foodList = Foods.objects.filter(fType__exact = 'foodType')
    	return foodList

    def __unicode__(self):
        return self.fName

    def clean(self):

    	if self.fCalorie == 0:
    		raise ValidationError({'fCalorie': 'Food calories cannot be zero.'})

