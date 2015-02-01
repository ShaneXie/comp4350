from django.contrib import admin
from calTrack.calTrack_models.foods import Foods
from calTrack.calTrack_models.users import Users

# Register your models here.


admin.site.register(Foods)
admin.site.register(Users)