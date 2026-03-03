import tkinter as tk
from tkinter import *
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
    charge_entries = []
    charges_frames = []

    def get_inputs():
            charges = []
            for ci, xi, yi in charge_entries:
                c = int(ci.get())
                x = int(xi.get())
                y = int(yi.get())
                charges.append((c, (x, y)))

            fig = fld.create_quiver(X, Y, charges)
            draw_plot(fig, plot_frame)

    def charge_settings():
        row = Frame(charge_frame)
        row.pack(fill="x", anchor="w")

        charge_label = Label(master=row, text='Charge: ')
        charge_label.pack(side="left")
        charge_var = tk.StringVar()
        charge_var.set(1)
        charge = Entry(master=row, textvariable=charge_var, width=4)
        charge.pack(side="left")

        x_label = Label(master=row, text='X: ')
        x_label.pack(side="left")
        x_var = tk.StringVar()
        x_var.set(100)
        x = Entry(master=row, textvariable=x_var, width=4)
        x.pack(side="left")

        y_label = Label(master=row, text='Y: ')
        y_label.pack(side="left")
        y_var = tk.StringVar()
        y_var.set(100)
        y = Entry(master=row, textvariable=y_var, width=4)
        y.pack(side="left")

        charges_frames.append(row)
        charge_entries.append((charge_var, x_var, y_var))

    def delete_charge():
        charges_frames[-1].destroy()
        charges_frames.pop()
        charge_entries.pop()
    
    window = Tk()
    window.title('Electrostatic Simulation')
    window.state('zoomed')
    
    sidebar = Frame(window, width=200, bg="#f0f0f0")
    sidebar.pack(side="left")

    plot_frame = Frame(window, name="plot_frame", bg="white")
    plot_frame.pack()
    
    button_row = Frame(sidebar)
    button_row.pack(fill="x", anchor="w", padx=10, pady=5)

    charge_frame = Frame(sidebar)
    charge_frame.pack(fill="x", anchor="w", padx=10, pady=5)

    charge_button_frame = Frame(sidebar)
    charge_button_frame.pack(fill="x", anchor="w", padx=10, pady=5)

    add_charge = Button(master = charge_button_frame, height= 2, width=10, text="Add Charge", command=charge_settings)
    add_charge.pack(side="left")

    delete_charge = Button(master = charge_button_frame, height= 2, width=10, text="Delete Charge", command=delete_charge)
    delete_charge.pack(side="left")

    generate_button = Button(master = button_row, height= 2, width=10, text="Plot", command=get_inputs)
    generate_button.pack(side="left")
    window.mainloop()

if __name__ == "__main__":
    create_window(0, 0)