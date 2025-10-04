from PySide6.QtCore import Qt, QDateTime, QDate
from PySide6.QtWidgets import QDialog, QComboBox, QTableWidgetItem, QAbstractScrollArea
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
        database = DatabaseManager()

        values = DatabaseManager.read_all_values(database,"tests")
        #print(values[0])
        

        self.tableNO2.setRowCount(len(values))
        self.tableNO2.setColumnCount(3)
        self.tableNO2.setHorizontalHeaderLabels(["Test", "Value", "Date"])  
        for i in range(len(values)):
            item_test = QTableWidgetItem(values[i][1])
            #item_value = QTableWidgetItem(values[i][2])
            #print(values[i][2])
            item_date = QTableWidgetItem(values[i][3])

            item_value = QTableWidgetItem()
            item_value.setData(Qt.DisplayRole, values[i][2])
            self.tableNO2.setItem(i, 0, item_test)
            self.tableNO2.setItem(i, 1, item_value)
            self.tableNO2.setItem(i, 2, item_date)

        self.tableNO2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableNO2.resizeColumnsToContents()
        self.insertButton.clicked.connect(self.save_settings)
        

    def save_settings(self):
        
        date_test = self.dateEdit.dateTime().toPython()
        value = self.textEdit.toPlainText()
        save_values=(["test_type",self.comboBox_test_type.currentText()],["test_value",value], ["date",date_test.strftime("%Y-%m-%d %H:%M:%S")])
        database = DatabaseManager()
        DatabaseManager.insert_value(database, "tests", save_values)
        #refresh table
        database = DatabaseManager()
        values = DatabaseManager.read_all_values(database,"tests")
        #print(values[0])
        self.tableNO2.setRowCount(len(values))
        self.tableNO2.setColumnCount(3)
        self.tableNO2.setHorizontalHeaderLabels(["Test", "Value", "Date"])  
        for i in range(len(values)):
            item_test = QTableWidgetItem(values[i][1])
            #item_value = QTableWidgetItem(values[i][2])
            #print(values[i][2])
            item_date = QTableWidgetItem(values[i][3])

            item_value = QTableWidgetItem()
            item_value.setData(Qt.DisplayRole, values[i][2])
            self.tableNO2.setItem(i, 0, item_test)
            self.tableNO2.setItem(i, 1, item_value)
            self.tableNO2.setItem(i, 2, item_date)
