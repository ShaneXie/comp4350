from django.contrib import admin
from calTrack.calTrackModels.foods import Foods
from calTrack.calTrackModels.users import Users

# Register your models here.


admin.site.register(Foods)
admin.site.register(Users)