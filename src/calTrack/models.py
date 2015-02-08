from django.db import models
from django.core.validators import ValidationError, RegexValidator
from django.contrib.auth.models import User


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

            
class UserProfile(models.Model):

    GENDER_TYPE = (
        ('m','Male'),
        ('f','Female'),
    )

    user = models.ForeignKey(User, unique=True)
    age = models.PositiveIntegerField(default = 1, max_length = 2)
    weight = models.FloatField(default=0.0, max_length = 3)
    height = models.FloatField(default=0.0, max_length = 3)
    amtOfExc = models.FloatField(default=0.0, blank = True)
    gender = models.CharField(choices=GENDER_TYPE, max_length = 1)

    def __unicode__(self):
        return ' '.join([
            self.user.first_name,
            self.user.last_name,
        ])

    def clean(self):

        #Limits are based on worlds height and weight records.
        if self.age < 10 and self.age >100:
            raise ValidationError({'age': 'Invalid age.'})

        if self.height < 50 and self.height > 250:
            raise ValidationError({'height': 'Invalid height.'})

        if self.weight < 10 and self.height > 700:
            raise ValidationError({'weight': 'Invalid weight.'})



