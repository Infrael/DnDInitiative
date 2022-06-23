from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class MainWindow(Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry("666x420+400+150")
        self.title("DI (Dungeon Initiative)")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.launcher_image = ImageTk.PhotoImage(Image.open("Images/Main.jpg"))
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


class Campaign(Toplevel):
    def __init__(self):
        super(Campaign, self).__init__()
        self.geometry(f"666x333+{launcher.winfo_x()}+{launcher.winfo_y()}")
        self.title("Battle Settings")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.encounter_image = ImageTk.PhotoImage(Image.open("Images/Campaign.jpg"))
        self.encounter_label = Label(self, image=self.encounter_image)
        self.encounter_label.place(relwidth=1, relheight=1)


def battle_configuration():
    campaign_window = Campaign()


def delicious_goblin():
    pass


launcher = MainWindow()
launcher.mainloop()
