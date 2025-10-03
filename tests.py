from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui_tests import Ui_Tests

class Tests(QDialog, Ui_Tests):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Tests")