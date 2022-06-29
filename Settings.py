import tkinter as ttk
from tkinter.filedialog import askopenfilename
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

        self.file_browser = ttk.Entry(self, width=42)
        self.file_browser.place(x=42, y=150)
        self.file_browser.insert(ttk.END, "C:\\*Your Campaign Location*")

        self.file_browser_button = ttk.Button(self, text="Browse", command=self.browse_for_file)
        self.file_browser_button.place(x=305, y=148, width=85, height=25)

    def browse_for_file(self):
        file_location = askopenfilename()[:-7]
        self.focus_set()
        self.file_browser.delete(0, 'end')
        self.file_browser.insert(ttk.END, file_location)

