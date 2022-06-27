import tkinter as ttk
from PIL import ImageTk, Image


class MainWindow(ttk.Tk):
    def __init__(self, active_campaign):
        super(MainWindow, self).__init__()
        self.geometry("666x420+400+150")
        self.title("DI (Dungeon Initiative)")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.main_image = ImageTk.PhotoImage(Image.open("Images/Main.jpg"))
        self.main_label = ttk.Label(image=self.main_image)
        self.main_label.place(relwidth=1, relheight=1)

        """ Main App Buttons """
        self.campaign_button = ttk.Button(text="Campaign", command=self.start_campaign)
        self.campaign_button.place(x=520, y=310, width=95)

        if not active_campaign:
            self.campaign_button["state"] = "disabled"
        else:
            self.campaign_button["state"] = "normal"
            self.campaign_button.focus_set()

        self.tavern_button = ttk.Button(text="Tavern", command=self.tavern)
        self.tavern_button.place(x=520, y=370, width=95)

        """ DEV ACCESS BUTTON """
        # self.test_button = ttk.Button(text="Developer", command=self.test_button)
        # self.test_button.place(x=560, y=15, width=95)

    def start_campaign(self):
        campaign_window = Campaign()

    def tavern(self):
        tavern_window = Tavern()


class Campaign(ttk.Toplevel):
    def __init__(self):
        super(Campaign, self).__init__()
        self.geometry(f"666x333")
        self.title("Adventure Time")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Campaign.jpg"))
        self.campaign_label = ttk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)


class Tavern(ttk.Toplevel):
    def __init__(self):
        super(Tavern, self).__init__()
        self.geometry(f"420x666")
        self.title("Delicious Goblin")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        # self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Campaign.jpg"))
        # self.campaign_label = ttk.Label(self, image=self.campaign_image)
        # self.campaign_label.place(relwidth=1, relheight=1)
