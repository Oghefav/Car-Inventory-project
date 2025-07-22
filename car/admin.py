from django.contrib import admin
from car.models import Car, CarAvailability, CarCondition, CarMake
# Register your models here.

admin.site.register([Car, CarAvailability, CarCondition, CarMake])
