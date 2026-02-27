import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


# function to get e (pos and q is passed as a nested tuple in a list, as follows [(q, (x, y))])
# x and y are the locations of the current point.
def get_e(q, pos, x, y):
    dx, dy = x - pos[0], y - pos[1] # calculates the distance for x and y axis
    r = np.sqrt(dx**2 + dy**2) # gets the hyponetues (is that how you spell that?) of the previous two distances.

    ex = q * dx/ r**3 # plugs values into electrofield equation, adjusted to account for direction and assuming k is 1.
    ey = q * dy/ r**3

    return ex, ey

# function to calculate the value for each point, charges is the same tuple mentioned in line 5
def calc_field(charges, X, Y):
    ex, ey = np.zeros(X.shape), np.zeros(Y.shape) # initiates ex and ey by seting them to zeros in the shape of X and Y arrays
    for q, pos in charges: # divides the tuple into two variables while looping for the amount of them.
        ex_add, ey_add = get_e(q, pos, X, Y) # Temporarily sets ex_add and ey_add to their respective values
        ex += ex_add # adds the temp values to the summation.
        ey += ey_add
    m = np.sqrt(ex**2 + ey**2)
    ex = ex / m
    ey = ey / m
    return ex, ey, m # returns the summed ex, ey, and M (the calculation is done inline.)


# START OF SCRIPT RUNNING
# Sets up graph
def setup_graph(width, height, interval_x, interval_y):
    x = np.linspace(0, width, interval_x) # Sets x and y values
    y = np.linspace(0, height, interval_y)
    X, Y = np.meshgrid(x, y) # Turns previous values into mesh grid
    return X, Y

# Defining charges
# (q, (x, y)) q is 1 for positive and -1 for negative

def create_quiver(X, Y, charges):
    Un, Vn, M = calc_field(charges, X, Y) # calls the calc field function and assigns the respective values
    norm = mpl.colors.LogNorm(vmin=1e-4, vmax=1.0) # Normalizes color map
    # Graphs the previous values on a quiver
    fig = Figure(figsize= (10,10), dpi=100)
    plot = fig.add_subplot(111)
    plot.quiver(X, Y, Un, Vn, M, norm=norm, cmap='CMRmap', pivot='middle', width=0.002, headwidth=2, headlength=2, headaxislength=2)
    return fig