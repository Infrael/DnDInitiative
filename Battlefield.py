import tkinter as tk
from tkinter import ttk, END
from PIL import ImageTk, Image
import operator


class CombatScreen(tk.Toplevel):
    def __init__(self, campaign, enemy_list):
        super().__init__()
        self.master = campaign

        self.geometry(f"790x560+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.title("Combat Screen")
        self.iconbitmap('Images/Icon.ico')
        self.resizable(False, False)

        self.combat_image = ImageTk.PhotoImage(Image.open("Images/Encounter.jpg"))
        self.combat_label = tk.Label(self, image=self.combat_image)
        self.combat_label.place(relwidth=1, relheight=1)

        self.final_list = enemy_list
        self.round_number = 1
        self.round_counter = 1
        self.round_total = 1
        self.initiation_token = 0

        self.simple_list = []

        self.turn_time_entry = tk.Entry(self, width=5, justify="center", font="BOLD 24")
        self.turn_time_entry.place(x=0, y=0)
        self.total_time_entry = tk.Entry(self, width=5, justify="center", font="12")
        self.total_time_entry.place(x=0, y=40)
        self.total_time_entry.config(foreground="gray")

        self.combatants_tree = ttk.Treeview(self, columns=("A", "B"), selectmode="browse")

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(None, 14))

        self.combatants_tree.heading("A", text="State", anchor=tk.CENTER)
        self.combatants_tree.column("A", minwidth=0, width=60, stretch=tk.NO)
        self.combatants_tree.heading("B", text=f"Round: {self.round_number}", anchor=tk.W)
        self.combatants_tree.column("B", minwidth=0, width=100, stretch=tk.NO)
        self.combatants_tree.place(x=25, y=318, width=582)

        self.last_name = ""

        self.minutes = 0
        self.seconds = 0
        self.total_minutes = 0
        self.total_seconds = 0
        self.total_hours = 0

        self.next_button = ttk.Button(self, text="Next", command=self.button_next)
        self.next_button.place(x=670, y=510, width=100, height=33)

        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.free_text_box = tk.Text(self, width=37, height=4)
        self.free_text_box.place(x=477, y=0)
        self.free_text_box.insert(END, " Notes")

        self.update_the_tree()
        self.order_list = self.simple_list.copy()

        self.combatants_tree.bind('<Double-1>', self.double_click)

        self.combatants_tree.selection_set(self.last_name)
        self.start_timer()
        self.focus_set()

    def double_click(self, event):
        if self.combatants_tree.item(self.combatants_tree.focus()).get("values") == ["-DEAD-", '']:
            self.combatants_tree.set(self.combatants_tree.selection()[0], "A", "-          -")
        elif self.combatants_tree.item(self.combatants_tree.focus()).get("values") == ["-          -", '']:
            self.combatants_tree.set(self.combatants_tree.selection()[0], "A", "-DEAD-")
        else:
            self.combatants_tree.set(self.combatants_tree.selection()[0], "A", "-DEAD-")

    def clear_the_tree(self):
        self.combatants_tree.delete(*self.combatants_tree.get_children())

    def update_the_tree(self):
        self.clear_the_tree()

        self.round_total = len(self.final_list)

        for enemy in self.final_list:
            if type(enemy) is list:
                self.simple_list.append(enemy[0])
            else:
                self.simple_list.append(enemy)
        self.simple_list.sort(key=operator.attrgetter('initiative'))

        for combatant in self.simple_list:
            if combatant.amount > 1:
                self.combatants_tree.insert('', 0, f'{combatant.name[:-1]}',
                                            text=f"{combatant.name[:-1]} (Total: {combatant.amount})")
                numeric_value = 1
                for x in range(combatant.amount):
                    self.combatants_tree.insert(f'{combatant.name[:-1]}', 'end',
                                                f'{combatant.name[:-1]}{numeric_value}',
                                                text=f'{combatant.name[:-1]} .{numeric_value}. ')
                    numeric_value += 1
            else:
                try:
                    self.combatants_tree.insert('', 0, f'{combatant.name}', text=combatant)
                except tk.TclError:
                    pass

            if combatant.amount > 1:
                self.last_name = f"{combatant.name[:-1]}"
            else:
                self.last_name = combatant.name

    def button_next(self):
        self.turn_time_entry.delete(0, END)
        self.turn_time_entry.insert(0, "00:00")
        self.minutes = 0
        self.seconds = 0

        if self.round_counter == self.round_total:
            self.round_counter = 1
            self.round_number += 1
        else:
            self.round_counter += 1

        self.combatants_tree.heading("B", text=f"Round: {self.round_number}")

        if self.initiation_token == 0:
            self.initiation_token += 1
            self.order_list.reverse()

        for every in self.order_list:
            if every.amount > 1:
                self.combatants_tree.item(f"{every.name[:-1]}", open=False)

        if self.order_list[self.round_counter - 1].amount > 1:
            self.combatants_tree.selection_set(self.order_list[self.round_counter - 1].name[:-1])
        else:
            self.combatants_tree.selection_set(self.order_list[self.round_counter - 1].name)

    def start_timer(self):
        if self.seconds == 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1

        if self.minutes >= 1:
            self.turn_time_entry.config(foreground="dark red")
        elif self.seconds >= 20:
            self.turn_time_entry.config(foreground="dark orange")
        else:
            self.turn_time_entry.config(foreground="dark green")

        f_seconds = "{:02d}".format(self.seconds)
        f_minutes = "{:02d}".format(self.minutes)
        round_time_lapsed = f"{f_minutes}:{f_seconds}"

        if self.total_minutes == 59 and self.total_seconds == 59:
            self.total_hours += 1
            self.total_minutes = 0
            self.total_seconds = 0
        elif self.total_seconds == 59:
            self.total_minutes += 1
            self.total_seconds = 0

        else:
            self.total_seconds += 1

        f_total_seconds = "{:02d}".format(self.total_seconds)
        f_total_minutes = "{:02d}".format(self.total_minutes)

        if self.total_hours > 0:
            total_time_lapsed = f"{self.total_hours}H:{f_total_minutes}"
        else:
            total_time_lapsed = f"{f_total_minutes}:{f_total_seconds}"

        self.turn_time_entry.delete(0, END)
        self.turn_time_entry.insert(0, round_time_lapsed)
        self.total_time_entry.delete(0, END)
        self.total_time_entry.insert(0, total_time_lapsed)
        self.after(1000, self.start_timer)

    def close_window(self):
        self.destroy()
        self.master.deiconify()
