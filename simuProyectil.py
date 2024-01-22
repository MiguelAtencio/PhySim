import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation

# physical constants (in arbitrary units)
GRAV = 1
DRAG = .01 * GRAV

# initial position, velocity; acceleration
x0, y0 = 0., 0.
v0, alpha0 = 5., 69
ax, ay = -DRAG, -DRAG - GRAV

# projection of velocity
v0x = v0 * math.cos(math.radians(alpha0))
v0y = v0 * math.sin(math.radians(alpha0))

# maximum distance and height, time of flight to ground
t_max = 2. * v0 * math.sin(math.radians(alpha0)) / GRAV
x_max = v0 ** 2 * math.sin(2. * math.radians(alpha0)) / GRAV
y_max = (v0 * math.sin(math.radians(alpha0))) ** 2 / (2. * GRAV)
print(t_max, x_max, y_max)

# rounding up
x_max, y_max = math.ceil(x_max), math.ceil(y_max)

# time interval
t = np.linspace(0., t_max)
#print(t)

# kinematic equations: position and velocity
x = x0 + v0x * t + .5 * ax * t ** 2
y = y0 + v0y * t + .5 * ay * t ** 2

vx = v0x + ax * t
vy = v0y + ay * t

# plot setup: axis, labels, title, grid, etc.
fig = plt.figure()
ax = plt.axes(autoscale_on=False, xlim=(0, x_max), ylim=(0, y_max))
ax.set(xlabel='x [a.u.]', ylabel='y [a.u.]', title='Projectile motion')
#ax.set_aspect('equal')
ax.grid()

# line points setup, time template, points on top of axes
line, = ax.plot([], [], 'p-', c='blue', lw=0)
line.set_clip_on(False)
time_template = 'time = %.1f a.u.'
time_text = ax.text(0.4, 0.1, '', transform=ax.transAxes)
xdata, ydata = [], []

# helper functions for animation

def init():
    line.set_data(xdata, ydata)
    time_text.set_text('')
    return line, time_text

def animate(i):
    if y[i] >= 0.:
        xdata.append(x[i])
        ydata.append(y[i])

        line.set_data(xdata, ydata)
    time_text.set_text(time_template % t[i])
    return line, time_text

# animation setup using helper functions
ani = animation.FuncAnimation(fig, animate, range(len(y)), repeat=False,
                              interval=10, blit=False, init_func=init)
plt.show()