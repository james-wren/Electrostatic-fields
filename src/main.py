from simulation import field_generator as fld
from gui import gui

X, Y = fld.setup_graph(200, 200, 40, 40)
gui.create_window(X, Y)