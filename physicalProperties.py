class PhysicalProperty():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return("x: {x} y: {y} z: {z}".format(x=self.x, y=self.y, z=self.z))

class Position(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, xVel, yVel, zVel, SecondsPerFrame):
        self.x += (xVel * SecondsPerFrame)
        self.y += (yVel * SecondsPerFrame)
        self.z += (zVel * SecondsPerFrame)

class Velocity(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, xAcc, yAcc, zAcc, SecondsPerFrame):
        self.x += (xAcc * SecondsPerFrame)
        self.y += (yAcc * SecondsPerFrame)
        self.z += (zAcc * SecondsPerFrame)

class Acceleration(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, xForce, yForce, zForce, mass):
        self.x = (xForce / mass)
        self.y = (yForce / mass)
        self.z = (zForce / mass)

class Force(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def clear(self):
        self.x = 0
        self.y = 0
        self.z = 0
