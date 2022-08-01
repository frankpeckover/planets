import matplotlib.pyplot as plt

class Renderer():
    def __init__(self):
        plt.ion()
        self.figure = plt.figure()
        self.ax = plt.axes(projection='3d')
        self.ax.view_init(30, 145)
        plt.title('Orbitals')
        self.figure.tight_layout()

        #Set fullscreen
        #manager = plt.get_current_fig_manager()
        #manager.full_screen_toggle()
        
        plt.show()

        self.scale = 4

        self.prevX = (-10**self.scale, 10**self.scale)
        self.prevY = (-10**self.scale, 10**self.scale)
        self.prevZ = (-10**self.scale, 10**self.scale)

        self.configureAxes()

    def configureAxes(self):
        plt.axis('off')
        self.ax.set_xlim(self.prevX)
        self.ax.set_ylim(self.prevY)
        self.ax.set_zlim(self.prevZ)
        self.ax.set_facecolor('black')

    def render(self, solarSystem):
        self.prevX = self.ax.get_xlim()
        self.prevY = self.ax.get_ylim()
        self.prevZ = self.ax.get_zlim()
        self.ax.clear()
        for body in solarSystem.bodies:
            self.ax.plot(body.position.x, body.position.y, body.position.z, marker='o', color=body.color, markersize=body.radius, label=body.name)
            self.ax.plot(body.xhistory[-100:], body.yhistory[-100:], body.zhistory[-100:], color=body.color)
        self.configureAxes()
        
        
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()