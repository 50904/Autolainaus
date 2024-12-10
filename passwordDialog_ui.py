# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordDialog.ui'
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
        Dialog.setEnabled(False)
        Dialog.resize(400, 300)
        self.oldPasswordLabel = QLabel(Dialog)
        self.oldPasswordLabel.setObjectName(u"oldPasswordLabel")
        self.oldPasswordLabel.setGeometry(QRect(20, 30, 131, 16))
        font = QFont()
        font.setPointSize(10)
        self.oldPasswordLabel.setFont(font)
        self.newPasswordLabel = QLabel(Dialog)
        self.newPasswordLabel.setObjectName(u"newPasswordLabel")
        self.newPasswordLabel.setGeometry(QRect(20, 70, 91, 16))
        self.newPasswordLabel.setFont(font)
        self.newPasswordlineEdit = QLineEdit(Dialog)
        self.newPasswordlineEdit.setObjectName(u"newPasswordlineEdit")
        self.newPasswordlineEdit.setGeometry(QRect(140, 30, 201, 20))
        self.oldPasswordLineEdit = QLineEdit(Dialog)
        self.oldPasswordLineEdit.setObjectName(u"oldPasswordLineEdit")
        self.oldPasswordLineEdit.setEnabled(False)
        self.oldPasswordLineEdit.setGeometry(QRect(140, 70, 201, 20))
        self.savePasswordPushbutton = QPushButton(Dialog)
        self.savePasswordPushbutton.setObjectName(u"savePasswordPushbutton")
        self.savePasswordPushbutton.setEnabled(False)
        self.savePasswordPushbutton.setGeometry(QRect(210, 110, 121, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.savePasswordPushbutton.setFont(font1)
        self.savePasswordPushbutton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.oldPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Vanha salasana", None))
        self.newPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Uusi salasana", None))
        self.savePasswordPushbutton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
    # retranslateUi

