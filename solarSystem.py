import math

GRAVITY_CONST = 6.67408 * (10 ** -11)

class SolarSystem():
    def __init__(self, bodies):
        self.bodies = bodies

    def getDistance(self, x, y):
        xDist = x.physicalProperties.xPos - y.physicalProperties.xPos
        yDist = x.physicalProperties.yPos - y.physicalProperties.yPos
        magnitude = ((xDist ** 2) + (yDist ** 2)) ** (1/2)
        angle = math.atan(yDist/xDist)
        return {"magnitude": magnitude, "angle": angle, "xDist": xDist, "yDist": yDist }

    def getGravity(self, x, y):
        dist = self.getDistance(x, y)
        numerator = GRAVITY_CONST * x.physicalProperties.mass * y.physicalProperties.mass
        denominator = dist["magnitude"] ** 2
        magnitude = numerator/denominator
        xForce = math.cos(math.degrees(dist["angle"])) * magnitude
        yForce = math.sin(math.degrees(dist["angle"])) * magnitude
        return {"magnitude": magnitude, "xForce": xForce, "yForce": yForce}

    def update(self):
        for body in self.bodies:
            return