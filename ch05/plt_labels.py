import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(12, 8), facecolor='white')

# axis = fig.add_subplot(111)  # 1 row, 1 column, only graph
axis = fig.add_subplot(211)  # 2 rows, 1 column, top graph

x_values = [1, 2, 3, 4]
y_values = [5, 7, 6, 8]

axis.plot(x_values, y_values)
axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')

# axis.grid()  # default line style
axis.grid(linestyle='-')  # solid grid lines


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
