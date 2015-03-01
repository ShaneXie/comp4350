from django.db import models
from django.core.validators import ValidationError, RegexValidator
from django.contrib.auth.models import User


# Create your models here.

FOOD_TYPE_CHOICES = (
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
    ('Breakfast','Breakfast'),
    ('Snacks','Snacks'),
)

onlyAlphabet = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabets are allowed for the food name.')

class Foods(models.Model):

    fName = models.CharField(max_length = 25, unique=True, validators=[onlyAlphabet])
    fCalorie = models.PositiveIntegerField (default=1, max_length=4)
    fType = models.CharField (choices=FOOD_TYPE_CHOICES, max_length=10)

    def getFoodListByType(self, foodType):
        foodList = Foods.objects.filter(fType__exact = 'foodType')
        return foodList

    def __unicode__(self):
        return self.fName

    def clean(self):
        if self.fCalorie == 0:
            raise ValidationError({'fCalorie': 'Food calories cannot be zero.'})

        if self.fType != 'Lunch' and self.fType != 'Dinner' and self.fType != 'Breakfast' and self.fType != 'Snacks':
            raise ValidationError({'fType': 'Invalid food type'})

        if Foods.objects.filter(fName=self.fName).count() > 0:
            raise ValidationError({'fName': 'This food already exists'})

            
class UserProfile(models.Model):

    GENDER_TYPE = (
        ('Male','Male'),
        ('Female','Female'),
    )
    user = models.ForeignKey(User, unique=True)
    age = models.PositiveIntegerField(default = 1, max_length = 2)
    weight = models.FloatField(default=1.0, max_length = 3)
    height = models.FloatField(default=1.0, max_length = 3)
    amtOfExc = models.PositiveIntegerField(default=0, blank = True)
    gender = models.CharField(choices=GENDER_TYPE, max_length = 10)

    def __unicode__(self):
        return ' '.join([
            self.user.first_name,
            self.user.last_name])

    def clean(self):

        #Limits are based on worlds height and weight records.
        if self.age < 10:
            raise ValidationError({'age': 'Are you sure about your age?'})
        elif self.age >100:
            raise ValidationError({'age': 'Are you sure about your age?'})

        if self.height < 50:
            raise ValidationError({'height': 'Are you sure about your height?'})
        elif self.height > 250:
            raise ValidationError({'height': 'Are you sure about your height?'})

        if self.weight < 10:
            raise ValidationError({'weight': 'Are you sure about your weight?'})
        elif self.weight > 700:
            raise ValidationError({'weight': 'Are you sure about your weight?'})



