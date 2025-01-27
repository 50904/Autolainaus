# CIPHER.PY -MODDULIN YKSIKKÖTESTIT
# =================================

import pytest # Järjestelmätason virheiden testaus
from lendingModules import cipher # Testattavan moduulin lataus

plainText = b'Selkokielitesti'
key = b'XX1jpDo7aQeDExbSlFGoSDCpSv2OMPDcGrU9YYNLx9Q='
cipherEngine = cipher.createChipher(key)
cryptoText = cipher.encrypt(cipherEngine, plainText)

def test_decrypt():
    assert cipher.decrypt(cipherEngine, cryptoText, True) == plainText

# TODO: Tee tähän testi decryptString-funktiosta
# Luodaan salateksti käyttämällä encryptString-funktiota
cryptoText2 = cipher.encryptString('Selkokieliteksti')

# Tehdään testi, joka käyttää decryptString-funktiota
def test_decryptString():
    assert cipher.decryptString(cryptoText2) == 'Selkokieliteksti'

