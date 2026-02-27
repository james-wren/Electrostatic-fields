import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def draw_plot(fig, window):
    children = window.winfo_children()
    for child in children:
        if isinstance(child, tk.Canvas):
            child.destroy()
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def create_window(fig):
    window = Tk()
    window.title('Electrostatic Simulation')
    window.geometry("1000x1000")

    generate_button = Button(master= window, height= 2, width=10, text="Plot", command=lambda: draw_plot(fig, window))

    generate_button.pack()
    window.mainloop()