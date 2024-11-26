# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Car Make')
    description = models.CharField(null=False, max_length=1000, default='Description')
    established = models.DateField(null=True)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description + "," + \
               "Established: " + str(self.established)


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models)
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=30, default='Car Model')
    CAR_TYPES = [
    ('Sedan', 'Sedan'),
    ('SUV', 'SUV'),
    ('Truck', 'Truck'),
    ('Coupe', 'Coupe'),
    ]
    type = models.CharField(null=False, max_length=30, choices=CAR_TYPES, default='Sedan')
    year = models.DateField(null=True)
    def __str__(self):
        return "Car Make: " + self.car_make.name + "," + \
               "Dealer ID: " + str(self.dealer_id) + "," + \
               "Name: " + self.name + "," + \
               "Type: " + self.type + "," + \
               "Year: " + str(self.year)
   
