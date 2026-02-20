import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#function to get E, im using a list temporily 
# MUST DEAL WITH PASSING pos LATER
def get_e(q, pos, x, y):
    dx, dy = x - pos[0], y - pos[1]
    r = np.sqrt(dx**2 + dy**2)

    U = q * dx/ r**2
    V = q * dy/ r **2
    ex = q * dx / r**3
    ey = q * dy / r**3

    return U, V, ex, ey

def find_points(charges):
    U, V, M = None, None, None
    first = True
    for q, pos in charges:
        u, v, ex, ey = get_e(q, pos, X, Y)
        m = np.hypot(ex, ey)
        m = m.flatten()
        if not first:
            U = U + u
            V = (V + v)
            M = (M + m)
        else:
            U = u
            V = v
            M = m
            first = False
    return U, V, M

#I now need to set up my graph with mpl and np
x = np.linspace(-50, 50, 25)
y = np.linspace(-50, 50, 25)
X, Y = np.meshgrid(x, y)

#Defining charges
#(q, (x, y)) q is 1 for positive and -1 for negative
charges = [(-1, (-3, 0)), (1, (3, 0))] #Positive charge at x = -3

# Getting the points from a charge, will need to be able to average points later
#Creates color map, need to figure out how to normalize it
#Turns the 2d array into a 1d array, better for later nomalization
U, V, M = find_points(charges)
norm = mpl.colors.LogNorm(vmin=1e-4, vmax=1.0)

#plots the map
plt.quiver(X, Y, U, V, M, norm=norm, cmap='plasma', pivot='tip')
plt.show()