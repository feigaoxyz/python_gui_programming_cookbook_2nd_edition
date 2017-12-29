import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(12, 8), facecolor='white')

# axis = fig.add_subplot(111)  # 1 row, 1 column, only graph
axis = fig.add_subplot(211)  # 2 rows, 1 column, top graph

x_values = [1, 2, 3, 4]
y_values = [5, 7, 6, 8]

axis.plot(x_values, y_values)
axis.set_xlabel('Horizontal Label 1')
axis.set_ylabel('Vertical Label 1')
axis.grid(linestyle='-')  # solid grid lines

axis1 = fig.add_subplot(212)
x_values1 = x_values[:]
y_values1 = y_values[::-1]
axis1.plot(x_values1, y_values1)
axis1.set_xlabel('Horizontal Label 2')
axis1.set_ylabel('Vertical Label 2')
axis1.grid(linestyle='--')


def _destroy_window():
    root.quit()
    root.destroy()


root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroy_window)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()
