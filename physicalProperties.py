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

    def update(self, xVel, yVel, zVel, deltaTime):
        self.x += (xVel * deltaTime)
        self.y += (yVel * deltaTime)
        self.z += (zVel * deltaTime)


class Velocity(PhysicalProperty):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def update(self, xAcc, yAcc, zAcc, deltaTime):
        self.x += (xAcc * deltaTime)
        self.y += (yAcc * deltaTime)
        self.z += (zAcc * deltaTime)


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
