import tkinter as tk

win = tk.Tk()

double_data = tk.DoubleVar()
print(double_data.get())  # default value

double_data.set(2.4)
print(type(double_data))

add_doubles = 1.22 + double_data.get()
print(add_doubles)
print(type(add_doubles))
