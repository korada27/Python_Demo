from django.contrib import admin

# Register your models here.
from myrestaurants import models

admin.site.register(models.Restaurant)
admin.site.register(models.Dish)
admin.site.register(models.RestaurantReview)
