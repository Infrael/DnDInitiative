import tkinter
from tkinter import *
from PIL import ImageTk, Image


class BattleConfiguration(tkinter.Toplevel):
    def __init__(self):
        super(BattleConfiguration, self).__init__()
        self.geometry(f"666x333+{launcher.winfo_x()}+{launcher.winfo_y()}")
        self.title("Battle Settings")
        self.iconbitmap('Wanted_Posters/scroll.ico')
        self.resizable(False, False)

        self.encounter_image = ImageTk.PhotoImage(Image.open("Wanted_Posters/combat.jpg"))
        self.encounter_label = Label(self, image=self.encounter_image)
        self.encounter_label.place(relwidth=1, relheight=1)
