import AppGUI
import Database


try:
    current_campaign = Database.get_data("current_campaign")
except FileNotFoundError:
    current_campaign = False


if __name__ == "__main__":
    launcher = AppGUI.MainWindow(current_campaign)
    launcher.mainloop()
