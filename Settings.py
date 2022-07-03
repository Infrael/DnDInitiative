from AppGUI import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from pathlib import Path
import PartyCreator


class Tavern(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry(f"420x665+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.title("Delicious Goblin")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Settings.jpg"))
        self.campaign_label = ttk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)

        # Active Campaign

        self.campaign_status = ttk.StringVar()

        self.campaign_status_label = ttk.Label(self, textvariable=self.campaign_status, bd=5)
        self.campaign_status_label.place(x=42, y=202, width=333, height=25)

        self.update_campaign_status()

        self.file_browser_button = ttk.Button(self, text="Browse", command=self.browse_for_file)
        self.file_browser_button.place(x=42, y=227, width=333, height=25)

        # New Campaign

        self.hero_list = []

        self.new_campaign_button = ttk.Button(self, text="Start New Adventure", command=self.start_new_adventure)
        self.new_campaign_button.place(x=42, y=333, width=333, height=25)

        self.hero_image_1 = None
        self.hero_label_1 = None
        self.remove_hero_1 = None

        self.add_hero_1 = ttk.Button(self, text="Hire", command=lambda: self.add_hero(1))
        self.add_hero_1.place(x=16, y=575, width=42, height=25)

        self.hero_image_2 = None
        self.hero_label_2 = None
        self.remove_hero_2 = None

        self.add_hero_2 = ttk.Button(self, text="Hire", command=lambda: self.add_hero(2))
        self.add_hero_2.place(x=155, y=575, width=42, height=25)

        self.hero_image_3 = None
        self.hero_label_3 = None
        self.remove_hero_3 = None

        self.add_hero_3 = ttk.Button(self, text="Hire", command=lambda: self.add_hero(3))
        self.add_hero_3.place(x=230, y=575, width=42, height=25)

        self.hero_image_4 = None
        self.hero_label_4 = None
        self.remove_hero_4 = None

        self.add_hero_4 = ttk.Button(self, text="Hire", command=lambda: self.add_hero(4))
        self.add_hero_4.place(x=360, y=575, width=42, height=25)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def browse_for_file(self):
        file_location = askopenfilename()
        if file_location:
            if self.master.database.correct_format_check(file_location):
                self.master.database.update_current_campaign(file_name=Path(file_location).stem)
                self.master.database.save_current_campaign()
            else:
                ttk.messagebox.showerror("Incorrect File Format", "Your Data is stored in .pickle files.\n"
                                                                  "Please select a correct file", parent=self)
                self.browse_for_file()
        if self.winfo_exists() == 1:
            self.update_campaign_status()
            self.focus_set()

    def update_campaign_status(self):
        if self.master.database.current_campaign:
            self.campaign_status_label.config(bg="green")
            self.campaign_status.set(f"{self.master.database.current_campaign.get('campaign')} Campaign Active")
        else:
            self.campaign_status_label.config(bg="#4A7A8C")
            self.campaign_status.set("NO Active Campaign")

    def add_hero(self, number):
        global add_hero_window
        try:
            if add_hero_window.winfo_exists() == 1:
                add_hero_window.focus_set()
            else:
                add_hero_window = PartyCreator.Character(self, number)
        except NameError:
            add_hero_window = PartyCreator.Character(self, number)

    def add_hero_picture(self, chair_number, image_location):
        match chair_number:
            case 1:
                self.hero_image_1 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_1 = ttk.Label(self, image=self.hero_image_1)
                self.hero_label_1.place(x=5, y=465)

                self.remove_hero_1 = ttk.Button(self, text="Fire",
                                                command=lambda: self.remove_hero(chair_number, image_location))
                self.remove_hero_1.place(x=16, y=575, width=42, height=25)
            case 2:
                self.hero_image_2 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_2 = ttk.Label(self, image=self.hero_image_2)
                self.hero_label_2.place(x=125, y=465)

                self.remove_hero_2 = ttk.Button(self, text="Fire",
                                                command=lambda: self.remove_hero(chair_number, image_location))
                self.remove_hero_2.place(x=155, y=575, width=42, height=25)
            case 3:
                self.hero_image_3 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_3 = ttk.Label(self, image=self.hero_image_3)
                self.hero_label_3.place(x=220, y=465)

                self.remove_hero_3 = ttk.Button(self, text="Fire",
                                                command=lambda: self.remove_hero(chair_number, image_location))
                self.remove_hero_3.place(x=230, y=575, width=42, height=25)
            case 4:
                self.hero_image_4 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_4 = ttk.Label(self, image=self.hero_image_4)
                self.hero_label_4.place(x=332, y=465)

                self.remove_hero_4 = ttk.Button(self, text="Fire",
                                                command=lambda: self.remove_hero(chair_number, image_location))
                self.remove_hero_4.place(x=360, y=575, width=42, height=25)

    def remove_hero(self, chair_number, image_location):
        for hero in self.hero_list:
            if hero.image_location == image_location:
                self.hero_list.remove(hero)

        match chair_number:
            case 1:
                self.hero_label_1.destroy()
                self.remove_hero_1.destroy()
            case 2:
                self.hero_label_2.destroy()
                self.remove_hero_2.destroy()
            case 3:
                self.hero_label_3.destroy()
                self.remove_hero_3.destroy()
            case 4:
                self.hero_label_4.destroy()
                self.remove_hero_4.destroy()

    def start_new_adventure(self):
        if not self.hero_list:
            ttk.messagebox.showwarning("No Solo Adventures Please!", "You need to have at least 1 Hero to start.")
            self.focus_set()
        else:
            campaign_name = ttk.simpledialog.askstring("Chapter I", "Please enter a name for your Campaign:")
            if campaign_name:
                new_game = self.master.database.CampaignDTO(campaign=campaign_name, heroes=self.hero_list, quests=[], notes="")
                self.master.database.store_campaign_dto(new_game)
                self.master.database.update_current_campaign(new_game.get('campaign'))
                self.master.database.save_current_campaign()
                self.destroy()
                self.master.launch_campaign_window()

    def on_close(self):
        self.destroy()
        self.master.deiconify()
