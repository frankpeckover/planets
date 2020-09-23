class Body():
    def __init__(self, name, physicalProperties):
        self.name = name
        self.physicalProperties = physicalProperties

    def update(self):
        self.physicalProperties.changeAcceleration()