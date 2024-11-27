from django.db import models


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Car Make')
    description = models.CharField(null=False,
                                   max_length=1000, default='Description')
    established = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description + "," + \
               "Established: " + str(self.established)


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake,
                                 on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=False)
    name = models.CharField(null=False,
                            max_length=30, default='Car Model')
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Coupe', 'Coupe'),
    ]
    type = models.CharField(null=False, max_length=30,
                            choices=CAR_TYPES, default='Sedan')
    year = models.DateField(null=True)

    def __str__(self):
        return "Car Make: " + self.car_make.name + "," + \
               "Dealer ID: " + str(self.dealer_id) + "," + \
               "Name: " + self.name + "," + \
               "Type: " + self.type + "," + \
               "Year: " + str(self.year)


class CarDealer:
    def __init__(self, address, city, full_name,
                 id, lat, long, short_name, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name
