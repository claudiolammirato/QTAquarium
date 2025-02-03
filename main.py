from PySide6 import QtWidgets
from main_window import MainWindow
from database_class import DatabaseManager
from create_database import create_database
import sys
import time

def main():
    #DATABASE Settings
    create_database("qtaquarium")

    #CREATE Tables
    database = DatabaseManager()
    #CREATE TABLE IF NOT EXISTS
    table_string_DS18=(["id","SERIAL PRIMARY KEY"],["aquarium_name", "TEXT"],["sensor_type", "TEXT"], ["data_temp", "REAL"],["date", "TEXT"])
    DatabaseManager.table_creation(database, "ds18", table_string_DS18)
    time.sleep(5)
    table_string_DHT=(["id","SERIAL PRIMARY KEY"],["aquarium_name", "TEXT"],["sensor_type", "TEXT"], ["data_temp", "REAL"],["data_hum", "REAL"],["date", "TEXT"])
    DatabaseManager.table_creation(database, "dht", table_string_DHT)
    time.sleep(5)




    #GUI Settings
    app =QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    app.exec()


if __name__ == "__main__":
    main()