from solarSystem import SolarSystem
from physicalProperties import *
from body import Body
from renderer import plotBodies
import random
import time

def randomProperties():
    mass = random.randint(10, 1000)
    radius = random.randint(10, 50)
    xPos = random.randint(600 * 0.25, 600 * 0.75)
    yPos = random.randint(600 * 0.25, 600 * 0.75)
    zPos = random.randint(600 * 0.25, 600 * 0.75)
    xVel = random.randint(-50, 50)
    yVel = random.randint(-50, 50)
    zVel = random.randint(-50, 50)
    pos = Position(xPos, yPos, zPos)
    vel = Velocity(xVel, yVel, zVel)
    acc = Acceleration(0, 0, 0)
    return [mass, radius, pos, vel, acc]

system = SolarSystem()

for x in range(10):
    props = randomProperties()
    system.addBody(Body(x, props[0], props[1], props[2], props[3], props[4]))

plotBodies(system.bodies)

while 1:
    system.update()
    plotBodies(system.bodies)