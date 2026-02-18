import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#function to get E, im using a list temporily 
# MUST DEAL WITH pos LATER
def get_e(q, pos, x, y):
    dx, dy = x - pos[0], y - pos[1]
    r = np.sqrt(dx**2 + dy**2)

    U = q * dx / r
    V = q * dy / r
    ex = q * dx / r**3
    ey = q * dy / r**3

    return U, V, ex, ey

#I now need to set up my graph with mpl and np
x = np.linspace(-50, 50, 25)
y = np.linspace(-50, 50, 25)
X, Y = np.meshgrid(x, y)

#(q, (x, y)) q is 1 for positive and -1 for negative
charge = (-1, (-3, 0)) #Positive charge at x = -3
q, pos = charge

U, V, ex, ey = get_e(q, pos, X, Y)
M = np.hypot(ex, ey)

#I have ran into a problem, I need to figure out how to 
# get U and, problem is, I have no clue what they are and how to get 
# them from X and Y -NOTEBOOK-22
plt.quiver(X, Y, U, V, M, pivot='tip')
plt.show()
print(M)