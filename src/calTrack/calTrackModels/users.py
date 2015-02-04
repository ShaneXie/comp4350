from django.db import models

class Users(models.Model):

    GENDER_TYPE = (
    ('m','M'),
    ('f','D'),
)

    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
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

