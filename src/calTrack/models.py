from django.db import models
from django.core.validators import ValidationError, RegexValidator 


# Create your models here.

FOOD_TYPE_CHOICES = (
    ('l','Lunch'),
    ('d','Dinner'),
    ('b','Breakfast'),
    ('s','Snacks'),
)

onlyAlphabet = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabets are allowed for the food name.')

class Foods(models.Model):

    fName = models.CharField(max_length = 25, unique=True, validators=[onlyAlphabet])
    fCalorie = models.PositiveIntegerField (default=1)
    fType = models.CharField (choices=FOOD_TYPE_CHOICES, max_length = 1)

    def getFoodListByType(self, foodType):
        foodList = Foods.objects.filter(fType__exact = 'foodType')
        return foodList

    def __unicode__(self):
        return self.fName

    def clean(self):
        if self.fCalorie == 0:
            raise ValidationError({'Food Calories': 'Food calories cannot be zero or negative.'})

        if self.fType != 'l' and self.fType != 'd' and self.fType != 'b' and self.fType != 's':
            raise ValidationError({'Food Type': 'Invalid food type'})

        if Foods.objects.filter(fName=self.fName).count() > 0:
            raise ValidationError({'Food Type': 'This food already exists'})

            
class Users(models.Model):

    GENDER_TYPE = (
    ('m','Male'),
    ('f','Female'),
)

    firstName = models.CharField(max_length = 25)
    lastName = models.CharField(max_length = 25)
    age = models.PositiveIntegerField(default = 0)
    weight = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    amtOfExc = models.FloatField(default=0.0, blank = True)
    gender = models.CharField(choices=GENDER_TYPE, max_length = 1)

    def __unicode__(self):
        return ' '.join([
            self.firstName,
            self.lastName,
        ])

    def clean(self):

        if self.age == 0:
            raise ValidationError({'age': 'Invalid age.'})

