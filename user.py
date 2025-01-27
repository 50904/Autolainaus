# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet

# Tuodaan käyttöliittymään Pythoniksi käännetty tiedosto 
# Korvaa mainwindow_ui todellisella tiedoston nimellä
from user_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka joka perii QMainWindow- ja Ui_
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""

    # Määritellään oliomuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()


        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindown:n ui-ominaisuudeksi.
        # Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        self.ui.calendarPictureLabel.hide()
        self.ui.clockTimeLabel.hide()
        self.ui.dateTimeLabel.hide()
        self.ui.goBackPictureLabel.hide()
        self.ui.readyKeyLineEdit.hide()
        self.ui.keyPicturesLabel.hide()
        self.ui.readLicenceLineEdit.hide()
        self.ui.soundOnPictureLabel.hide()
        self.ui.ssnLineEdit.hide()
        self.ui.keyBarcodeLineEdit.hide()
        self.ui.statusLabel.hide()
        self.ui.dateTimeLabel.hude()

        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kun tallennuspainiketta on klikattu, kutsutaan metodia 
        self.ui.takeCarPushButton.clicked.connect(self.activateLender)



        
    # OHJELMOIDUT SLOTIT
    # ------------------
    def activateLender(self):
        self.ui.statusLabel.setText('Auton lainaus')
        self.ui.lenderPictureLabel.show()
        self.ui.ssnLineEdit.show()
        self.ui.goBackPictureLabel.show()
        self.ui.ssnLineEdit.setFocus()
        self.ui.returnCarPushButton.hide()
        self.ui.takeCarPushButton.hide()
        self.ui.statusLabel.show()
        self.ui.statusbar.showMessage('Syötä ajokortti koneeseen')


    # Tallennetaan syötetyt tiedot tietokantaan
    def saveData(self):
        pass 
    # Muutetaan tulostettuLabel:n sisältö: teksti ja väri
    def updatePrintedLabel(self):
        self.ui.tulostettuLabel.setText('Tulostettu')
        self.ui.tulostettuLabel.setStyleSheet(u"color: rgb(0, 255, 0)")

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

# LUODAAN VARSINAINEN SOVELLUS
# ============================
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä (event loop)
app.exec()

