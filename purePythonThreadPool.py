# PYTHONIN SÄIEVARANTO
# ====================

import concurrent.futures # Säievarantojen luominen
import time # Viiveiden tuottaminen

# Työfunktio, jota suoritetaan säikeessä
def longLastingFunction(parameter):
    time.sleep(10) # Odotetaan 10 sekunttia
    print(parameter)

    # Luodaan säievaranto
    pool = concurrent.futures.ThreadPoolExecutor
    
    # Luodaan säie, jossa suoritetaan työfunktio
    pool.submit(longLastingFunction('Hippopotamus'))

    # Tulostetaan pääsäikeen olevan valmis
    print('Valmis')