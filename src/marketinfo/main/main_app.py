import json
import sys
from tkinter import *

from src.marketinfo.data.get_data import GetData
from src.marketinfo.window import Window


class MainApp(Window):
    def __init__(self):
        super().__init__("name", 500, 200)
        self.attributes("-topmost", 1)

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
        self.drop.pack(padx=20)

        self.btn = Button(self, text="Get Data", command=lambda: self.show_data(crypto), fg="#A23E48",
                          bg="#FFF275")
        self.btn.pack(padx=20)

        self.lbl = Label(self, text=" ")
        self.lbl.pack(pady=50)

        mainloop()

    def show_data(self, cr):
        data = GetData(cr).data
        self.lbl.configure(text=data)
