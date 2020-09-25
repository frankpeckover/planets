class PhysicalProperty():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Position(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, xVel, yVel, zVel, deltaTime):
        self.x = self.x + (xVel * deltaTime)
        self.y = self.y + (yVel * deltaTime)
        self.z = self.z + (zVel * deltaTime)

class Velocity(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, xAcc, yAcc, zAcc, deltaTime):
        self.x = self.x + (xAcc * deltaTime)
        self.y = self.y + (yAcc * deltaTime)
        self.z = self.z + (zAcc * deltaTime)

class Acceleration(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, xForce, yForce, zForce, mass):
        self.x = self.x + (xForce / mass)
        self.y = self.y + (yForce / mass)
        self.z = self.z + (zForce / mass)
