import tkinter as tk
from tkinter import *


def button_pressed(i):
    Window(i, 500, 200)


class Window(Tk):
    def __init__(self, name, w, h):
        super().__init__()
        self.title(name)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)


window = tk.Tk()

greeting = tk.Label(
    text="hallo",
    fg="black",
    background="#34A2FE",
    height=10,
    width=50
)

btn = tk.Button(
    text="hallo",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=lambda m="test": button_pressed(m)
)

greeting.pack(fill=tk.Y, side=tk.LEFT)
btn.pack(fill=tk.X)

window.mainloop()

print("test")