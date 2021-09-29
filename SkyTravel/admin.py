from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Places)
admin.site.register(AirChart)
admin.site.register(BusChart)
admin.site.register(AirTrip)
admin.site.register(BusTrip)
