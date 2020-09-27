from solarSystem import SolarSystem
from physicalProperties import *
from body import Body
from renderer import *
import random
import time

loop = False

system = SolarSystem()

def sun():
    mass = 10**21
    radius = random.randint(10**2, 10**3)
    pos = Position(0, 0, 0)
    vel = Velocity(0, 0, 0)
    acc = Acceleration(0, 0, 0)
    force = Force(0, 0, 0)
    sun = Body("Sun", mass, radius, pos, vel, acc, force)
    system.addBody(sun)

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

def ourSystem():
    sun = Body("Sun", 1.989*10**30, 6.9*10000**5, Position(0,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    mercury = Body("Mercury", 3.285*10**23, 4880000, Position(57.9*10**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    venus = Body("venus", 4.867*10**24, 12100000, Position(108.2*10**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    earth = Body("Earth", 5.972*10**24, 12756000, Position(149.6*10**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    mars = Body("Mars", 6.39*10**23, 6790000, Position(227*10**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    jupiter = Body("Jupiter", 1.898*10**27, 142800000, Position(778*10**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    saturn = Body("Saturn", 5.683*10**26, 120000000, Position(1427*10**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    uranus = Body("Uranus", 8.681*10**25, 51810000, Position(2870**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    neptune = Body("Neptune", 1.024*10**26, 49000000, Position(4497*10**6,0,0), Velocity(0,0,0), Acceleration(0,0,0), Force(0,0,0))
    return [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# for body in ourSystem():
#     system.addBody(body)

sun()
for i in range(150):
    props = randomProperties()
    system.addBody(Body(i, props[0], props[1],
                        props[2], props[3], props[4], props[5]))


create(system.bodies)

loop = True

while loop:
    system.update()
    update(system.bodies)
    time.sleep(0.008)
