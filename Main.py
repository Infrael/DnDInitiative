import AppGUI
import Database


if __name__ == "__main__":
    active_database = Database.Storage()
    launcher = AppGUI.MainWindow(active_database)
    launcher.mainloop()
