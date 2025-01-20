# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LainaaPOPUUSIN.ui'
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
        Form.resize(611, 519)
        Form.setStyleSheet(u"background-color: rgb(255, 64, 150);")
        self.teacherPictureLabel = QLabel(Form)
        self.teacherPictureLabel.setObjectName(u"teacherPictureLabel")
        self.teacherPictureLabel.setEnabled(True)
        self.teacherPictureLabel.setGeometry(QRect(190, 20, 241, 121))
        self.teacherPictureLabel.setInputMethodHints(Qt.ImhHiddenText)
        self.teacherPictureLabel.setPixmap(QPixmap(u":/png/Teacher.png"))
        self.teacherPictureLabel.setScaledContents(True)
        self.licesensCardlineEdit = QLineEdit(Form)
        self.licesensCardlineEdit.setObjectName(u"licesensCardlineEdit")
        self.licesensCardlineEdit.setEnabled(True)
        self.licesensCardlineEdit.setGeometry(QRect(190, 150, 241, 41))
        font = QFont()
        font.setPointSize(11)
        self.licesensCardlineEdit.setFont(font)
        self.licesensCardlineEdit.setLayoutDirection(Qt.LeftToRight)
        self.licesensCardlineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.licesensCardlineEdit.setInputMethodHints(Qt.ImhNone)
        self.licesensCardlineEdit.setFrame(True)
        self.licesensCardlineEdit.setReadOnly(False)
        self.keyBarcodeLineEdit = QLineEdit(Form)
        self.keyBarcodeLineEdit.setObjectName(u"keyBarcodeLineEdit")
        self.keyBarcodeLineEdit.setGeometry(QRect(190, 300, 251, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.keyBarcodeLineEdit.setFont(font1)
        self.keyBarcodeLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.carPictureLabel = QLabel(Form)
        self.carPictureLabel.setObjectName(u"carPictureLabel")
        self.carPictureLabel.setGeometry(QRect(240, 240, 141, 41))
        self.carPictureLabel.setPixmap(QPixmap(u":/png/autolainausauto.png"))
        self.carPictureLabel.setScaledContents(True)
        self.rentfailedLabel = QTextBrowser(Form)
        self.rentfailedLabel.setObjectName(u"rentfailedLabel")
        self.rentfailedLabel.setGeometry(QRect(190, 390, 251, 31))
        self.rentfailedLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.rentsuccesLabel = QTextBrowser(Form)
        self.rentsuccesLabel.setObjectName(u"rentsuccesLabel")
        self.rentsuccesLabel.setGeometry(QRect(190, 350, 251, 31))
        self.rentsuccesLabel.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.teacherPictureLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.teacherPictureLabel.setText("")
#if QT_CONFIG(tooltip)
        self.licesensCardlineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.licesensCardlineEdit.setText(QCoreApplication.translate("Form", u"Ajokortti: Skannaa ajokortti!", None))
        self.licesensCardlineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Skanna ajokortti! ", None))
        self.keyBarcodeLineEdit.setText("")
        self.keyBarcodeLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Avain: Lue avaimen viivakoodi", None))
        self.carPictureLabel.setText("")
        self.rentfailedLabel.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Lainaus ep\u00e4onnistui</span></p></body></html>", None))
        self.rentsuccesLabel.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Lainaus onnistui</span></p></body></html>", None))
    # retranslateUi

