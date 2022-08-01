class SolarSystem():
    def __init__(self):
        self.bodies = []

    def addBody(self, body):
        self.bodies.append(body)

    def removeBody(self, body):
        self.bodies.remove(body)
    
    def setBodies(self, array):
        self.bodies = array

    def update(self, SecondsPerFrame):
        for body in self.bodies:
            body.force.clear()
            for other in self.bodies:
                if (other != body):
                    grav = body.getGravity(other)
                    body.force.update(
                        grav["xForce"], grav["yForce"], grav["zForce"])
            body.update(SecondsPerFrame)
