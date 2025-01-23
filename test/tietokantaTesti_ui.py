# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tietokantaTesti.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import testPictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 628)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        iconThemeName = u"emblem-shared"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(3000)
        MainWindow.setStyleSheet(u"background-color: rgb(223, 32, 122)")
        self.actionLopeta = QAction(MainWindow)
        self.actionLopeta.setObjectName(u"actionLopeta")
        icon1 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionLopeta.setIcon(icon1)
        self.actionKalle = QAction(MainWindow)
        self.actionKalle.setObjectName(u"actionKalle")
        self.actionVille = QAction(MainWindow)
        self.actionVille.setObjectName(u"actionVille")
        self.actionJaana = QAction(MainWindow)
        self.actionJaana.setObjectName(u"actionJaana")
        self.actionMikko = QAction(MainWindow)
        self.actionMikko.setObjectName(u"actionMikko")
        self.actionTallenna_nimell = QAction(MainWindow)
        self.actionTallenna_nimell.setObjectName(u"actionTallenna_nimell")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(30, 40, 113, 20))
        self.firstNameLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(23, 66, 70);")
        self.firstNameLabel = QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(30, 10, 111, 16))
        font = QFont()
        font.setPointSize(11)
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.firstNameLabel.setTextFormat(Qt.PlainText)
        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(170, 40, 113, 20))
        self.lastNameLabel = QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setGeometry(QRect(170, 10, 111, 16))
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lastNameLabel.setTextFormat(Qt.PlainText)
        self.savePushButton = QPushButton(self.centralwidget)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(210, 80, 75, 31))
        self.savePushButton.setFont(font)
        self.savePushButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.keyPictureLabel = QLabel(self.centralwidget)
        self.keyPictureLabel.setObjectName(u"keyPictureLabel")
        self.keyPictureLabel.setGeometry(QRect(380, 80, 241, 231))
        self.keyPictureLabel.setPixmap(QPixmap(u":/png/Keys.png"))
        self.teacherPictureLabel = QLabel(self.centralwidget)
        self.teacherPictureLabel.setObjectName(u"teacherPictureLabel")
        self.teacherPictureLabel.setGeometry(QRect(50, 150, 221, 231))
        self.teacherPictureLabel.setPixmap(QPixmap(u":/png/Teacher.png"))
        self.studentPictureLabel = QLabel(self.centralwidget)
        self.studentPictureLabel.setObjectName(u"studentPictureLabel")
        self.studentPictureLabel.setGeometry(QRect(260, 330, 221, 231))
        self.studentPictureLabel.setPixmap(QPixmap(u":/png/student.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        self.menuTiedosto = QMenu(self.menubar)
        self.menuTiedosto.setObjectName(u"menuTiedosto")
        self.menuEdelliset = QMenu(self.menuTiedosto)
        self.menuEdelliset.setObjectName(u"menuEdelliset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(255, 96, 165);")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTiedosto.menuAction())
        self.menuTiedosto.addAction(self.actionLopeta)
        self.menuTiedosto.addAction(self.menuEdelliset.menuAction())
        self.menuTiedosto.addAction(self.actionTallenna_nimell)
        self.menuEdelliset.addAction(self.actionKalle)
        self.menuEdelliset.addAction(self.actionVille)
        self.menuEdelliset.addAction(self.actionJaana)
        self.menuEdelliset.addAction(self.actionMikko)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tallentaa henkil\u00f6n tiedot tietokantaan</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionLopeta.setText(QCoreApplication.translate("MainWindow", u"Lopeta", None))
#if QT_CONFIG(shortcut)
        self.actionLopeta.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionKalle.setText(QCoreApplication.translate("MainWindow", u"Kalle", None))
        self.actionVille.setText(QCoreApplication.translate("MainWindow", u"Ville", None))
        self.actionJaana.setText(QCoreApplication.translate("MainWindow", u"Jaana", None))
        self.actionMikko.setText(QCoreApplication.translate("MainWindow", u"Mikko", None))
        self.actionTallenna_nimell.setText(QCoreApplication.translate("MainWindow", u"Tallenna nimell\u00e4...", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Puhuttelunimi", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.keyPictureLabel.setText("")
        self.teacherPictureLabel.setText("")
        self.studentPictureLabel.setText("")
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menuEdelliset.setTitle(QCoreApplication.translate("MainWindow", u"Edelliset", None))
    # retranslateUi

