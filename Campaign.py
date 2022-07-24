import tkinter as tk
from tkinter import ttk, END
from random import randint
from PIL import ImageTk, Image


class Campaign(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.database = self.master.database

        self.geometry(f"666x333+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.title("Adventure Time")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.campaign_image = ImageTk.PhotoImage(Image.open("Images/Campaign.jpg"))
        self.campaign_label = tk.Label(self, image=self.campaign_image)
        self.campaign_label.place(relwidth=1, relheight=1)

        # Quests

        self.columns = ('quest', 'type', "notes")
        self.quest_tree = ttk.Treeview(self, columns=self.columns, show='headings')
        self.quest_tree.place(x=280, y=5, width=380, height=120)

        self.quest_tree.column("type", width=50, stretch=False)

        self.quest_tree.heading('quest', text='Quest')
        self.quest_tree.heading('type', text='Type')
        self.quest_tree["displaycolumns"] = ("quest", "type")

        self.quest_data = ()

        self.quest_tree.bind("<<TreeviewSelect>>", self.get_quest_data)
        self.quest_tree.bind('<Double-1>', self.edit_quest)

        self.refresh_table()

        self.add_quest_button = tk.Button(self, text="Add Quest", command=self.add_quest)
        self.add_quest_button.place(x=541, y=140, width=100)

        self.complete_quest_button = tk.Button(self, text="Complete Quest", command=self.complete_quest)
        self.complete_quest_button.place(x=541, y=166, width=100)

        # Notes

        self.notes = tk.Text(self, bg="#56626b", fg="white", wrap=tk.WORD)
        self.notes.insert(tk.INSERT, self.database.current_campaign.get('notes'))
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

    def get_quest_data(self, event):
        selected_entry = self.quest_tree.focus()
        if selected_entry:
            name, quest_type, notes = self.quest_tree.item(selected_entry)["values"]
            self.quest_data = (name, quest_type, notes)

    def add_quest(self):
        QuestManager(self, quest_data=())

    def edit_quest(self, event):
        QuestManager(self, self.quest_data)

    def complete_quest(self):
        name, quest_type, notes = self.quest_data
        completed_quest_index = self.database.get_quest_index(name, quest_type, notes)
        self.database.manage_quest_list(name, "Completed", notes, completed_quest_index)
        self.refresh_table()

    def refresh_table(self):
        self.quest_tree.delete(*self.quest_tree.get_children())
        for quest in self.database.current_campaign.get('quests'):
            self.quest_tree.insert("", index=tk.END, values=quest)

    def initiate_combat(self):
        pass

    def roll_d20(self):
        self.dice_roll.set(randint(1, 20))

    def on_close(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.database.current_campaign["notes"] = self.notes.get("1.0", tk.END)
            self.database.save_current_campaign()
            self.master.destroy()


class QuestManager(tk.Toplevel):
    def __init__(self, campaign, quest_data):
        super().__init__(campaign)
        self.campaign = campaign
        self.database = self.campaign.master.database

        self.geometry(f"320x196+{self.campaign.winfo_x()}+{self.campaign.winfo_y()}")
        self.title("Adventure Awaits!")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.quest_amendment_index = -1

        self.quest_title = tk.Label(self, text="Quest Title:")
        self.quest_title.grid(row=0, column=0)

        self.quest_title_entry = tk.Entry(self, width=40)
        self.quest_title_entry.grid(row=0, column=1)
        self.quest_title_entry.focus_set()

        self.quest_type_text = tk.StringVar()
        self.quest_type_text.set("Side")
        self.quest_type = tk.Checkbutton(self, text='Main Quest?', variable=self.quest_type_text,
                                         onvalue="Main", offvalue="Side")
        self.quest_type.grid(row=1, column=1)

        self.quest_notes_label = tk.Label(self, text="Description:")
        self.quest_notes_label.grid(row=2, column=0)

        self.quest_notes = tk.Text(self, width=30, height=7, wrap=tk.WORD)
        self.quest_notes.grid(row=2, column=1, columnspan=2)

        self.add_quest_button_text = "Add Quest"

        if quest_data:
            name, quest_type, notes = quest_data
            self.quest_amendment_index = self.database.get_quest_index(name, quest_type, notes)

            self.quest_title_entry.insert(0, name)
            self.quest_type_text.set(quest_type)
            self.quest_notes.insert(END, notes)
            self.add_quest_button_text = "Update"

        self.add_quest_button = tk.Button(self, text=self.add_quest_button_text, command=self.manage_quest)
        self.add_quest_button.grid(row=3, column=1, sticky="E")

    def manage_quest(self):
        name = self.quest_title_entry.get()
        quest_type = self.quest_type_text.get()
        notes = self.quest_notes.get("1.0", tk.END)
        self.database.manage_quest_list(name, quest_type, notes, self.quest_amendment_index)
        self.campaign.refresh_table()
        self.destroy()
