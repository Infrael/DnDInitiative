import tkinter as ttk
from PIL import ImageTk, Image


class Tavern(ttk.Toplevel):
    def __init__(self, position_x, position_y):
        super(Tavern, self).__init__()
        self.geometry(f"420x666+{position_x}+{position_y}")
        self.title("Delicious Goblin")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Settings.jpg"))
        self.campaign_label = ttk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)
