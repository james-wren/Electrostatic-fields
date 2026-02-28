import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from simulation import field_generator as fld


def draw_plot(fig, window):
    children = window.winfo_children()
    for child in children:
        if isinstance(child, tk.Canvas):
            child.destroy()
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def create_window(X, Y):
    def get_inputs():
            charges = [(int(charge_var.get()), (int(x_var.get()), int(y_var.get())))]
            fig = fld.create_quiver(X, Y, charges)
            draw_plot(fig, window)
    
    window = Tk()
    window.title('Electrostatic Simulation')
    window.state('zoomed')


    charge_label = Label(master=window, text='Charge: ')
    charge_label.pack()
    charge_var = tk.StringVar()
    charge_var.set(1)
    charge = Entry(master=window, textvariable=charge_var, width=2)
    charge.pack()

    x_label = Label(master=window, text='Charge: ')
    x_label.pack()
    x_var = tk.StringVar()
    x_var.set(100)
    x = Entry(master=window, textvariable=x_var, width=2)
    x.pack()

    y_label = Label(master=window, text='Charge: ')
    y_label.pack()
    y_var = tk.StringVar()
    y_var.set(100)
    y = Entry(master=window, textvariable=y_var, width=2)
    y.pack()

    generate_button = Button(master= window, height= 2, width=10, text="Plot", command=get_inputs)
    generate_button.pack()
    window.mainloop()
