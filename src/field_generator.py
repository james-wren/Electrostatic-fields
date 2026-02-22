import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# function to get E, im using a list temporily 
# MUST DEAL WITH PASSING pos LATER
def get_e(q, pos, x, y):
    dx, dy = x - pos[0], y - pos[1]
    r2 = dx**2 + dy**2

    r = np.sqrt(r2)
    r[r < 1e-6] = 1e-6  # Avoid division by zero

    ex = q * dx/ r2**1.5
    ey = q * dy/ r2**1.5

    return ex, ey

def calc_feild(charges):
    ex, ey = np.zeros(X.shape), np.zeros(Y.shape)
    for q, pos in charges:
        ex_add, ey_add = get_e(q, pos, X, Y)
        ex += ex_add
        ey += ey_add

    return ex, ey, np.sqrt(ex**2 + ey**2)

# I now need to set up my graph with mpl and np
x = np.linspace(-100, 100, 40)
y = np.linspace(-100, 100, 40)
X, Y = np.meshgrid(x, y)

# Defining charges
# (q, (x, y)) q is 1 for positive and -1 for negative
# charges = [(-1, (-10, 0)), (1, (10, 5)), (1, (-10, 20))] #Positive charge at x = -3
charges = [(-1, (-19, 93)), (1, (-32, 20)), (1, (-14, 62)), (-1, (-68, -55)), (-1, (-33, 11)), (-1, (-46, -5)), (1, (-30, -46)), (-1, (-96, -83)), (-1, (86, 46)), (1, (30, -14))]

# Getting the points from a charge, will need to be able to average points later
# Creates color map, need to figure out how to normalize it
# Turns the 2d array into a 1d array, better for later nomalization
U, V, M = calc_feild(charges)
Un = U / M
Vn = V / M
norm = mpl.colors.LogNorm(vmin=1e-4, vmax=1.0)

#plots the map
plt.quiver(X, Y, Un, Vn, M, norm=norm, cmap='CMRmap', pivot='middle', width=0.002, headwidth=2, headlength=2, headaxislength=2)
plt.show()