from solarSystem import SolarSystem
from physicalProperties import *
from body import Body
from renderer import plotBodies
import random
import time

loop = False

system = SolarSystem()


def randomProperties():
    mass = random.randint(10**6, 10**16)
    radius = random.randint(10, 100)
    xPos = random.randint(-1000, 1000)
    yPos = random.randint(-1000, 1000)
    zPos = random.randint(-1000, 1000)
    xVel = random.randint(-5, 5)
    yVel = random.randint(-5, 5)
    zVel = random.randint(-5, 5)
    pos = Position(xPos, yPos, zPos)
    vel = Velocity(xVel, yVel, zVel)
    acc = Acceleration(0, 0, 0)
    force = Force(0, 0, 0)
    return [mass, radius, pos, vel, acc, force]


for i in range(100):
    props = randomProperties()
    system.addBody(Body(i, props[0], props[1],
                        props[2], props[3], props[4], props[5]))

loop = True

while loop:
    plotBodies(system.bodies)
    system.update()
    time.sleep(0.008)
