# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 19, 451, 41))
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(91, 86, 451, 211))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dsb_a = QPushButton(self.widget)
        self.dsb_a.setObjectName(u"dsb_a")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_a.sizePolicy().hasHeightForWidth())
        self.dsb_a.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.dsb_a)

        self.ber_a = QPushButton(self.widget)
        self.ber_a.setObjectName(u"ber_a")
        sizePolicy.setHeightForWidth(self.ber_a.sizePolicy().hasHeightForWidth())
        self.ber_a.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ber_a)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tests = QPushButton(self.widget)
        self.tests.setObjectName(u"tests")
        sizePolicy.setHeightForWidth(self.tests.sizePolicy().hasHeightForWidth())
        self.tests.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.tests)

        self.settings = QPushButton(self.widget)
        self.settings.setObjectName(u"settings")
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.settings)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Smart Aquarium", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Smart    Aquarium", None))
        self.dsb_a.setText(QCoreApplication.translate("MainWindow", u"DSB Aquarium", None))
        self.ber_a.setText(QCoreApplication.translate("MainWindow", u"Berlinese Aquarium", None))
        self.tests.setText(QCoreApplication.translate("MainWindow", u"Tests", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

