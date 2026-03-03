from simulation import field_generator as fld
from gui import gui

X, Y = fld.setup_graph(100, 100, 25, 25)
gui.create_window(X, Y)