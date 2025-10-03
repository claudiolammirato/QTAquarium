from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox
from ui_settings import Ui_Settings
from setting_class import ConfigClass


class Settings(QDialog, Ui_Settings):
    def __init__(self):
        super().__init__()

        settings = ConfigClass()
        settings_loaded = settings.load_item("settings")

        self.setupUi(self)
        self.setWindowTitle("Settings")
        self.ip_database.setText(settings_loaded["database"]["url"])
        self.ip_dsb.setText(settings_loaded["dsb"]["url"])
        self.ip_berlinese.setText(settings_loaded["berlinese"]["url"])
        self.saveButton.clicked.connect(self.save_settings)

    def save_settings(self):
        settings = ConfigClass()
        settings.save_item("settings","dsb", "url", self.ip_dsb.toPlainText())
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Settings")
        dlg.setText("Settings Saved")
        dlg.exec()

