import csv

from django.core.management.base import BaseCommand

from vehicle.models import Car

# This command imports Vehicles.csv into the Car model
class Command(BaseCommand):
    def handle(self, *args, **options):
        dataReader = csv.reader(open('vehicle/Vehicles.csv'), delimiter=',', quotechar='"')

        # delete old data
        Car.objects.all().delete()

        # insert new data
        # skip 1st HEADER row
        next(dataReader)
        for row in dataReader:
            car = Car()
            car.vehicleId = row[0]
            car.make = row[1]
            car.shortModel = row[2]
            car.longModel = row[3]
            car.trim = row[4]
            car.derivative = row[5]
            car.yearIntroduced = row[6]
            car.yearDiscontinued = row[7]
            car.currentlyAvailable = row[8]
            car.save()
