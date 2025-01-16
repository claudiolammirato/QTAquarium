from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui_dsb_aquarium import Ui_DsbAquarium

class DsbAquarium(QDialog, Ui_DsbAquarium):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Aquarium DSB")

