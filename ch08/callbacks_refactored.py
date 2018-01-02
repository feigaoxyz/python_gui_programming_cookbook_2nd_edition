import tkinter as tk


class Callbacks:
    def __init__(self, root):
        self.root = root

    def defaultFileEntries(self):
        self.root.fileEntry.delete(0, tk.END)
        self.root.fileEntry.insert(0, 'Z:\\')  # bogus path
        self.root.fileEntry.config(state='readonly')

        self.root.netwEntry.delete(0, tk.END)
        self.root.netwEntry.insert(0, 'Z:\\Backup')  # bogus path

    # Combobox callback
    def _combo(self, val=0):
        value = self.root.combo.get()
        self.root.scr.insert(tk.INSERT, value + '\n')
