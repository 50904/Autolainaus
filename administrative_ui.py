# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'administrative.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 866)
        self.actionMuokkaa = QAction(MainWindow)
        self.actionMuokkaa.setObjectName(u"actionMuokkaa")
        self.actionTietoja_ohjelmasta = QAction(MainWindow)
        self.actionTietoja_ohjelmasta.setObjectName(u"actionTietoja_ohjelmasta")
        self.actionvaihdaSalasana = QAction(MainWindow)
        self.actionvaihdaSalasana.setObjectName(u"actionvaihdaSalasana")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.valikko_2 = QTabWidget(self.centralwidget)
        self.valikko_2.setObjectName(u"valikko_2")
        self.valikko_2.setGeometry(QRect(-10, 0, 821, 881))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.valikko_2.setFont(font)
        self.studentTab_2 = QWidget()
        self.studentTab_2.setObjectName(u"studentTab_2")
        self.studentTab_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_2 = QLabel(self.studentTab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 101, 16))
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(self.studentTab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 20, 201, 20))
        self.label_3 = QLabel(self.studentTab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 91, 16))
        self.label_3.setFont(font)
        self.lineEdit_2 = QLineEdit(self.studentTab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 60, 201, 20))
        self.label_4 = QLabel(self.studentTab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 91, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.studentTab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 180, 101, 16))
        self.label_5.setFont(font)
        self.lineEdit_4 = QLineEdit(self.studentTab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(120, 180, 201, 21))
        self.comboBox = QComboBox(self.studentTab_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 140, 201, 22))
        self.tableWidget_2 = QTableWidget(self.studentTab_2)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        if (self.tableWidget_2.rowCount() < 10):
            self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 250, 771, 331))
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setColumnCount(3)
        self.pushButton_2 = QPushButton(self.studentTab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 180, 151, 23))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.studentTab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 220, 151, 16))
        self.label_10 = QLabel(self.studentTab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 140, 101, 16))
        self.label_10.setFont(font)
        self.lineEdit_6 = QLineEdit(self.studentTab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(120, 100, 201, 20))
        self.valikko_2.addTab(self.studentTab_2, "")
        self.vechileTab_2 = QWidget()
        self.vechileTab_2.setObjectName(u"vechileTab_2")
        self.vechileTab_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.registerNumberLabel = QLabel(self.vechileTab_2)
        self.registerNumberLabel.setObjectName(u"registerNumberLabel")
        self.registerNumberLabel.setGeometry(QRect(10, 30, 101, 16))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.registerNumberLabel.setFont(font1)
        self.markeLabel = QLabel(self.vechileTab_2)
        self.markeLabel.setObjectName(u"markeLabel")
        self.markeLabel.setGeometry(QRect(10, 60, 47, 13))
        self.markeLabel.setFont(font1)
        self.modelLabel = QLabel(self.vechileTab_2)
        self.modelLabel.setObjectName(u"modelLabel")
        self.modelLabel.setGeometry(QRect(10, 90, 47, 13))
        self.modelLabel.setFont(font1)
        self.yearModel = QLabel(self.vechileTab_2)
        self.yearModel.setObjectName(u"yearModel")
        self.yearModel.setGeometry(QRect(10, 120, 71, 16))
        self.yearModel.setFont(font1)
        self.registerNumberlineEdit = QLineEdit(self.vechileTab_2)
        self.registerNumberlineEdit.setObjectName(u"registerNumberlineEdit")
        self.registerNumberlineEdit.setGeometry(QRect(110, 30, 141, 20))
        self.markeLineEdit = QLineEdit(self.vechileTab_2)
        self.markeLineEdit.setObjectName(u"markeLineEdit")
        self.markeLineEdit.setGeometry(QRect(110, 60, 141, 20))
        self.modelLineEdit = QLineEdit(self.vechileTab_2)
        self.modelLineEdit.setObjectName(u"modelLineEdit")
        self.modelLineEdit.setGeometry(QRect(110, 90, 141, 20))
        self.yearModelLineEdit = QLineEdit(self.vechileTab_2)
        self.yearModelLineEdit.setObjectName(u"yearModelLineEdit")
        self.yearModelLineEdit.setGeometry(QRect(110, 120, 141, 20))
        self.personCountLabel = QLabel(self.vechileTab_2)
        self.personCountLabel.setObjectName(u"personCountLabel")
        self.personCountLabel.setGeometry(QRect(10, 150, 81, 16))
        self.personCountLabel.setFont(font1)
        self.personCountLineEdit = QLineEdit(self.vechileTab_2)
        self.personCountLineEdit.setObjectName(u"personCountLineEdit")
        self.personCountLineEdit.setGeometry(QRect(110, 150, 141, 20))
        self.printSaveButton = QPushButton(self.vechileTab_2)
        self.printSaveButton.setObjectName(u"printSaveButton")
        self.printSaveButton.setGeometry(QRect(260, 150, 81, 23))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.printSaveButton.setFont(font2)
        self.printSaveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.printSaveButton.setStyleSheet(u"background-color: rgb(94, 172, 255);\n"
"color: rgb(247, 247, 247);")
        self.printBarcodeButton = QPushButton(self.vechileTab_2)
        self.printBarcodeButton.setObjectName(u"printBarcodeButton")
        self.printBarcodeButton.setGeometry(QRect(260, 120, 81, 23))
        self.printBarcodeButton.setFont(font1)
        self.printBarcodeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.printBarcodeButton.setStyleSheet(u"background-color: rgb(255, 140, 46);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(self.vechileTab_2)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 220, 751, 331))
        self.tableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.label_31 = QLabel(self.vechileTab_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 200, 111, 16))
        self.valikko_2.addTab(self.vechileTab_2, "")
        self.groupTab = QWidget()
        self.groupTab.setObjectName(u"groupTab")
        self.label_6 = QLabel(self.groupTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 169, 16))
        self.label_6.setFont(font)
        self.resonsivleLabel = QLabel(self.groupTab)
        self.resonsivleLabel.setObjectName(u"resonsivleLabel")
        self.resonsivleLabel.setGeometry(QRect(20, 50, 169, 47))
        self.resonsivleLabel.setFont(font)
        self.groupNameLineEdit = QLineEdit(self.groupTab)
        self.groupNameLineEdit.setObjectName(u"groupNameLineEdit")
        self.groupNameLineEdit.setGeometry(QRect(120, 20, 167, 24))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.groupNameLineEdit.setFont(font3)
        self.responsibleDateEdit = QLineEdit(self.groupTab)
        self.responsibleDateEdit.setObjectName(u"responsibleDateEdit")
        self.responsibleDateEdit.setGeometry(QRect(120, 60, 167, 24))
        self.responsibleDateEdit.setFont(font3)
        self.savebutton = QPushButton(self.groupTab)
        self.savebutton.setObjectName(u"savebutton")
        self.savebutton.setGeometry(QRect(300, 61, 121, 21))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.savebutton.setFont(font4)
        self.savebutton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.groupTabelWidget = QTableWidget(self.groupTab)
        if (self.groupTabelWidget.columnCount() < 2):
            self.groupTabelWidget.setColumnCount(2)
        if (self.groupTabelWidget.rowCount() < 10):
            self.groupTabelWidget.setRowCount(10)
        self.groupTabelWidget.setObjectName(u"groupTabelWidget")
        self.groupTabelWidget.setGeometry(QRect(10, 170, 771, 391))
        self.groupTabelWidget.setRowCount(10)
        self.groupTabelWidget.setColumnCount(2)
        self.savedGroupLabel = QLabel(self.groupTab)
        self.savedGroupLabel.setObjectName(u"savedGroupLabel")
        self.savedGroupLabel.setGeometry(QRect(10, 150, 121, 20))
        self.savedGroupLabel.setFont(font)
        self.valikko_2.addTab(self.groupTab, "")
        self.reportsTab_2 = QWidget()
        self.reportsTab_2.setObjectName(u"reportsTab_2")
        self.label = QLabel(self.reportsTab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 16))
        self.label.setFont(font)
        self.startDateEdit = QDateEdit(self.reportsTab_2)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setGeometry(QRect(20, 100, 151, 31))
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDate(QDate(2025, 1, 1))
        self.reportTypecomboBox = QComboBox(self.reportsTab_2)
        self.reportTypecomboBox.setObjectName(u"reportTypecomboBox")
        self.reportTypecomboBox.setGeometry(QRect(20, 30, 151, 22))
        self.statDateLable = QLabel(self.reportsTab_2)
        self.statDateLable.setObjectName(u"statDateLable")
        self.statDateLable.setGeometry(QRect(20, 80, 71, 16))
        self.statDateLable.setFont(font)
        self.endDateEdit = QDateEdit(self.reportsTab_2)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setGeometry(QRect(220, 100, 151, 31))
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(QDate(2025, 1, 1))
        self.endDateLabel = QLabel(self.reportsTab_2)
        self.endDateLabel.setObjectName(u"endDateLabel")
        self.endDateLabel.setGeometry(QRect(220, 80, 71, 16))
        self.endDateLabel.setFont(font)
        self.printResultPushButton = QPushButton(self.reportsTab_2)
        self.printResultPushButton.setObjectName(u"printResultPushButton")
        self.printResultPushButton.setGeometry(QRect(390, 100, 81, 31))
        self.printResultPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.printResultPushButton.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"color: rgb(249, 249, 249);")
        self.tableWidget_3 = QTableWidget(self.reportsTab_2)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        if (self.tableWidget_3.rowCount() < 22):
            self.tableWidget_3.setRowCount(22)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(20, 170, 731, 331))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(False)
        self.tableWidget_3.setFont(font5)
        self.tableWidget_3.setRowCount(22)
        self.tableWidget_3.setColumnCount(6)
        self.firstLookLabel = QLabel(self.reportsTab_2)
        self.firstLookLabel.setObjectName(u"firstLookLabel")
        self.firstLookLabel.setGeometry(QRect(20, 140, 81, 16))
        self.valikko_2.addTab(self.reportsTab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionMuokkaa)
        self.menu.addAction(self.actionTietoja_ohjelmasta)
        self.menu.addAction(self.actionvaihdaSalasana)

        self.retranslateUi(MainWindow)

        self.valikko_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionMuokkaa.setText(QCoreApplication.translate("MainWindow", u"Muokkaa...", None))
        self.actionTietoja_ohjelmasta.setText(QCoreApplication.translate("MainWindow", u"Tietoja ohjelmasta...", None))
        self.actionvaihdaSalasana.setText(QCoreApplication.translate("MainWindow", u"Salasana...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ajoneuvoluokka", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Reksiter\u00f6idyt lainaajat", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4", None))
        self.valikko_2.setTabText(self.valikko_2.indexOf(self.studentTab_2), QCoreApplication.translate("MainWindow", u"Lainaajat", None))
        self.registerNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Rekisterinumero", None))
        self.markeLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"Malli", None))
        self.yearModel.setText(QCoreApplication.translate("MainWindow", u"Vuosimalli", None))
        self.personCountLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6m\u00e4\u00e4r\u00e4", None))
        self.printSaveButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.printBarcodeButton.setText(QCoreApplication.translate("MainWindow", u"Viivakoodi", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Autoluettelo", None))
        self.valikko_2.setTabText(self.valikko_2.indexOf(self.vechileTab_2), QCoreApplication.translate("MainWindow", u"Autot", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4n nimi", None))
        self.resonsivleLabel.setText(QCoreApplication.translate("MainWindow", u"Vastuuhenkil\u00f6", None))
        self.savebutton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.savedGroupLabel.setText(QCoreApplication.translate("MainWindow", u"Tallennetut ryhm\u00e4t", None))
        self.valikko_2.setTabText(self.valikko_2.indexOf(self.groupTab), QCoreApplication.translate("MainWindow", u"Ryhm\u00e4t", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Raportti", None))
        self.statDateLable.setText(QCoreApplication.translate("MainWindow", u"Alkaa", None))
        self.endDateLabel.setText(QCoreApplication.translate("MainWindow", u"P\u00e4\u00e4ttyy", None))
        self.printResultPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.firstLookLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.valikko_2.setTabText(self.valikko_2.indexOf(self.reportsTab_2), QCoreApplication.translate("MainWindow", u"Raportit", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Asetukset", None))
    # retranslateUi

