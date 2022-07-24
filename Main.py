import tkinter as tk
from PIL import ImageTk, Image
from Tavern import Tavern
from Campaign import Campaign
import Database


class MainWindow(tk.Tk):
    def __init__(self, database):
        super().__init__()
        self.geometry("666x420+400+150")
        self.title("DI (Dungeon Initiative)")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)
        self.database = database

        self.main_image = ImageTk.PhotoImage(Image.open("Images/Main.jpg"))
        self.main_label = tk.Label(image=self.main_image)
        self.main_label.place(relwidth=1, relheight=1)

        # App Buttons

        self.campaign_button = tk.Button(text="Campaign", command=self.launch_campaign_window)
        self.campaign_button.place(x=520, y=340, width=95)

        self.tavern_button = tk.Button(text="Tavern", command=self.launch_tavern_window)
        self.tavern_button.place(x=520, y=370, width=95)

        self.check_for_active_campaign()

    def launch_campaign_window(self):
        global campaign_window
        try:
            if campaign_window.winfo_exists() == 1:
                campaign_window.focus_set()
            else:
                campaign_window = Campaign()
                self.iconify()
        except NameError:
            campaign_window = Campaign()
            self.iconify()

    def launch_tavern_window(self):
        global tavern_window
        try:
            if tavern_window.winfo_exists() == 1:
                tavern_window.focus_set()
            else:
                tavern_window = Tavern()
                self.iconify()
        except NameError:
            tavern_window = Tavern()
            self.iconify()

    def check_for_active_campaign(self):
        self.database.update_current_campaign()

        if not self.database.current_campaign:
            self.campaign_button["state"] = "disabled"
            self.tavern_button.focus_set()
        else:
            self.campaign_button["state"] = "normal"
            self.campaign_button.focus_set()


if __name__ == "__main__":
    active_database = Database.Storage()
    launcher = MainWindow(active_database)
    launcher.mainloop()
