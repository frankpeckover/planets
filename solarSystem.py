import math
import time

class SolarSystem():
    def __init__(self):
        self.bodies = []
        self.initialTime = time.perf_counter()
            
    def addBody(self, body):
        self.bodies.append(body)

    def update(self):
        deltaTime = time.perf_counter() - self.initialTime
        for body in self.bodies:
            for other in self.bodies:
                if (other != body):
                    grav = body.getGravity(other)
                    body.update(grav["xForce"], grav["yForce"], grav["zForce"], deltaTime)
        self.initialTime = time.perf_counter()