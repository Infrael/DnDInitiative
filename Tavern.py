import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from pathlib import Path
from Characters import Hero


class Tavern(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.database = self.master.database

        self.geometry(f"420x665+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.title("Delicious Goblin")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Settings.jpg"))
        self.campaign_label = tk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)

        # Active Campaign

        self.campaign_status = tk.StringVar()

        self.campaign_status_label = tk.Label(self, textvariable=self.campaign_status, bd=5)
        self.campaign_status_label.place(x=42, y=202, width=333, height=25)

        self.update_campaign_status()

        self.file_browser_button = tk.Button(self, text="Browse", command=self.browse_for_file)
        self.file_browser_button.place(x=42, y=227, width=333, height=25)

        # New Campaign

        self.hero_list = []

        self.new_campaign_button = tk.Button(self, text="Start New Adventure", command=self.start_new_adventure)
        self.new_campaign_button.place(x=42, y=333, width=333, height=25)

        self.hero_image_1 = None
        self.hero_label_1 = None
        self.remove_hero_1 = None

        self.add_hero_1 = tk.Button(self, text="Hire", command=lambda: self.add_hero(1))
        self.add_hero_1.place(x=16, y=575, width=42, height=25)

        self.hero_image_2 = None
        self.hero_label_2 = None
        self.remove_hero_2 = None

        self.add_hero_2 = tk.Button(self, text="Hire", command=lambda: self.add_hero(2))
        self.add_hero_2.place(x=155, y=575, width=42, height=25)

        self.hero_image_3 = None
        self.hero_label_3 = None
        self.remove_hero_3 = None

        self.add_hero_3 = tk.Button(self, text="Hire", command=lambda: self.add_hero(3))
        self.add_hero_3.place(x=230, y=575, width=42, height=25)

        self.hero_image_4 = None
        self.hero_label_4 = None
        self.remove_hero_4 = None

        self.add_hero_4 = tk.Button(self, text="Hire", command=lambda: self.add_hero(4))
        self.add_hero_4.place(x=360, y=575, width=42, height=25)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def browse_for_file(self):
        file_location = askopenfilename()
        if file_location:
            if self.database.correct_format_check(file_location):
                self.database.update_current_campaign(file_name=Path(file_location).stem)
                self.database.save_current_campaign()
            else:
                tk.messagebox.showerror("Incorrect File Format", "Your Data is stored in .pickle files.\n"
                                                                 "Please select a correct file", parent=self)
                self.browse_for_file()
        if self.winfo_exists() == 1:
            self.update_campaign_status()
            self.focus_set()

    def update_campaign_status(self):
        if self.database.current_campaign:
            self.campaign_status_label.config(bg="green")
            self.campaign_status.set(f"{self.database.current_campaign.get('campaign')} Campaign Active")
            self.master.check_for_active_campaign()
        else:
            self.campaign_status_label.config(bg="#4A7A8C")
            self.campaign_status.set("NO Active Campaign")

    def add_hero(self, number):
        global add_hero_window
        try:
            if add_hero_window.winfo_exists() == 1:
                add_hero_window.focus_set()
            else:
                add_hero_window = PartyMember(self, number)
        except NameError:
            add_hero_window = PartyMember(self, number)

    def add_hero_picture(self, chair_number, image_location):
        match chair_number:
            case 1:
                self.hero_image_1 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_1 = tk.Label(self, image=self.hero_image_1)
                self.hero_label_1.place(x=5, y=465)

                self.remove_hero_1 = tk.Button(self, text="Fire",
                                               command=lambda: self.remove_hero(chair_number, image_location))
                self.remove_hero_1.place(x=16, y=575, width=42, height=25)
            case 2:
                self.hero_image_2 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_2 = tk.Label(self, image=self.hero_image_2)
                self.hero_label_2.place(x=125, y=465)

                self.remove_hero_2 = tk.Button(self, text="Fire",
                                               command=lambda: self.remove_hero(chair_number, image_location))
                self.remove_hero_2.place(x=155, y=575, width=42, height=25)
            case 3:
                self.hero_image_3 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_3 = tk.Label(self, image=self.hero_image_3)
                self.hero_label_3.place(x=220, y=465)

                self.remove_hero_3 = tk.Button(self, text="Fire",
                                               command=lambda: self.remove_hero(chair_number, image_location))
                self.remove_hero_3.place(x=230, y=575, width=42, height=25)
            case 4:
                self.hero_image_4 = ImageTk.PhotoImage(Image.open(image_location).resize((80, 80), Image.ANTIALIAS))
                self.hero_label_4 = tk.Label(self, image=self.hero_image_4)
                self.hero_label_4.place(x=332, y=465)

                self.remove_hero_4 = tk.Button(self, text="Fire",
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
            tk.messagebox.showwarning("No Solo Adventures Please!", "You need to have at least 1 Hero to start.")
            self.focus_set()
        else:
            campaign_name = tk.simpledialog.askstring("Chapter I", "Please enter a name for your Campaign:")
            if campaign_name:
                new_game = self.database.CampaignDTO(campaign=campaign_name, heroes=self.hero_list,
                                                     quests=[], notes="")
                self.database.store_campaign_dto(new_game)
                self.database.update_current_campaign(new_game.get('campaign'))
                self.database.save_current_campaign()
                self.master.check_for_active_campaign()
                self.destroy()
                self.master.launch_campaign_window()

    def on_close(self):
        self.master.check_for_active_campaign()
        self.destroy()
        self.master.deiconify()


class PartyMember(tk.Toplevel):
    def __init__(self, tavern, chair_number):
        super().__init__(tavern)
        self.tavern = tavern

        self.geometry(f"200x323+{self.tavern.winfo_x()+100}+{self.tavern.winfo_y()+350}")
        self.title("Who has joined The Party?")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.hero_name_label = tk.Label(self, text="Hero Name:")
        self.hero_name_label.grid(row=0, column=0)

        self.hero_name_entry = tk.Entry(self, width=15)
        self.hero_name_entry.grid(row=0, column=1)
        self.hero_name_entry.focus_set()

        self.hero_image = ImageTk.PhotoImage(Image.open(f"Images/Characters/default_male.jpg"))
        self.hero_label = tk.Label(self, image=self.hero_image)
        self.hero_label.grid(row=1, column=0, columnspan=2)

        self.radio_button_value = tk.StringVar()

        self.gender_male_radio = tk.Radiobutton(self, text="Male", variable=self.radio_button_value,
                                                value="male", command=self.change_hero_image)
        self.gender_male_radio.invoke()
        self.gender_male_radio.grid(row=2, column=0)

        self.gender_female_radio = tk.Radiobutton(self, text="Female", variable=self.radio_button_value,
                                                  value="female", command=self.change_hero_image)
        self.gender_female_radio.deselect()
        self.gender_female_radio.grid(row=2, column=1)

        self.hero_image_browse_button = tk.Button(self, text="OR, Browse For Image (jpg, png)",
                                                  command=self.browse_for_file)
        self.hero_image_browse_button.grid(row=3, column=0, columnspan=2, sticky="WE")

        self.grid_placeholder = tk.Label(self, text="=^.^=")
        self.grid_placeholder.grid(row=4, column=0, columnspan=2)

        self.hero_image_location = "Images/Characters/default_male.jpg"

        self.create_hero_button = tk.Button(self, text="Add to Party", command=lambda: self.add_hero(chair_number))
        self.create_hero_button.grid(row=6, column=0, columnspan=2, sticky="WE")

    def change_hero_image(self):
        if self.radio_button_value.get() == "male":
            default_male = ImageTk.PhotoImage(Image.open("Images/Characters/default_male.jpg"))
            self.hero_label.configure(image=default_male)
            self.hero_label.image = default_male
            self.hero_image_location = "Images/Characters/default_male.jpg"
        else:
            default_female = ImageTk.PhotoImage(Image.open("Images/Characters/default_female.jpg"))
            self.hero_label.configure(image=default_female)
            self.hero_label.image = default_female
            self.hero_image_location = "Images/Characters/default_female.jpg"

    def browse_for_file(self):
        file_location = askopenfilename()
        if file_location:
            self.hero_image = ImageTk.PhotoImage(Image.open(file_location).resize((200, 200), Image.ANTIALIAS))
            self.hero_label.configure(image=self.hero_image)
            self.hero_label.image = self.hero_image
        self.focus_set()
        self.hero_image_location = file_location
        self.gender_male_radio.deselect()
        self.gender_female_radio.deselect()

    def add_hero(self, chair_number):
        if self.hero_name_entry.get():
            name = self.hero_name_entry.get()
            image_location = self.hero_image_location
            self.tavern.hero_list.append(Hero(name, image_location))

            self.tavern.add_hero_picture(chair_number, image_location)

            self.destroy()
        else:
            tk.messagebox.showwarning("Oops", "Please enter the name of the Hero", parent=self)
            self.focus_set()
