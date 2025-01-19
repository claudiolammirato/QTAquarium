from PySide6 import QtWidgets
from main_window import MainWindow
from database_class import DatabaseManager
from create_database import create_database
import sys

def main():
    #DATABASE Settings
    create_database("qtaquarium")

    #CREATE Tables
    database = DatabaseManager()
    table_string_DSB=(["id","SERIAL PRIMARY KEY"],["name", "TEXT NOT NULL"],["cognome", "TEXT"])
    DatabaseManager.table_creation(database,"DSB", table_string_DSB)




    #GUI Settings
    app =QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    app.exec()


if __name__ == "__main__":
    main()