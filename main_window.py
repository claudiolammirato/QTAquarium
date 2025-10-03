from PySide6.QtWidgets import QWidget, QPushButton
from ui_mainwindow import Ui_MainWindow
from dsb_aquarium import DsbAquarium
from berl_aquarium import BerlAquarium
from settings import Settings


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle("Smart Aquarium")

        #self.dsbaquarium = DsbAquarium()
        self.berlaquarium = BerlAquarium()
      
        self.dsb_a.clicked.connect(self.dsb_a_launch)
        self.ber_a.clicked.connect(self.ber_a_launch)
        self.tests.clicked.connect(self.tests_launch)
        self.settings.clicked.connect(self.settings_launch)

    def dsb_a_launch(self):
        self.dsbaquarium = DsbAquarium()
        self.dsbaquarium.resize(800,600);
        self.dsbaquarium.show();
        #self.dsbaquarium.showMaximized()
        print("DSB!!!")
    
    def ber_a_launch(self):
        self.berlaquarium = BerlAquarium()
        self.berlaquarium.resize(800,600);
        self.berlaquarium.show();
        #self.berlaquarium.showMaximized()
        print("Berlinese!!!")
    
    def update_ber_a_launch_dht(self, temp, hum, t):
        self.berlaquarium.berl_room_temperature.setText("Room Temperature: "+temp+"°C")
        self.berlaquarium.berl_room_humidity.setText("Room Humidity: "+hum+"%")
        self.berlaquarium.berl_time.setText("reading time: "+ t)
        print("Berlinese!!!")

    def update_ber_a_launch_ds(self, temp):
        self.berlaquarium.berl_temperature.setText("Aquarium Temperature: "+temp+"°C")
        print("Berlinese!!!")
    
    def tests_launch(self):
        
        print("Tests!!!")
    
    def settings_launch(self):
        self.berlaquarium = Settings()
        self.berlaquarium.resize(800,600);
        self.berlaquarium.show();
        print("Settings!!!")
        
  

