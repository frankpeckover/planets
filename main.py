from solarSystem import SolarSystem
from physicalProperties import PhysicalProperties
from body import Body

sunPhysical = PhysicalProperties(0, 0, 100, 0, 0, 0, 0)
earthPhysical = PhysicalProperties(1, 1, 12, 2, -4, 2, 2)
sun = Body(sunPhysical)
earth = Body(earthPhysical)

system = SolarSystem([sun, earth])
print(system.getDistance(system.bodies[0], system.bodies[1]))
print(system.getGravity(system.bodies[0], system.bodies[1]))
