# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dsb_aquarium.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QWidget)

class Ui_DsbAquarium(object):
    def setupUi(self, BerlAquarium):
        if not BerlAquarium.objectName():
            BerlAquarium.setObjectName(u"BerlAquarium")
        BerlAquarium.resize(640, 480)
        self.dsb_temperature = QLabel(BerlAquarium)
        self.dsb_temperature.setObjectName(u"dsb_temperature")
        self.dsb_temperature.setGeometry(QRect(40, 30, 260, 16))
        self.dsb_room_temperature = QLabel(BerlAquarium)
        self.dsb_room_temperature.setObjectName(u"dsb_room_temperature")
        self.dsb_room_temperature.setGeometry(QRect(40, 70, 260, 16))
        self.dsb_room_humidity = QLabel(BerlAquarium)
        self.dsb_room_humidity.setObjectName(u"dsb_room_humidity")
        self.dsb_room_humidity.setGeometry(QRect(40, 110, 260, 16))
        self.dsb_time = QLabel(BerlAquarium)
        self.dsb_time.setObjectName(u"dsb_time")
        self.dsb_time.setGeometry(QRect(40, 160, 260, 16))
        self.frame = QFrame(BerlAquarium)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 600, 200))
        palette = QPalette()
        brush = QBrush(QColor(54, 54, 54, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        self.frame.setPalette(palette)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.berl_graph = QWidget(BerlAquarium)
        self.berl_graph.setObjectName(u"berl_graph")
        self.berl_graph.setGeometry(QRect(20, 230, 591, 221))
        self.dsb_graph = QWebEngineView(self.berl_graph)
        self.dsb_graph.setObjectName(u"dsb_graph")
        self.dsb_graph.setGeometry(QRect(9, 9, 581, 211))
        self.frame.raise_()
        self.dsb_temperature.raise_()
        self.dsb_room_temperature.raise_()
        self.dsb_room_humidity.raise_()
        self.dsb_time.raise_()
        self.berl_graph.raise_()

        self.retranslateUi(BerlAquarium)

        QMetaObject.connectSlotsByName(BerlAquarium)
    # setupUi

    def retranslateUi(self, BerlAquarium):
        BerlAquarium.setWindowTitle(QCoreApplication.translate("BerlAquarium", u"Berlinese Aquarium", None))
        self.dsb_temperature.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
        self.dsb_room_temperature.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
        self.dsb_room_humidity.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
        self.dsb_time.setText(QCoreApplication.translate("BerlAquarium", u"TextLabel", None))
    # retranslateUi

