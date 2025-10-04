from PySide6.QtCore import Qt, QDateTime, QDate
from PySide6.QtWidgets import QDialog, QComboBox
from ui_tests import Ui_Tests
from database_class import DatabaseManager


class Tests(QDialog, Ui_Tests):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Tests")

        self.dateEdit.setDateTime(QDateTime.currentDateTime())

        self.comboBox_test_type.addItem('NO3')
        self.comboBox_test_type.addItem('NO2')
        self.comboBox_test_type.addItem('Ca')
        self.comboBox_test_type.addItem('Mg')
        self.comboBox_test_type.addItem('KH')
        self.comboBox_test_type.addItem('PH')
        self.comboBox_test_type.addItem('Si')
        self.comboBox_test_type.addItem('PO')
        self.comboBox_test_type.addItem('NH4/NH3')

        

        self.insertButton.clicked.connect(self.save_settings)
        

    def save_settings(self):
        
        date = self.dateEdit.dateTime().toPython()
        value = self.textEdit.toPlainText()
        save_values = [self.comboBox_test_type.currentText(), value, date.strftime("%Y-%m-%d %H:%M:%S")]
        print(value)
        print(date.strftime("%Y-%m-%d %H:%M:%S"))
        print(save_values)
        database = DatabaseManager()
        DatabaseManager.insert_value(database, "tests", save_values)