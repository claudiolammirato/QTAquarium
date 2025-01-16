from PySide6 import QtWidgets
from main_window import MainWindow
from dsb_aquarium import DsbAquarium
import sys

app =QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec()