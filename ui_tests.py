# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tests.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Tests(object):
    def setupUi(self, Tests):
        if not Tests.objectName():
            Tests.setObjectName(u"Tests")
        Tests.resize(640, 480)
        self.insertButton = QPushButton(Tests)
        self.insertButton.setObjectName(u"insertButton")
        self.insertButton.setGeometry(QRect(20, 90, 75, 24))
        self.dateEdit = QDateEdit(Tests)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 30, 113, 24))
        self.comboBox_test_type = QComboBox(Tests)
        self.comboBox_test_type.setObjectName(u"comboBox_test_type")
        self.comboBox_test_type.setGeometry(QRect(170, 30, 73, 24))
        self.textEdit = QTextEdit(Tests)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(277, 33, 104, 21))

        self.retranslateUi(Tests)

        QMetaObject.connectSlotsByName(Tests)
    # setupUi

    def retranslateUi(self, Tests):
        Tests.setWindowTitle(QCoreApplication.translate("Tests", u"Form", None))
        self.insertButton.setText(QCoreApplication.translate("Tests", u"Insert", None))
    # retranslateUi

