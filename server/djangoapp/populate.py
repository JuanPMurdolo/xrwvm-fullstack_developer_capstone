import datetime
from .models import CarMake, CarModel


def initiate():
    # Create CarMake instances
    car_make_data = [
        {"name": "NISSAN",
         "description": "Great cars. Japanese technology"},
        {"name": "Mercedes",
         "description": "Great cars. German technology"},
        {"name": "Audi",
         "description": "Great cars. German technology"},
        {"name": "Kia",
         "description": "Great cars. Korean technology"},
        {"name": "Toyota",
         "description": "Great cars. Japanese technology"},
    ]

    # Create CarMake entries
    car_make_instances = [
        CarMake.objects.create(
            name=data["name"],
            description=data["description"]
        ) for data in car_make_data
    ]

    # Create CarModel instances with corresponding CarMake
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year":
         datetime.date(2023, 1, 1), "car_make": car_make_instances[4]},
    ]

    # Create CarModel entries
    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_make=data["car_make"],
            type=data["type"],
            year=data["year"]
        )
