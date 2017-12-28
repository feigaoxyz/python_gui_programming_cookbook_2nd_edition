from tkinter import messagebox as msg, Tk

root = Tk()
root.wm_withdraw()

msg.showinfo(
    'This is a Title',
    'Python GUI created using tkinter:\nThe year is 2017'
)
