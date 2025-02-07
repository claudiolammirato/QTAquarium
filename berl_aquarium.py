from PySide6.QtCore import Qt, QUrl, QFile
from PySide6.QtWidgets import QDialog
from ui_berl_aquarium import Ui_BerlAquarium
from database_class import DatabaseManager
from PySide6.QtWebEngineWidgets import QWebEngineView

import plotly.express as px 
import os
 
 


class BerlAquarium(QDialog, Ui_BerlAquarium):
    def __init__(self):
        super().__init__()
        database = DatabaseManager()

        data_ds18 = DatabaseManager.read_all_values(database,"ds18")
        data_dht = DatabaseManager.read_all_values(database,"dht")

        self.setupUi(self)
        self.setWindowTitle("Aquarium DSB")
        self.berl_temperature.setText("Aquarium Temperature: "+str(data_ds18[-1][3])+"°C")
        self.berl_room_temperature.setText("Room Temperature: "+str(data_dht[-1][3])+"°C")
        self.berl_room_humidity.setText("Room Humidity: "+str(data_dht[-1][4])+"%")
        self.berl_time.setText("reading time: "+str(data_dht[-1][5]))

        # Creating the Figure instance
        fig = px.line(x=[1, 2, 3], y=[1, 2, 3]) 
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "saved_graph","berl_graph.html"))
        print(file_path)
        fig.write_html(file_path)

        
        # showing the plot
        #fig.show()


        self.berl_graph_2.load(QUrl.fromLocalFile(file_path))
        self.berl_graph_2.show()

