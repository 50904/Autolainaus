# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(315, 236)
        self.databaseLabel = QLabel(Dialog)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setGeometry(QRect(20, 70, 71, 16))
        font = QFont()
        font.setPointSize(9)
        self.databaseLabel.setFont(font)
        self.databaseLineEdit = QLineEdit(Dialog)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setGeometry(QRect(110, 70, 151, 20))
        self.serverLineEdit = QLineEdit(Dialog)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        self.serverLineEdit.setGeometry(QRect(110, 10, 151, 20))
        self.ServerLabel = QLabel(Dialog)
        self.ServerLabel.setObjectName(u"ServerLabel")
        self.ServerLabel.setGeometry(QRect(20, 10, 47, 13))
        self.ServerLabel.setFont(font)
        self.portLabel = QLabel(Dialog)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setGeometry(QRect(20, 40, 47, 13))
        self.portLabel.setFont(font)
        self.userLabel = QLabel(Dialog)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setGeometry(QRect(20, 100, 101, 16))
        self.userLabel.setFont(font)
        self.portLineEdit = QLineEdit(Dialog)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setGeometry(QRect(110, 40, 151, 20))
        self.userLineEdit = QLineEdit(Dialog)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setGeometry(QRect(110, 100, 151, 20))
        self.saveSettingspushButton = QPushButton(Dialog)
        self.saveSettingspushButton.setObjectName(u"saveSettingspushButton")
        self.saveSettingspushButton.setEnabled(True)
        self.saveSettingspushButton.setGeometry(QRect(190, 180, 71, 21))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.saveSettingspushButton.setFont(font1)
        self.saveSettingspushButton.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.passwordLabel = QLabel(Dialog)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(20, 130, 71, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.passwordLabel.setFont(font2)
        self.passwordLineEdit = QLineEdit(Dialog)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(110, 130, 151, 20))
        font3 = QFont()
        font3.setPointSize(8)
        self.passwordLineEdit.setFont(font3)
        self.passwordLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.closePushButton = QPushButton(Dialog)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setGeometry(QRect(110, 180, 75, 23))
        self.closePushButton.setFont(font)
        self.closePushButton.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.databaseLabel.setText(QCoreApplication.translate("Dialog", u"Tietokanta", None))
        self.ServerLabel.setText(QCoreApplication.translate("Dialog", u"Palvelin", None))
        self.portLabel.setText(QCoreApplication.translate("Dialog", u"Portti", None))
        self.userLabel.setText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.saveSettingspushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Salasana", None))
        self.closePushButton.setText(QCoreApplication.translate("Dialog", u"Sulje", None))
    # retranslateUi

