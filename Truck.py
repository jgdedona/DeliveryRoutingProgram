from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time


class Truck:
    def __init__(self):
        self.packages = []
        self.miles = 0
        self.time = datetime.combine(date.today(), time.fromisoformat('08:00:00'))

    def add_package(self, package):
        self.packages.append(package)

    def remove_package(self, package):
        if package in self:
            self.packages.remove(package)

    def add_miles(self, miles):
        self.miles += miles

    def add_time(self, miles_traveled): # have to test this
        time_to_add = (miles_traveled/18.0) * 60
        self.time = self.time + timedelta(minutes = time_to_add)

    def __iter__(self):
        return iter(self.packages)

