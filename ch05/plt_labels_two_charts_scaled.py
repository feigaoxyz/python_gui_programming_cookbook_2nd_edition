import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(12, 5), facecolor='white')

axis = fig.add_subplot(111)

x_values = [1, 2, 3, 4]
y_0 = [6, 7.5, 8, 7.5]
y_1 = [5.5, 6.5, 80, 6]
y_2 = [6.6, 7, 8, 7.1]

t0, = axis.plot(x_values, y_0, color='red')
t1, = axis.plot(x_values, y_1)
t2, = axis.plot(x_values, y_2)

axis.set_xlabel('X')
axis.set_ylabel('Y')
axis.set_ylim(4, 9)

axis.grid()

fig.legend(
    (t0, t1, t2),
    ('First line', 'Second line', 'Third line'),
    'upper right'
)


def _destroy():
    root.quit()
    root.destroy()


root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroy)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side='top', fill='both', expand=1)

root.update()
root.deiconify()
root.mainloop()
