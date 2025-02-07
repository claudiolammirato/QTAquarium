from PySide6 import QtWidgets
from main_window import MainWindow
from database_class import DatabaseManager
from create_database import create_database
import sys
import time
from threading import Thread
import select
import psycopg2
import psycopg2.extensions
import json
from setting_class import ConfigClass



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
    print("here")

    #GUI Settings
    app =QtWidgets.QApplication(sys.argv)
    window = MainWindow()


    t2 = Thread(target = database_check, args=[window])
    t2.setDaemon(True)
    t2.start()

    window.resize(800,600);
    window.show();

    #window.showMaximized()

    app.exec()

    

def database_check(window):
    settings = ConfigClass()
    settings_loaded = settings.load_item("settings")
    conn = psycopg2.connect(database=settings_loaded['database']['name'],
                            host=settings_loaded["database"]["url"],
                            user=settings_loaded["database"]["username"],
                            password=settings_loaded["database"]["password"],
                            port=settings_loaded["database"]["port"])
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    curs = conn.cursor()
    curs.execute("LISTEN users_notification;")

    print("Waiting for notifications on channel 'notification'")
    while True:
        if select.select([conn],[],[],5) == ([],[],[]):
            #print("Timeout")
            pass
        else:
            conn.poll()
            while conn.notifies:
                notify = conn.notifies.pop(0)
                print("Got NOTIFY:", notify.pid, notify.channel, notify.payload)
                y = json.loads(notify.payload)
                print(y)
                if y["aquarium_name"] == "Berlinese":
                    if y["sensor_type"] == "DHT":
                        window.update_ber_a_launch_dht(str(y["data_temp"]), str(y["data_hum"]), str(y["date"]))
                        print("dht update!!!)")
                if y["aquarium_name"] == "Berlinese":
                    if y["sensor_type"] == "DS18B20":
                        window.update_ber_a_launch_ds(str(y["data_temp"]))
                        print("ds update!!!")


if __name__ == "__main__":
    main()