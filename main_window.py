from PySide6.QtWidgets import QWidget, QPushButton
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle("Aquarium Smart")
        
        self.dsb_a.clicked.connect(self.dsb_a_launch)
        self.ber_a.clicked.connect(self.ber_a_launch)
        self.tests.clicked.connect(self.tests_launch)
        self.settings.clicked.connect(self.settings_launch)

    def dsb_a_launch(self):
        print("DSB!!!")
    
    def ber_a_launch(self):
        print("Berlinese!!!")
    
    def tests_launch(self):
        print("Tests!!!")
    
    def settings_launch(self):
        print("Settings!!!")
        
  

