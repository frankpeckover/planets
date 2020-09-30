from solarSystem import SolarSystem
from physicalProperties import Position, Velocity, Acceleration, Force
from body import Body
from renderer import Renderer
import random
import time

def randomProperties():
    mass = random.randint(10**10, 10**14)
    radius = random.randint(10**1, 10**2)
    xPos = random.randint(-(10**4), 10**4)
    yPos = random.randint(-(10**4), 10**4)
    zPos = random.randint(-(10**4), 10**4)
    xVel = random.randint(-(10**3), 10**3)
    yVel = random.randint(-(10**3), 10**3)
    zVel = random.randint(-(10**3), 10**3)
    pos = Position(xPos, yPos, zPos)
    vel = Velocity(xVel, yVel, zVel)
    acc = Acceleration(0, 0, 0)
    force = Force(0, 0, 0)
    return [mass, radius, pos, vel, acc, force]

def randomBodies(max):
    arr = []
    for i in range(max):
        props = randomProperties()
        newBody = Body(i, props[0], props[1],
                            props[2], props[3], props[4], props[5])
        arr.append(newBody)
    return arr

system = SolarSystem()
sun = Body("Sun", 10**21, 10**3, Position(0,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
system.setBodies(randomBodies(150))
system.addBody(sun)

renderer = Renderer()
renderer.setBodies(system.bodies)
renderer.initialise()

while True:
    if (len(system.bodies) != len(renderer.bodies)):
        renderer.setBodies(system.bodies)
        renderer.initialise()
        print("not equal lengths")
    system.update()
    renderer.update()
    time.sleep(0.008)
