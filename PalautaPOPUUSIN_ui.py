# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PalautaPOPUUSIN.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QTextBrowser, QWidget)
import testPictures_rc
import testPictures_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(581, 424)
        Form.setStyleSheet(u"background-color: rgb(255, 64, 150);")
        self.keyBarcodeLineEdit = QLineEdit(Form)
        self.keyBarcodeLineEdit.setObjectName(u"keyBarcodeLineEdit")
        self.keyBarcodeLineEdit.setGeometry(QRect(140, 130, 251, 41))
        font = QFont()
        font.setPointSize(12)
        self.keyBarcodeLineEdit.setFont(font)
        self.keyBarcodeLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.CarPictureLabel = QLabel(Form)
        self.CarPictureLabel.setObjectName(u"CarPictureLabel")
        self.CarPictureLabel.setGeometry(QRect(190, 70, 141, 41))
        self.CarPictureLabel.setPixmap(QPixmap(u":/png/autolainausauto.png"))
        self.CarPictureLabel.setScaledContents(True)
        self.rentFailedLabel = QTextBrowser(Form)
        self.rentFailedLabel.setObjectName(u"rentFailedLabel")
        self.rentFailedLabel.setGeometry(QRect(140, 220, 251, 31))
        self.rentFailedLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.rentsuccesfulLabel = QTextBrowser(Form)
        self.rentsuccesfulLabel.setObjectName(u"rentsuccesfulLabel")
        self.rentsuccesfulLabel.setGeometry(QRect(140, 180, 251, 31))
        self.rentsuccesfulLabel.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.keyBarcodeLineEdit.setText("")
        self.keyBarcodeLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Avain: Lue avaimen viivakoodi", None))
        self.CarPictureLabel.setText("")
        self.rentFailedLabel.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Palautus ep\u00e4onnistui</span></p></body></html>", None))
        self.rentsuccesfulLabel.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Palautus onnistui</span></p></body></html>", None))
    # retranslateUi

