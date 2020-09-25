import math
GRAVITY_CONST = 6.67408e-11


class Body():
    def __init__(self, name, mass, radius, position, velocity, acceleration, force):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.force = force

    def update(self, deltaTime):
        self.acceleration.update(
            self.force.x, self.force.y, self.force.z, self.mass)
        self.velocity.update(
            self.acceleration.x, self.acceleration.y, self.acceleration.z, deltaTime)
        self.position.update(self.velocity.x, self.velocity.y,
                             self.velocity.z, deltaTime)

    def getDistance(self, other):
        xDist = self.position.x - other.position.x
        yDist = self.position.y - other.position.y
        zDist = self.position.z - other.position.z
        magnitude = ((xDist ** 2) + (yDist ** 2) + (zDist ** 2)) ** (1/2)
        unitVector = [xDist / magnitude, yDist / magnitude, zDist / magnitude]
        return {"magnitude": magnitude, "unitVector": unitVector}

    def getGravity(self, other):
        dist = self.getDistance(other)
        numerator = (-1 * GRAVITY_CONST) * self.mass * other.mass
        denominator = dist["magnitude"] ** 2
        magnitude = numerator/denominator
        xForce = magnitude * dist["unitVector"][0]
        yForce = magnitude * dist["unitVector"][1]
        zForce = magnitude * dist["unitVector"][2]
        return {"magnitude": magnitude, "xForce": xForce, "yForce": yForce, "zForce": zForce}
