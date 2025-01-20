# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lainausPOP.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import testPictures_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(759, 580)
        Form.setStyleSheet(u"background-color: rgb(255, 64, 150);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(340, 210, 261, 41))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(350, 400, 271, 41))
        self.studentPictureLabel = QLabel(Form)
        self.studentPictureLabel.setObjectName(u"studentPictureLabel")
        self.studentPictureLabel.setGeometry(QRect(380, 40, 161, 161))
        self.studentPictureLabel.setPixmap(QPixmap(u":/png/student.png"))
        self.studentPictureLabel.setScaledContents(True)
        self.keyPictureLabel = QLabel(Form)
        self.keyPictureLabel.setObjectName(u"keyPictureLabel")
        self.keyPictureLabel.setGeometry(QRect(410, 280, 131, 111))
        self.keyPictureLabel.setPixmap(QPixmap(u":/png/Keys.png"))
        self.keyPictureLabel.setScaledContents(True)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 70, 221, 131))
        font = QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 320, 221, 131))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Henkil\u00f6", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"Avain", None))
        self.studentPictureLabel.setText("")
        self.keyPictureLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Lainaa", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Palauta", None))
    # retranslateUi

