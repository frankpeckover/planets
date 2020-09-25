from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

plt.ion()
figure = plt.figure(figsize=(16, 8))
axis = Axes3D(figure)
axis.axis('off')
axis.set_xlim3d(-1000, 1000)
axis.set_ylim3d(-1000, 1000)
axis.set_zlim3d(-1000, 1000)
axis.set_frame_on(False)
plt.show()

#ani = animation.FuncAnimation(figure, update, gen)


def plotBodies(bodies):
    x = []
    y = []
    z = []
    n = []
    r = []

    for body in bodies:
        x.append(body.position.x)
        y.append(body.position.y)
        z.append(body.position.z)
        n.append(body.name)
        r.append(body.radius)

    axis.clear()
    axis.scatter(x, y, z, s=r)
    axis.axis('off')
    plt.pause(0.008)
