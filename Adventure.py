import tkinter as ttk
from PIL import ImageTk, Image


class Campaign(ttk.Toplevel):
    def __init__(self, campaign):
        super(Campaign, self).__init__()
        self.geometry(f"666x333+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.title("Adventure Time")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Campaign.jpg"))
        self.campaign_label = ttk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        if ttk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            self.master.deiconify()
