# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ServerLabel = QLabel(self.centralwidget)
        self.ServerLabel.setObjectName(u"ServerLabel")
        self.ServerLabel.setGeometry(QRect(20, 10, 47, 13))
        font = QFont()
        font.setPointSize(9)
        self.ServerLabel.setFont(font)
        self.portLabel = QLabel(self.centralwidget)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setGeometry(QRect(20, 40, 47, 13))
        self.portLabel.setFont(font)
        self.databaseLabel = QLabel(self.centralwidget)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setGeometry(QRect(20, 70, 71, 16))
        self.databaseLabel.setFont(font)
        self.userLabel = QLabel(self.centralwidget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setGeometry(QRect(20, 100, 101, 16))
        self.userLabel.setFont(font)
        self.passwordLabel = QLabel(self.centralwidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(20, 130, 71, 16))
        self.passwordLabel.setFont(font)
        self.serverLineEdit = QLineEdit(self.centralwidget)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        self.serverLineEdit.setGeometry(QRect(110, 10, 151, 20))
        self.portLineEdit = QLineEdit(self.centralwidget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setGeometry(QRect(110, 40, 151, 20))
        self.databaseLineEdit = QLineEdit(self.centralwidget)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setGeometry(QRect(110, 70, 151, 20))
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(110, 130, 151, 20))
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.userLineEdit = QLineEdit(self.centralwidget)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setGeometry(QRect(110, 100, 151, 20))
        self.saveSettingspushButton = QPushButton(self.centralwidget)
        self.saveSettingspushButton.setObjectName(u"saveSettingspushButton")
        self.saveSettingspushButton.setGeometry(QRect(110, 160, 111, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.saveSettingspushButton.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.passwordLineEdit, self.serverLineEdit)
        QWidget.setTabOrder(self.serverLineEdit, self.userLineEdit)
        QWidget.setTabOrder(self.userLineEdit, self.portLineEdit)
        QWidget.setTabOrder(self.portLineEdit, self.databaseLineEdit)
        QWidget.setTabOrder(self.databaseLineEdit, self.saveSettingspushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ServerLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
        self.saveSettingspushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
    # retranslateUi

