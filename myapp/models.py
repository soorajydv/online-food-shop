from django.db import models
from django.contrib.auth.models import User


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="food/",null=False)
    # Add any other fields relevant to the FoodItem model
    
    def __str__(self):
        return self.name

class FeatureProduct(models.Model):
    food_items = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    def __str__(self):
        return self.food_items.name 


# Order tracking system

class Order(models.Model):
    STATUS_CHOICES = [
        ('PL', 'Placed'),
        ('SH', 'Shipped'),
        ('DL', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PL')
    tracking_number = models.CharField(max_length=20)
    def __str__(self):
        return self.tracking_number

    
