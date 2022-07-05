import tkinter as tk
from tkinter import ttk
import random
from PIL import ImageTk, Image


class Campaign(tk.Toplevel):
    def __init__(self):
        super(Campaign, self).__init__()
        self.geometry(f"666x333+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.title("Adventure Time")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Campaign.jpg"))
        self.campaign_label = tk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)

        # Quests

        self.columns = ('quest', 'type')
        self.quest_tree = ttk.Treeview(self, columns=self.columns, show='headings')
        self.quest_tree.place(x=280, y=5, width=380, height=120)

        self.quest_tree.column("type", width=50, stretch=False)

        self.quest_tree.heading('quest', text='Quest')
        self.quest_tree.heading('type', text='Type')

        self.add_quest_button = tk.Button(self, text="Add Quest", command=self.add_quest)
        self.add_quest_button.place(x=541, y=140, width=100)

        self.complete_quest_button = tk.Button(self, text="Complete Quest", command=self.complete_quest)
        self.complete_quest_button.place(x=541, y=166, width=100)

        # Notes

        self.notes = tk.Text(self, bg="#56626b", fg="white", wrap=tk.WORD)
        self.notes.insert(tk.INSERT, self.master.database.current_campaign.get('notes'))
        self.notes.place(x=5, y=5, width=270, height=323)

        # Roll D20

        self.dice_roll = tk.IntVar()

        self.dice_roll_button = tk.Button(self, text="Roll D20", command=self.roll_d20)
        self.dice_roll_button.place(x=528, y=300, width=69, height=23)

        self.dice_result_label = tk.Label(self, textvariable=self.dice_roll)
        self.dice_result_label.place(x=599, y=300, width=42, height=23)

        # Battle

        self.combat_button = tk.Button(self, text="To Battle!", borderwidth=5, command=self.initiate_combat)
        self.combat_button.place(x=300, y=280, width=69, height=42)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_quest(self):
        pass

    def complete_quest(self):
        pass

    def initiate_combat(self):
        pass

    def roll_d20(self):
        self.dice_roll.set(random.randint(1, 20))

    def on_close(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.database.current_campaign["notes"] = self.notes.get("1.0", tk.END)
            self.master.database.save_current_campaign()
            self.master.destroy()
