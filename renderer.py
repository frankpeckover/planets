from vpython import *
import time

visuals = []
loop = False

def create(bodies):
    data = bodies
    scene = canvas(width = 1920 * 0.75, height = 1080 * 0.75, center = vector(0,0,0))
    for body in data:
        newBody = sphere(canvas=scene, pos=vector(body.position.x, body.position.y, body.position.z), radius=body.radius, color=color.red)
        visuals.append(newBody) 
    scene.camera.follow(visuals[0])

def update(bodies):
    for i in range(len(bodies)):
        visuals[i].pos.x = bodies[i].position.x
        visuals[i].pos.y = bodies[i].position.y
        visuals[i].pos.z = bodies[i].position.z
    time.sleep(0.08)