# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'berl_aquarium.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_BerlAquarium(object):
    def setupUi(self, BerlAquarium):
        if not BerlAquarium.objectName():
            BerlAquarium.setObjectName(u"BerlAquarium")
        BerlAquarium.resize(640, 480)
        self.berl_temperature = QLabel(BerlAquarium)
        self.berl_temperature.setObjectName(u"berl_temperature")
        self.berl_temperature.setGeometry(QRect(40, 30, 260, 16))
        self.berl_room_temperature = QLabel(BerlAquarium)
        self.berl_room_temperature.setObjectName(u"berl_room_temperature")
        self.berl_room_temperature.setGeometry(QRect(40, 70, 260, 16))
        self.berl_room_humidity = QLabel(BerlAquarium)
        self.berl_room_humidity.setObjectName(u"berl_room_humidity")
        self.berl_room_humidity.setGeometry(QRect(40, 110, 260, 16))
        self.berl_time = QLabel(BerlAquarium)
        self.berl_time.setObjectName(u"berl_time")
        self.berl_time.setGeometry(QRect(40, 160, 260, 16))

        self.retranslateUi(BerlAquarium)

        QMetaObject.connectSlotsByName(BerlAquarium)
    # setupUi

    def retranslateUi(self, BerlAquarium):
        BerlAquarium.setWindowTitle(QCoreApplication.translate("BerlAquarium", u"Berlinese Aquarium", None))
        self.berl_temperature.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
        self.berl_room_temperature.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
        self.berl_room_humidity.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
        self.berl_time.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
    # retranslateUi

