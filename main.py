from simulation import Simulation 
from renderer import Renderer
import time

simulation = Simulation()
renderer = Renderer()
fps = 60
running = True

while running:
    simulation.stepSimulation(1/fps)
    renderer.render(simulation.solarSystem)
    time.sleep(1/fps)
