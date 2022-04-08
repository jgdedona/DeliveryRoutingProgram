class Truck:
    def __init__(self):
        self.packages = []
        self.miles = 0

    def add_package(self, package):
        self.packages.append(package)

    def remove_package(self, package):
        if package in self:
            self.packages.remove(package)

    def add_miles(self, miles):
        self.miles += miles

    def __iter__(self):
        return iter(self.packages)

