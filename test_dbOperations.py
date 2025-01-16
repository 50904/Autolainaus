# TIETOKANTAYHTEYKSIEN TESTAUS
# ============================

import pytest # Virheilmoitusten testaus vaatii
import dbOperations # Testattava moduuli

settingsDictionary = {'server': 'localhost', 
                      'port': '5433',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty'}

dbconnection = dbOperations.DbConnection(settingsDictionary)

# Testataan, että yhteysmerkkijono muodostuu oikein
def test_connectionString():
    assert dbconnection.connectionString == f'dbname=testaus user=postgres password=Q2werty host=localhost port=5433'

# Testataan että taulun kaikki tiedot saadaan ja ensimmäinen rivi on Virtanen Ville
def test_readOneRow():
    resultList = dbconnection.readAllColumnsFromTable('person') # Hakee taulun kaikki rivit listaan
    assert resultList[0] == (1, 'Virtanen', 'Ville') # Ensimmäinen rivi pitäisi olla 1 Virtanen Ville


# TODO: Mieti mitä muita testejä pitää kirjoittaa