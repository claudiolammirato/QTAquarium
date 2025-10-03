from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui_dsb_aquarium import Ui_DsbAquarium
from database_class import DatabaseManager
from PySide6.QtCore import Qt, QUrl, QFile

import os
from graph_funct import plot_graph

class DsbAquarium(QDialog, Ui_DsbAquarium):
    def __init__(self):
        super().__init__()
        database = DatabaseManager()

        data_ds18 = DatabaseManager.read_all_values(database,"ds18")
        data_dht = DatabaseManager.read_all_values(database,"dht")

        self.setupUi(self)
        self.setWindowTitle("Aquarium DSB")
        self.dsb_temperature.setText("Aquarium Temperature: "+str(data_ds18[-1][3])+"°C")
        self.dsb_room_temperature.setText("Room Temperature: "+str(data_dht[-1][3])+"°C")
        self.dsb_room_humidity.setText("Room Humidity: "+str(data_dht[-1][4])+"%")
        self.dsb_time.setText("reading time: "+str(data_dht[-1][5]))

        # Graph creation
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "saved_graph","berl_graph.html"))
        fig = plot_graph()
        fig.write_html(file_path)
        self.dsb_graph.load(QUrl.fromLocalFile(file_path))
        self.dsb_graph.show()
        

