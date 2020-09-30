import math
import time


class SolarSystem():
    def __init__(self):
        self.bodies = []
        self.initialTime = time.perf_counter()

    def addBody(self, body):
        self.bodies.append(body)

    def removeBody(self, body):
        self.bodies.remove(body)
    
    def setBodies(self, array):
        self.bodies = array

    def update(self):
        for body in self.bodies:
            body.force.clear()
            for other in self.bodies:
                if (other != body):
                    grav = body.getGravity(other)
                    body.force.update(
                        grav["xForce"], grav["yForce"], grav["zForce"])
                    if (body.hasCollided(other) or abs(body.position.x) > 10**4 * 2 or abs(body.position.y) > 10**4 * 2 or abs(body.position.z) > 10**4 * 2):
                        self.removeBody(body)
                        print("collision happened or out of bounds")
                        return
            body.update(0.16)
