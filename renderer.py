from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

plt.ion()
fig = plt.figure()
ax = plt.axes(projection="3d")
plt.axis('off')
fig.show()
fig.canvas.draw()

def plotBodies(bodies):
    x = []
    y = []
    z = []
    
    for body in bodies:
        x.append(body.position.x)
        y.append(body.position.y)
        z.append(body.position.z)
    
    ax.clear()
    ax.scatter( x, y, z, "r+" )
    fig.canvas.draw()
    plt.pause(0.05)

    
