from PySide6 import QtWidgets
from main_window import MainWindow
import sys

app =QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()