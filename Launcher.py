from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image


class Launcher(Tk):
    def __init__(self):
        super(Launcher, self).__init__()
        self.geometry("666x420+400+150")
        self.title("DI (Dungeon Initiative)")
        self.iconbitmap('Wanted_Posters/scroll.ico')
        self.resizable(False, False)

        self.launcher_image = ImageTk.PhotoImage(Image.open("Wanted_Posters/launcher.jpg"))
        self.launcher_label = Label(image=self.launcher_image)
        self.launcher_label.place(relwidth=1, relheight=1)

        """ Main App Buttons """
        self.battle_button = ttk.Button(text="Campaign", command=battle_configuration)
        self.battle_button.place(x=520, y=310, width=95)
        self.battle_button.focus_set()

        self.settings_button = ttk.Button(text="Tavern", command=delicious_goblin)
        self.settings_button.place(x=520, y=370, width=95)

        """ DEV ACCESS BUTTON """
        # self.test_button = ttk.Button(text="Developer", command=self.test_button)
        # self.test_button.place(x=560, y=15, width=95)


def battle_configuration():
    pass


def delicious_goblin():
    pass