class PhysicalProperties():
    def __init__(self, xPos, yPos, mass, xVel, yVel, xAcc, yAcc):
        self.xPos = xPos
        self.yPos = yPos
        self.mass = mass

        self.xVel = xVel
        self.yVel = yVel
        self.xAcc = xAcc
        self.yAcc = yAcc

    def changeAcceleration(self, xForce, yForce):
        self.xAcc = xForce / mass
        self.yAcc = yForce / mass

    def updateVelocity(self, deltaTime):
        self.xVel = xVel + xAcc * deltaTime
        self.yVel = yVel + yAcc * deltaTime

    def updatePosition(self, deltaTime):
        self.xPos = xPos + xVel * deltaTime
        self.yPos = yPos + yVel * deltaTime
