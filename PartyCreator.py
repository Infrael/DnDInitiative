from AppGUI import tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from Characters import Hero


class Character(tk.Toplevel):
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
