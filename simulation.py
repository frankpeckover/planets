from solarSystem import SolarSystem
from physicalProperties import Position, Velocity, Acceleration, Force
from body import Body
import random
import numpy

minMass = 1
maxMass = 21
maxRadius = 8
minMaxRange = 4


class Simulation():
    def __init__(self):
        self.solarSystem = SolarSystem()
        sun = Body("Sun", 10**22, maxRadius + 5, Position(0,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0), 'yellow')
        self.solarSystem.setBodies(self.randomBodies(10))
        self.solarSystem.addBody(sun)

    def randomProperties(self):
        massIndex = random.randint(minMass, maxMass)
        mass = 10**massIndex
        radius = (massIndex/maxMass) * maxRadius
        xPos = random.randint(-(10**minMaxRange), 10**minMaxRange)
        yPos = random.randint(-(10**minMaxRange), 10**minMaxRange)
        zPos = random.randint(-(10**minMaxRange), 10**minMaxRange)
        xVel = random.randint(-(10**minMaxRange), 10**minMaxRange)
        yVel = random.randint(-(10**minMaxRange), 10**minMaxRange)
        zVel = random.randint(-(10**minMaxRange), 10**minMaxRange)
        pos = Position(xPos, yPos, zPos)
        vel = Velocity(xVel, yVel, zVel)
        acc = Acceleration(0, 0, 0)
        force = Force(0, 0, 0)
        return [mass, radius, pos, vel, acc, force]

    def randomBodies(self, numberOfBodies):
        arr = []
        for i in range(numberOfBodies):
            props = self.randomProperties()
            newBody = Body('Body: ' + str(i), props[0], props[1],
                                props[2], props[3], props[4], props[5], numpy.random.rand(3,))
            arr.append(newBody)
        return arr

    def stepSimulation(self, SecondsPerFrame):
        self.solarSystem.update(SecondsPerFrame)



