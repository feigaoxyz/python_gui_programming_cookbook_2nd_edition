import tkinter as tk


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.leave)
        self.tip_window = None

        self.id = None
        self.wait_time = 500

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hide_tip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.show_tip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def show_tip(self, event=None):
        """Display text in a tooltip window.
        """
        x = y = 0
        x, y, cx, cy = self.widget.bbox('insert')  # get size of widget
        x += self.widget.winfo_rootx() + 25  # calculate to display tooltip
        y += self.widget.winfo_rooty() + 20  # below and to the right

        self.tip_window = tw = tk.Toplevel(self.widget)  # create new tooltip window

        self.tip_window.wm_overrideredirect(True)  # remove all Window Manager (wm) decorations
        # tw.wm_overrideredirect(False)  # uncomment to see the effect
        self.tip_window.wm_geometry("+%d+%d" % (x, y))  # create window size

        label = tk.Label(
            self.tip_window,
            text=self.text,
            justify=tk.LEFT,
            background="#ffffff",
            relief=tk.SOLID,
            borderwidth=1,
            wraplength=100,
        )
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


win = tk.Tk()

butt1 = tk.Button(
    win,
    text="Button 1"
)
butt1.grid(
    row=0, column=0
)
butt1_tip = ToolTip(butt1, "button 1 tip")


win.mainloop()
