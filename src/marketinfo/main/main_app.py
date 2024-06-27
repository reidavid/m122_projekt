import json
import sys
from tkinter import *

from src.marketinfo.data.get_data import GetData
from src.marketinfo.window import Window


class MainApp(Window):
    def __init__(self):
        super().__init__("name", 500, 400)
        self.attributes("-topmost", 1)

        # colors
        primary = "#6C8EAD"
        secondary = "#A23E48"
        secondary_fg = "white"

        self["bg"]=primary

        options = [
            "BTC",
            "ETH",
            "ASD",
            "SDF",
            "DFG"
        ] # wahrscheinlich value zu key hinzufügen für filter in data

        crypto = StringVar()
        crypto.set("Select Currency")

        self.drop = OptionMenu(self, crypto, *options)
        self.drop["bg"]=secondary
        self.drop["fg"]=secondary_fg
        self.drop.pack(padx=20, pady=5)

        self.btn = Button(self, text="Get Data", command=lambda: self.show_data(crypto), fg=secondary_fg,
                          bg=secondary, height=3, width=9)
        self.btn.pack(padx=20, pady=5)

        self.lbl = Label(self, text="", wraplength=400, height= 300, width= 400)
        self.lbl.pack(pady=20)

        mainloop()

    def show_data(self, cr):
        data = GetData(cr).data
        self.lbl["text"]=data
