# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autolainausfirstPage.ui'
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
import testPictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 640)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 64, 150);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rentPushButton = QPushButton(self.centralwidget)
        self.rentPushButton.setObjectName(u"rentPushButton")
        self.rentPushButton.setGeometry(QRect(50, 90, 221, 161))
        font = QFont()
        font.setPointSize(24)
        self.rentPushButton.setFont(font)
        self.rentPushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.returnPushButton = QPushButton(self.centralwidget)
        self.returnPushButton.setObjectName(u"returnPushButton")
        self.returnPushButton.setGeometry(QRect(50, 290, 221, 151))
        self.returnPushButton.setFont(font)
        self.returnPushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.keyBarcodeReaderLinEdit = QLineEdit(self.centralwidget)
        self.keyBarcodeReaderLinEdit.setObjectName(u"keyBarcodeReaderLinEdit")
        self.keyBarcodeReaderLinEdit.setGeometry(QRect(410, 400, 251, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.keyBarcodeReaderLinEdit.setFont(font1)
        self.keyBarcodeReaderLinEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.keyPictureLabel = QLabel(self.centralwidget)
        self.keyPictureLabel.setObjectName(u"keyPictureLabel")
        self.keyPictureLabel.setGeometry(QRect(30, 480, 131, 91))
        self.keyPictureLabel.setPixmap(QPixmap(u":/png/Keys.png"))
        self.keyPictureLabel.setScaledContents(True)
        self.readLicenceBarcodelineEdit = QLineEdit(self.centralwidget)
        self.readLicenceBarcodelineEdit.setObjectName(u"readLicenceBarcodelineEdit")
        self.readLicenceBarcodelineEdit.setEnabled(True)
        self.readLicenceBarcodelineEdit.setGeometry(QRect(410, 140, 241, 41))
        font2 = QFont()
        font2.setPointSize(11)
        self.readLicenceBarcodelineEdit.setFont(font2)
        self.readLicenceBarcodelineEdit.setLayoutDirection(Qt.LeftToRight)
        self.readLicenceBarcodelineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.readLicenceBarcodelineEdit.setInputMethodHints(Qt.ImhNone)
        self.readLicenceBarcodelineEdit.setFrame(True)
        self.readLicenceBarcodelineEdit.setReadOnly(False)
        self.teacherPictureLabel = QLabel(self.centralwidget)
        self.teacherPictureLabel.setObjectName(u"teacherPictureLabel")
        self.teacherPictureLabel.setEnabled(True)
        self.teacherPictureLabel.setGeometry(QRect(410, 10, 241, 121))
        self.teacherPictureLabel.setInputMethodHints(Qt.ImhHiddenText)
        self.teacherPictureLabel.setPixmap(QPixmap(u":/png/Teacher.png"))
        self.teacherPictureLabel.setScaledContents(True)
        self.rentSuccedLabel = QLabel(self.centralwidget)
        self.rentSuccedLabel.setObjectName(u"rentSuccedLabel")
        self.rentSuccedLabel.setGeometry(QRect(610, 240, 161, 31))
        font3 = QFont()
        font3.setPointSize(15)
        self.rentSuccedLabel.setFont(font3)
        self.rentSuccedLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.renFailLabel = QLabel(self.centralwidget)
        self.renFailLabel.setObjectName(u"renFailLabel")
        self.renFailLabel.setGeometry(QRect(580, 290, 191, 31))
        self.renFailLabel.setFont(font3)
        self.renFailLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.keyBarcodeSucced = QLabel(self.centralwidget)
        self.keyBarcodeSucced.setObjectName(u"keyBarcodeSucced")
        self.keyBarcodeSucced.setGeometry(QRect(570, 520, 211, 41))
        font4 = QFont()
        font4.setPointSize(13)
        self.keyBarcodeSucced.setFont(font4)
        self.keyBarcodeSucced.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.keyBarcodefailLabel = QLabel(self.centralwidget)
        self.keyBarcodefailLabel.setObjectName(u"keyBarcodefailLabel")
        self.keyBarcodefailLabel.setGeometry(QRect(560, 470, 221, 41))
        self.keyBarcodefailLabel.setFont(font1)
        self.keyBarcodefailLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.carPictureLabel = QLabel(self.centralwidget)
        self.carPictureLabel.setObjectName(u"carPictureLabel")
        self.carPictureLabel.setGeometry(QRect(450, 340, 141, 41))
        self.carPictureLabel.setPixmap(QPixmap(u":/png/autolainausauto.png"))
        self.carPictureLabel.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.readLicenceBarcodelineEdit.raise_()
        self.teacherPictureLabel.raise_()
        self.rentPushButton.raise_()
        self.returnPushButton.raise_()
        self.keyBarcodeReaderLinEdit.raise_()
        self.keyPictureLabel.raise_()
        self.rentSuccedLabel.raise_()
        self.renFailLabel.raise_()
        self.keyBarcodeSucced.raise_()
        self.keyBarcodefailLabel.raise_()
        self.carPictureLabel.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rentPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaa", None))
        self.returnPushButton.setText(QCoreApplication.translate("MainWindow", u"Palauta", None))
        self.keyBarcodeReaderLinEdit.setText("")
        self.keyBarcodeReaderLinEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Avain: Lue avaimen viivakoodi", None))
        self.keyPictureLabel.setText("")
#if QT_CONFIG(tooltip)
        self.readLicenceBarcodelineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.readLicenceBarcodelineEdit.setText(QCoreApplication.translate("MainWindow", u"Ajokortti: Skannaa ajokortti!", None))
        self.readLicenceBarcodelineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Skanna ajokortti! ", None))
#if QT_CONFIG(tooltip)
        self.teacherPictureLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.teacherPictureLabel.setText("")
        self.rentSuccedLabel.setText(QCoreApplication.translate("MainWindow", u"Lainaus onnistui", None))
        self.renFailLabel.setText(QCoreApplication.translate("MainWindow", u"Lainaus ep\u00e4onnistui", None))
        self.keyBarcodeSucced.setText(QCoreApplication.translate("MainWindow", u"  Viivakoodin luku onnistui", None))
        self.keyBarcodefailLabel.setText(QCoreApplication.translate("MainWindow", u" Viivakoodin luku ep\u00e4onnistui", None))
        self.carPictureLabel.setText("")
    # retranslateUi

