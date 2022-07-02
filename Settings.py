import tkinter as ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


class Tavern(ttk.Toplevel):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.geometry(f"420x666+{position_x}+{position_y}")
        self.title("Delicious Goblin")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Settings.jpg"))
        self.campaign_label = ttk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)

        self.campaign_status = ttk.StringVar()

        self.campaign_status_label = ttk.Label(self, textvariable=self.campaign_status, bd=5)
        self.campaign_status_label.place(x=42, y=148, width=250, height=25)

        self.update_campaign_status()

        self.file_browser_button = ttk.Button(self, text="Browse", command=self.browse_for_file)
        self.file_browser_button.place(x=305, y=148, width=85, height=25)

    def browse_for_file(self):
        file_location = askopenfilename()
        if file_location:
            if self.master.database.correct_format_check(file_location):
                self.master.check_for_current_campaign()
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
            self.campaign_status.set("Campaign Active")
        else:
            self.campaign_status_label.config(bg="#4A7A8C")
            self.campaign_status.set("NO Active Campaign")

