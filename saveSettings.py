# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-muunnokset

from PySide6 import QtWidgets # Qt-vimpaimet
from saveSettings_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

import cipher # DIY modduli salaukseen, käytä Fernet-salausta

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

        # Salausavain luottamuksellisten asetusten kryptaamiseen
        # Avainta ei saa vaihtaa ohjelman käyttöönoton jälkeen!
        # Avain on luotu cipher.py
        self.secretKey = b'2bSsngqKLDl1vFNaU6tKu-FJITmWFSYrb2eXBvf8vag='
        self.cryptoEngine = cipher.createChipher(self.secretKey)

  
        # Luetaan asetustiedostot Python-sanakirjasta
        self.currentSettings = {}

        # Tarkistetaan ensin, että asetustiedot on olemassa
        try:
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            self.ui.serverLineEdit.setText(self.currentSettings['server'])
            self.ui.portLineEdit.setText(self.currentSettings['port'])
            self.ui.databaseLineEdit.setText(self.currentSettings['database'])
            self.ui.serverLineEdit.setText(self.currentSettings['userName'])
            self.ui.passwordLineEdit.setText(self.currentSettings['password'])
        except Exception as e:
            self.openWarning

        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kun Tallenna-painiketta on klikattu, kutsutaan saveToJsonFile-metodia 
        self.ui.saveSettingspushButton.clicked.connect(self.saveToJsonFile)

    
        # OHJELMOIDUT SLOTIT
        # ------------------

    # Tallennetaan käyttöliittymään syötetyt asetukset tiedostoon
    def saveToJsonFile(self):
       
        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.serverLineEdit.text()
        port = self.ui.portLineEdit.text()
        database = self.ui.databaseLineEdit.text()
        userName = self.ui.userLineEdit.text()

        # Muutetaan merkkijono tavumuotoon (byte, merkistö UTF-8)
        plainTextPassword = bytes(self.ui.passwordLineEdit.text(), 'utf-8')

        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = str(cipher.encrypt(self.cryptoEngine, plainTextPassword))

        # TODO: Lisää tähän salasana kryptaus
        
        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName,
            'password': encryptedPassword,

        }       

        # Muunnetaan sanakirja Json-muotoon
        jsonData = json.dumps(settingsDictionary)

        # Avataan asetustiedosto kirjoitetaan asetukset
        with open('setting.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)

     # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.information)
        msgBox.setWindowTitle('Puuttuvat asetukset')
        msgBox.setText('Asetuksia ei ole tehty, syötä tietokannan asetukset')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

if __name__ == "__main__":

    # Luodaan sovellus
    app = QtWidgets.QApplication(sys.argv)

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()
