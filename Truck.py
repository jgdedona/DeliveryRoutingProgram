from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time


class Truck:
    def __init__(self):
        self.packages = []
        self.miles = 0
        self.time = datetime.combine(date.today(), time.fromisoformat('08:00:00'))

    # O(1) amortized for time and space
    def add_package(self, package):
        self.packages.append(package)

    # O(n) for time, O(1) for space
    def remove_package(self, package):
        if package in self:
            self.packages.remove(package)

    # O(1) for time and space
    def add_miles(self, miles):
        self.miles += miles

    # O(1) for time and space
    def add_time(self, miles_traveled):
        time_to_add = (miles_traveled/18.0) * 60
        self.time = self.time + timedelta(minutes = time_to_add)

    def __iter__(self):
        return iter(self.packages)

