from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Meal,Category,Order,Promocode,Worker,MealToOrder])