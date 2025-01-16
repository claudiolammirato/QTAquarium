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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QSizePolicy,
    QTextEdit, QWidget)

class Ui_DsbAquarium(object):
    def setupUi(self, DsbAquarium):
        if not DsbAquarium.objectName():
            DsbAquarium.setObjectName(u"DsbAquarium")
        DsbAquarium.resize(640, 480)
        self.frame = QFrame(DsbAquarium)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 30, 611, 111))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.text_temperature = QTextEdit(self.frame)
        self.text_temperature.setObjectName(u"text_temperature")
        self.text_temperature.setGeometry(QRect(40, 20, 511, 64))

        self.retranslateUi(DsbAquarium)

        QMetaObject.connectSlotsByName(DsbAquarium)
    # setupUi

    def retranslateUi(self, DsbAquarium):
        DsbAquarium.setWindowTitle(QCoreApplication.translate("DsbAquarium", u"DSB Aquarium", None))
    # retranslateUi

