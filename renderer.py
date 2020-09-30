from vpython import *
import time

class Renderer():
    def __init__(self):
        self.visuals = []
        self.bodies = []
        self.scene = canvas(width = 1920 * 0.9, height = 1080 * 0.9, center = vector(0,0,0), background = color.black)

    def setBodies(self, bodies):
        self.bodies = bodies
        return True

    def initialise(self):
        self.visuals = []
        for obj in scene.objects:
            del obj
        for body in self.bodies:
            newBody = sphere(canvas=self.scene, pos=vector(body.position.x, body.position.y, body.position.z), radius=body.radius, color=color.red)
            self.visuals.append(newBody)
        self.scene.autoscale = False

    def update(self):
        for i in range(len(self.bodies)):
            self.visuals[i].pos.x = self.bodies[i].position.x
            self.visuals[i].pos.y = self.bodies[i].position.y
            self.visuals[i].pos.z = self.bodies[i].position.z