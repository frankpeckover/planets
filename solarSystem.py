import math
import time


class SolarSystem():
    def __init__(self):
        self.bodies = []
        self.initialTime = time.perf_counter()

    def addBody(self, body):
        self.bodies.append(body)

    def update(self):
        for body in self.bodies:
            body.force.clear()
            for other in self.bodies:
                if (other != body):
                    grav = body.getGravity(other)
                    body.force.update(
                        grav["xForce"], grav["yForce"], grav["zForce"])
            body.update(0.16)
