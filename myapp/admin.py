from django.contrib import admin
from .models import FoodItem, Order, FeatureProduct

# Register your models here.
admin.site.register(FoodItem)

admin.site.register(Order)
admin.site.register(FeatureProduct)
