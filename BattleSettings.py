import tkinter as tk
from tkinter import ttk, messagebox, END
from PIL import ImageTk, Image
from Characters import Enemy
from Battlefield import CombatScreen


class BattleConfiguration(tk.Toplevel):
    def __init__(self, campaign):
        super().__init__(campaign)
        self.master = campaign
        self.geometry(f"666x333+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.title("Battle Settings")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.encounter_image = ImageTk.PhotoImage(Image.open("Images/Combat.jpg"))
        self.encounter_label = tk.Label(self, image=self.encounter_image)
        self.encounter_label.place(relwidth=1, relheight=1)

        self.hero_list = self.master.master.database.current_campaign["heroes"]
        self.hero_widgets = []

        if self.hero_list:
            for hero in self.hero_list:
                hero_image = ImageTk.PhotoImage(Image.open(hero.image_location).resize((70, 70), Image.ANTIALIAS))
                hero_label = tk.Label(self, image=hero_image, borderwidth=0)

                hero_initiative = tk.Entry(self, font="BOLD", borderwidth=3, justify="center", width=2)

                self.hero_widgets.append((hero_image, hero_label, hero_initiative))

        hero_image_position = 20
        hero_entry_position = 40
        for widget_set in self.hero_widgets:
            widget_set[1].place(x=hero_image_position, y=50)
            widget_set[2].place(x=hero_entry_position, y=130)
            hero_image_position += 70
            hero_entry_position += 70

        self.enemy_list = []

        self.enemy_list_box = tk.Listbox(self, height=6, width=57)
        self.enemy_list_box.place(x=307, y=220)

        self.gray_wall = tk.Label(self, pady=40, padx=147)
        self.gray_wall.place(x=10, y=221)

        self.enemy_name_label = tk.Label(self, text="Name", pady=3)
        self.enemy_name_label.place(x=18, y=249)
        self.enemy_name_entry = tk.Entry(self, width=20)
        self.enemy_name_entry.place(x=58, y=250)
        self.enemy_name_entry.focus_set()

        self.enemy_initiative_label = tk.Label(self, text="Initiative", pady=3)
        self.enemy_initiative_label.place(x=208, y=249)
        self.enemy_initiative_entry = tk.Entry(self, width=4)
        self.enemy_initiative_entry.place(x=263, y=250)

        self.enemy_amount_label = tk.Label(self, text="Amount", pady=4)
        self.enemy_amount_label.place(x=208, y=278)
        self.enemy_amount_entry = tk.Entry(self, width=3)
        self.enemy_amount_entry.place(x=263, y=280)
        self.enemy_amount_entry.insert(END, "1")

        self.info_label = tk.Label(self, text="Double-click an entry to remove it*", pady=1, font=("Comic Sans", 8))
        self.info_label.place(x=10, y=299)

        self.add_entry_button = ttk.Button(self, text="Add Enemy", width=48, command=self.add_entry)
        self.add_entry_button.place(x=10, y=220)

        self.battle_button_image = ImageTk.PhotoImage(file="Images/Battle_button.png")
        self.battle_button = tk.Button(self, image=self.battle_button_image, command=self.to_battle, borderwidth=2)
        self.battle_button.place(x=464, y=35, width=75, height=84)

        self.bind("<Return>", self.add_entry_event)
        self.bind('<Double-1>', self.remove_enemy_event)
        self.protocol("WM_DELETE_WINDOW", self.close_bc_window)

    def add_entry_event(self, event):
        self.add_entry()

    def add_entry(self):
        name_token = 0
        try:
            initiative = int(self.enemy_initiative_entry.get())
            amount = int(self.enemy_amount_entry.get())
            name = str(self.enemy_name_entry.get())

            for entry in self.enemy_list:
                if type(entry) is list:
                    if f"{name.capitalize()}1" == entry[0].name.capitalize():
                        name_token += 1
                elif name.capitalize() == entry.name.capitalize():
                    name_token += 1

            if amount >= 10:
                self.focus_set()
                messagebox.showinfo("Too much to handle! :(",
                                    "Please make another group, if there are more than 9 enemies..",
                                    parent=self)
                self.focus_set()
            elif name_token == 0:
                if int(self.enemy_amount_entry.get()) <= 1:
                    self.enemy_list.append(Enemy(name.capitalize(), initiative, amount))
                    self.refresh()
                    self.clear_entries()
                else:
                    multi_enemy = []
                    enemy_id = 0
                    for x in range(int(self.enemy_amount_entry.get())):
                        enemy_id += 1
                        multi_enemy.append(Enemy(f"{name.capitalize()}{enemy_id}", initiative, amount))
                    self.enemy_list.append(multi_enemy)
                    self.refresh()
                    self.clear_entries()
            else:
                self.focus_set()
                messagebox.showinfo("Who are you calling fat?!",
                                    "This beautiful name is already taken. Sorry Bub.",
                                    parent=self)
                self.focus_set()
        except ValueError:
            self.focus_set()
            messagebox.showerror("Eghem", "Hp/Initiative/Amount must contain a number.",
                                 parent=self)
            self.focus_set()
        self.enemy_name_entry.focus_set()

    def remove_enemy_event(self, event):
        self.remove_enemy()

    def remove_enemy(self):
        if len(self.enemy_list) > 0:
            try:
                selection = self.enemy_list_box.curselection()
                element = int(str(selection)[1])
                del self.enemy_list[element]
                self.enemy_list_box.delete(selection)
            except ValueError:
                pass
        else:
            pass

    def clear_entries(self):
        self.enemy_name_entry.delete(0, 'end')
        self.enemy_initiative_entry.delete(0, 'end')
        self.enemy_amount_entry.delete(0, 'end')
        self.enemy_amount_entry.insert(END, "1")

    def refresh(self):
        self.enemy_list_box.delete(0, END)
        for enemy in self.enemy_list:
            if type(enemy) is list:
                self.enemy_list_box.insert(0, enemy[0])
            else:
                self.enemy_list_box.insert(0, enemy)

    def to_battle(self):
        hero_number = 0
        for hero in self.hero_list:
            try:
                int(self.hero_widgets[hero_number][2].get())
            except ValueError:
                tk.messagebox.showwarning("Oops", "Hero Initiative should be a Number", parent=self)
                break

            hero.initiative = int(self.hero_widgets[hero_number][2].get())
            self.enemy_list.append(hero)
            hero_number += 1
        else:
            self.destroy()
            CombatScreen(self.master, self.enemy_list)

    def close_bc_window(self):
        self.destroy()
        self.master.deiconify()
