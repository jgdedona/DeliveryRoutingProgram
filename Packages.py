class Package:
    def __init__(self, packageId, address, city, state, zip, deliveryDeadline, massKilo, notes, status):
        self.packagId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.massKilo = massKilo
        self.notes = notes
        self.status = status

    def __str__(self):
        return str(self.packagId + ', ' + self.address + ', ' + self.city + ', ' + self.state + ', '
                   + self.zip + ', ' + self.deliveryDeadline + ', ' + self.massKilo + ', ' + self.notes
                   + ', ' + self.status)
