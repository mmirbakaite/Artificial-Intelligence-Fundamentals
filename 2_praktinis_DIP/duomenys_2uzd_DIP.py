import random

def pasalinti_id_stulpeli(duomenys):
    """Funkcija, kuri pašalina ID stulpelį (pirmą stulpelį)."""
    return [linija[1:] for linija in duomenys]

def atnaujinti_klasiu_zymes(duomenys):
    """Funkcija, kuri keičia klasių žymes: 2 -> 0, 4 -> 1."""
    for linija in duomenys:
        if linija[-1] == '2':  # Nepiktybinis 
            linija[-1] = '0'
        elif linija[-1] == '4':  # Piktybinis 
            linija[-1] = '1'
    return duomenys

def pasalinti_trūkstamus_duomenis(linijos):
    """Funkcija, kuri pašalina eilutes, kuriose yra '?'."""
    isvalytos_linijos = []
    for linija in linijos:
        stulpeliai = linija.strip().split(',')
        if '?' not in stulpeliai:
            isvalytos_linijos.append(stulpeliai)
    return isvalytos_linijos

def ismaisyti_duomenis(duomenys):
    """Funkcija, kuri išmaišo eilutes atsitiktine tvarka."""
    random.shuffle(duomenys)
    return duomenys

def issaugoti_i_faila(duomenys, isvesties_failas):
    """Funkcija, kuri išsaugo duomenis į naują failą."""
    with open(isvesties_failas, 'w') as failas:
        for linija in duomenys:
            failas.write(','.join(linija) + '\n')

def padalinti_duomenis(duomenys, mokymo_procentai=80, validavimo_procentai=10):
    """Funkcija, kuri padalina duomenis į mokymo, validavimo ir testavimo aibes."""
    eiluciu_skaicius = len(duomenys)
    mokymo_indeksas = int(eiluciu_skaicius * mokymo_procentai / 100)
    validavimo_indeksas = mokymo_indeksas + int(eiluciu_skaicius * validavimo_procentai / 100)
    mokymo_duomenys = duomenys[:mokymo_indeksas]                            # 80:
    validavimo_duomenys = duomenys[mokymo_indeksas:validavimo_indeksas]     # :10:
    testavimo_duomenys = duomenys[validavimo_indeksas:]                     # :10
    return mokymo_duomenys, validavimo_duomenys, testavimo_duomenys         

def main(ivesties_failas, isvesties_failas):
    """Pagrindinė programa."""

    # 1. Nuskaityti duomenis iš failo
    with open(ivesties_failas, 'r') as failas:
        linijos = failas.readlines()
    # 2. Pašalinti eilutes su trūkstamais duomenimis ('?')
    isvalyti_duomenys = pasalinti_trūkstamus_duomenis(linijos)
    # 3. Pašalinti ID stulpelį
    duomenys_be_id = pasalinti_id_stulpeli(isvalyti_duomenys)
    # 4. Atnaujinti klasių žymes
    atnaujinti_duomenys = atnaujinti_klasiu_zymes(duomenys_be_id)
    # 5. Išmaišyti eilutes atsitiktine tvarka
    ismaisyti_duomenys = ismaisyti_duomenis(atnaujinti_duomenys)
    # 6. Išsaugoti visus duomenis į vieną failą (esamas funkcionalumas)
    issaugoti_i_faila(ismaisyti_duomenys, isvesties_failas)
    
    # 7. Papildomas funkcionalumas: padalinti duomenis ir išsaugoti į tris failus
    mokymo_duomenys, validavimo_duomenys, testavimo_duomenys = padalinti_duomenis(ismaisyti_duomenys)
    issaugoti_i_faila(mokymo_duomenys, '2uzd_MokymoDuomenys_DIP.data')
    issaugoti_i_faila(validavimo_duomenys, '2uzd_ValidavimoDuomenys_DIP.data')
    issaugoti_i_faila(testavimo_duomenys, '2uzd_TestavimoDuomenys_DIP.data')

    print(f"Duomenys sėkmingai apdoroti ir išsaugoti į {isvesties_failas}")
    print("Papildomai duomenys išskirstyti į tris failus:")
    print("- 2uzd_MokymoDuomenys_DIP.data (mokymo duomenys)")
    print("- 2uzd_ValidavimoDuomenys_DIP.data (validavimo duomenys)")
    print("- 2uzd_TestavimoDuomenys_DIP.data (testavimo duomenys)")

if __name__ == "__main__":
    """Pagrindinės programos paleidimas."""
    ivesties_failas = 'breast-cancer-wisconsin.data'
    isvesties_failas = '2uzd_ParuostiDuomenys_DIP.data'
    main(ivesties_failas, isvesties_failas)