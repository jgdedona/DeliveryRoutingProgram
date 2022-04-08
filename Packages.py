import csv
import Hash

class Package:
    def __init__(self, packageId, address, city, state, zip, deliveryDeadline, massKilo, notes, status, truck):
        self.packagId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.massKilo = massKilo
        self.notes = notes
        self.status = status
        self.truck = truck

    def __str__(self):
        return str(self.packagId + ', ' + self.address + ', ' + self.city + ', ' + self.state + ', '
                   + self.zip + ', ' + self.deliveryDeadline + ', ' + self.massKilo + ', ' + self.notes
                   + ', ' + self.status + ', ' + self.truck)


def create_package_hash(csv_file):
    packageHash = Hash.HashMap()

    with open(csv_file) as file:
        packageInfo = csv.reader(file, delimiter=',')

        for row in packageInfo:
            if len(row[7]) == 0:
                notes = 'None'
            else:
                notes = row[7]
            packageHash.insert(int(row[0]), Package(row[0], row[1], row[2], row[3], row[4],
                                                        row[5], row[6], notes, 'Hub', row[8]))
            #print(packageHash.search(row[0]))
    return packageHash
