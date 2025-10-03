from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui_settings import Ui_Settings

class Settings(QDialog, Ui_Settings):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Settings")
