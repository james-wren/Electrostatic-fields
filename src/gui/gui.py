import sys
from tkinter import *
from simulation import field_generator as fld

# root = Tk()
# a = Label(root, text="Hello World!")
# a.pack()

# root.mainloop()

X, Y = fld.setup_graph(200, 200, 40, 40)
fld.create_quiver(X, Y)