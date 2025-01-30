# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # Json-tiedostojen käsittely

from PySide6 import QtWidgets # Qt-vimpaimet

from lendingModules import sound # Äänitoiminnot
from lendingModules import dbOperations # Tietokantatoiminnot
from lendingModules import cipher # Salausmoduuli

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

                # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            # Avataam asetustiedosto ja muutetaan se Python sanakirjaksi
            with open('settings.json', 'rt') as settingsFile: # With sulkee tiedoston automaattisesti
                
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)
            
            # Puretaan salasana tietokantaoperaatioita varten  
            self.plainTextPassword = cipher.decryptString(self.currentSettings['password'])
        except Exception as error:
            self.openWarning()

        # Äänet oletuksena käytössä
        self.soundOnPictureLabel = True


        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        self.setInitialElements(self)


        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Palauta käyttöliittymä alkutilanteeseen
    def setInitialElements(self):
        self.ui.returnCarPushButton.show()
        self.ui.borrowCarPushButton.show()
        self.ui.calendarPictureLabel.hide()
        self.ui.clockTimeLabel.hide()
        self.ui.dateTimeLabel.hide()
        self.ui.goBackPictureLabel.hide()
        self.ui.readyKeyLineEdit.hide()
        self.ui.keyPicturesLabel.hide()
        self.ui.readLicenceLineEdit.hide()
        self.ui.keyBarcodeLineEdit.clear()
        self.ui.keyBarcodeLineEdit.hide()
        self.ui.soundOnPictureLabel.hide()
        self.ui.ssnLineEdit.clear()
        self.ui.ssnLineEdit.hide()
        self.ui.statusLabel.hide()
        self.ui.dateTimeLabel.hide()
        self.ui.lenderNameLabel.hide()
        self.ui.carinfoLabel.hide()

        # Kun Lainaa-painiketta painetaan, kutsutaan activateLender metodia 
        self.ui.takeCarPushButton.clicked.connect(self.activateLender)

        # Kun ajokortin viivakoodi on luettu, kutsutaan activateKey-metodia
        self.ui.ssnLineEdit.returnPressed.connect(self.activateKey)

        # Kun avaimenperä on luettu, kutsutaan setLendingData
        self.ui.keyBarcodeLineEdit.returnPressed.connect(self.setLendingData)

        # Kun OK-painiketta on painettu, tallenna tiedot ja palauta käyttöliittymä alkutilaan
        self.ui.okPushButton.clicked.connect(self.saveLendingData)
        
        # Kun palauta-painiketta on painettu, kutsutaan activateReturnCar-metodia
        self.ui.returnCarPushButton.clicked.connect(self.activateReturnCar)

        # Kun avaimenperä on luettu palautettaessa, kutsutaan saveReturnData-metodia
        self.ui.keyReturnBarcodeLineEdit.returnPressed.connect(self.saveReturnData)

        # Kun mykistä painkietta painetaan kutsutaan mute-metodia
        self.ui.soundOffPictureLabel.clicked.connect(self.mute)

        # Kun äänipainiketta painetaan kutsutaan unmute-metodia
        self.ui.soundOnPictureLabel.clicked.connect(self.unmute)

        # Kun kumoa painiketta painetaan palautetaan UI-alkutilaan
        self.ui.goBackpushButton.clicked.connect(self.goBack)

    # OHJELMOIDUT SLOTIT
    # ------------------

    # Näyttää lainaajan kuvakkeen ja henkilötunnuksen kentän
    def activateLender(self):
        self.ui.statusLabel.setText('Auton lainaus')
        self.ui.lenderPictureLabel.show()
        self.ui.ssnLineEdit.show()
        self.ui.goBackPictureLabel.show()
        self.ui.ssnLineEdit.setFocus()
        self.ui.returnCarPushButton.hide()
        self.ui.borrowCarPushButton.hide()
        self.ui.statusLabel.show()
        self.ui.statusbar.showMessage('Syötä ajokortti koneeseen')
        if self.soundOn:
            sound.playWAV('Sounds\\drivingLicence.WAV')


    # Näyttää avaimen kuvakkeen, rekisterikenttä ja lainaajan tiedot
    def activateKey(self):
        self.ui.keyPicturesLabel.show()
        self.ui.keyBarcodeLineEdit.show()
        self.ui.keyBarcodeLineEdit.setFocus()
        self.ui.lenderNameLabel.show()

    # Näyttää lainauksen loput tiedot
    def setLendingData(self):
        self.ui.carinfoLabel.show()
        self.ui.dateTimeLabel.show()
        self.ui.clockTimeLabel.show()
        self.ui.okPushButton.show()

    # Tallennetaan lainauksen tiedot ja palautetaan käyttöliittymä alkutilaan
    def saveLendingData(self):
        # Save data to the database
        ssn = self.ui.ssnLineEdit.text()
        key = self.ui.keyBarcodeLineEdit.text()
        dbOperations.DbConnection()
        self.setInitialElements()
        self.ui.statusbar.showMessage('Auton lainaustiedot tallennettiin', 5000)
        
    
    # Näytetään palautukseen liittyvät kentät ja kuvat 
    def activateReturnCar(self):
        self.ui.borrowCarPushButton.hide()
        self.ui.returnCarPushButton.show()
        self.ui.keyPicturesLabel.show()
        self.ui.keyReturnBarcodeLineEdit.show()
        self.ui.keyReturnBarcodeLineEdit.setFocus()
        self.ui.statusbar.showMessage('Lue avaimen viivakoodi')
        if self.soundOn:
            sound.playWav('sounds\\lendingOK.Wav')

    # TODO: Laita seuraava lohko virheenkäsittelyn sisälle
    # Luodaan tietokantayhteys olioon

    # Tallennetaan palautuksen tiedot tietokantaan ja palautetaan UI alkutila
    def saveReturnData(self):
        self.ui.statusbar.showMessage('Auto palautettu')
        self.setInitialElements()
    
    # Mykistetään äänet
    def mute(self):
        self.soundOffPictureLabel.hide()
        self.ui.soundOnPictureLabel.show()
        self.ui.statusbar.showMessage('Äänet mykistetty')
        self.sounfOn = False
    
    # Poistetaan mykistys
    def unmute(self):
        self.soundOffPictureLabel.show()
        self.ui.statusbar.showMessage('Äänet päällä')
        self.ui.soundOnPictureLabel.hide()
        self.sounfOn = True

    def goBack(self):
        self.setInitialElements()
        self.ui.statusbar.showMessage('Toiminto peruutettiin', 5000)


    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Tietokantayhteyttä ei voitu muodostaa')
        msgBox.setText('Ota yhteyttä järjestelmän valvojaan')
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

