import tkinter

tkinter.Tk()

print(tkinter.StringVar())
print(tkinter.IntVar())
print(tkinter.DoubleVar())
print(tkinter.BooleanVar())

print(tkinter.StringVar().get())
print(tkinter.IntVar().get())
print(tkinter.DoubleVar().get())
print(tkinter.BooleanVar().get())

var = tkinter.Variable()
print(type(var.get()))

var.set(None)
print(var.get())
