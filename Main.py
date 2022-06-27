import AppGUI
import Database


active_campaign = Database.load_data()

if __name__ == "__main__":
    launcher = AppGUI.MainWindow(active_campaign)
    launcher.mainloop()
