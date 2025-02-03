from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui_dsb_aquarium import Ui_DsbAquarium
from database_class import DatabaseManager

class DsbAquarium(QDialog, Ui_DsbAquarium):
    def __init__(self):
        super().__init__()
        database = DatabaseManager()

        data = DatabaseManager.read_all_values(database,"ds18")


        self.setupUi(self)
        self.setWindowTitle("Aquarium DSB")
        self.text_temperature.setText("DSAB Temperature: "+str(data[-1][3]))

        

