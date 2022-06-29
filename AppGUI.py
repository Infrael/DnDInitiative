import tkinter as ttk
import Settings
import Adventure
import Database
from PIL import ImageTk, Image


class MainWindow(ttk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry("666x420+400+150")
        self.title("DI (Dungeon Initiative)")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.main_image = ImageTk.PhotoImage(Image.open("Images/Main.jpg"))
        self.main_label = ttk.Label(image=self.main_image)
        self.main_label.place(relwidth=1, relheight=1)

        """ Main App Buttons """
        self.campaign_button = ttk.Button(text="Campaign", command=self.launch_campaign_window)
        self.campaign_button.place(x=520, y=340, width=95)

        self.tavern_button = ttk.Button(text="Tavern", command=self.launch_settings_window)
        self.tavern_button.place(x=520, y=370, width=95)

        try:
            self.current_campaign = Database.get_data("current_campaign")
        except FileNotFoundError:
            self.current_campaign = False

        if not self.current_campaign:
            self.campaign_button["state"] = "disabled"
            self.tavern_button.focus_set()
        else:
            self.campaign_button["state"] = "normal"
            self.campaign_button.focus_set()

        """ DEV ACCESS BUTTON """
        # self.test_button = ttk.Button(text="Developer", command=self.test_button)
        # self.test_button.place(x=560, y=15, width=95)

    def launch_campaign_window(self):
        global campaign_window
        try:
            if campaign_window.winfo_exists() == 1:
                campaign_window.focus_set()
            else:
                campaign_window = Adventure.Campaign(self.winfo_x(), self.winfo_y())
        except NameError:
            campaign_window = Adventure.Campaign(self.winfo_x(), self.winfo_y())

    def launch_settings_window(self):
        global tavern_window
        try:
            if tavern_window.winfo_exists() == 1:
                tavern_window.focus_set()
            else:
                tavern_window = Settings.Tavern(self.winfo_x(), self.winfo_y())
        except NameError:
            tavern_window = Settings.Tavern(self.winfo_x(), self.winfo_y())
