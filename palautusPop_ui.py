# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'palautusPop.ui'
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
        Form.resize(706, 514)
        Form.setStyleSheet(u"background-color: rgb(255, 64, 150);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 81, 16))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 70, 113, 22))
        self.palaaPushButton = QPushButton(Form)
        self.palaaPushButton.setObjectName(u"palaaPushButton")
        self.palaaPushButton.setGeometry(QRect(380, 310, 75, 23))
        self.palaaPushButton.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.studentPictureLabel = QLabel(Form)
        self.studentPictureLabel.setObjectName(u"studentPictureLabel")
        self.studentPictureLabel.setGeometry(QRect(70, 310, 161, 161))
        self.studentPictureLabel.setPixmap(QPixmap(u":/png/student.png"))
        self.studentPictureLabel.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Palautus", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Avain", None))
        self.palaaPushButton.setText(QCoreApplication.translate("Form", u"Palaa", None))
        self.studentPictureLabel.setText("")
    # retranslateUi

