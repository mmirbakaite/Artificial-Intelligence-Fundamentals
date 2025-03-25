import numpy as np
import pandas as pd
import time
from tyrimas_2uzd_DIP import paketinio_gradientinio_nusileidimo_grafikai

def sigmoidine_funkcija(z):
    """Sigmoidinė funkcija."""
    return 1 / (1 + np.exp(-z))

def nuskaityti_duomenis(failas):
    """Duomenų nuskaitymas iš failo."""
    df = pd.read_csv(failas, header=None)
    pozymiai = df.iloc[:, :-1].values
    klase = df.iloc[:, -1].values
    return pozymiai, klase

def a_apskaiciavimas(pozymiai, svoriai, poslinkis):
    """Aktyvacijos funkcijos įėjimo reikšmės apskaičiavimas."""
    return np.dot(pozymiai, svoriai) + poslinkis

def paketinis_gradientinis_nusileidimas(mokymo_pozymiai, mokymo_klase, mokymosi_greitis=0.05, epochos=10000, mokymo_riba=1e-6, validavimo_pozymiai=None, validavimo_klase=None):
    """Sigmoidinio neurono mokymas gradientinį taikant paketinį gradientinį nusileidimą."""
    np.random.seed(150)
    m, n = mokymo_pozymiai.shape
    svoriai = np.random.randn(n)
    poslinkis = np.random.randn()
    totalError = float('inf')
    epocha = 0

    mokymo_totalErrors_grafikui = []
    validavimo_totalErrors_grafikui = []
    mokymo_tikslumas_grafikui = []
    validavimo_tikslumas_grafikui = []
    
    pradzios_laikas = time.time()

    while totalError > mokymo_riba and epocha < epochos:
        totalError = 0
        gradientSum = np.zeros(n)
        
        for i in range(m):
            z = a_apskaiciavimas(mokymo_pozymiai[i], svoriai, poslinkis)
            yi = sigmoidine_funkcija(z)
            ti = mokymo_klase[i]
            
            for k in range(n):
                gradientSum[k] += (yi - ti) * yi * (1 - yi) * mokymo_pozymiai[i, k]

            error = (ti - yi) ** 2
            totalError += error
            totalError_avg = totalError / (i + 1)  
        
        for k in range(n):
            svoriai[k] -= mokymosi_greitis * (gradientSum[k] / m)
        
        epocha += 1
        
        mokymo_prognoze = np.round(sigmoidine_funkcija(np.dot(mokymo_pozymiai, svoriai) + poslinkis))
        mokymo_tikslumas = np.mean(mokymo_prognoze == mokymo_klase)
        mokymo_totalErrors_grafikui.append(totalError_avg)
        mokymo_tikslumas_grafikui.append(mokymo_tikslumas)
        
        validavimo_pradzios_laikas = time.time()
        # Klasifikavimo tikslumo ir paklaidos skaičiavimas su validavimo duomenimis
        if validavimo_pozymiai is not None and validavimo_klase is not None:
            validavimo_prognoze = np.round(sigmoidine_funkcija(np.dot(validavimo_pozymiai, svoriai) + poslinkis))
            validavimo_tikslumas = np.mean(validavimo_prognoze == validavimo_klase)
            validavimo_paklaida = np.mean((validavimo_klase - validavimo_prognoze) ** 2)
            print(f"Epocha {epocha}: Paklaida mokymo metu = {totalError_avg:.6f}, Tikslumas mokymo metu = {mokymo_tikslumas:.4f}, Paklaida validavimo metu = {validavimo_paklaida:.6f}, Tikslumas validavimo metu = {validavimo_tikslumas:.4f}")
        else:
            print(f"Epocha {epocha}: Paklaida mokymo metu = {totalError_avg:.6f}, Tikslumas mokymo metu = {mokymo_tikslumas:.4f}")
        validavimo_pabaigos_laikas = time.time()
        bendras_validavimo_laikas = validavimo_pabaigos_laikas - validavimo_pradzios_laikas
        validavimo_totalErrors_grafikui.append(validavimo_paklaida)
        validavimo_tikslumas_grafikui.append(validavimo_tikslumas)

    pabaigos_laikas = time.time()
    bendras_laikas = pabaigos_laikas - pradzios_laikas
    bendras_mokymo_laikas = bendras_laikas - bendras_validavimo_laikas
    print(f"\nNeurono mokymo laikas: {bendras_mokymo_laikas:.4f} sekundės")
    
    return svoriai, poslinkis, mokymo_totalErrors_grafikui, validavimo_totalErrors_grafikui, mokymo_tikslumas_grafikui, validavimo_tikslumas_grafikui

def testavimas(testavimo_pozymiai, testavimo_klase, svoriai, poslinkis):
    """Tikslumas ir paklaida su testavimo duomenimis."""
    testavimo_prognoze = np.round(sigmoidine_funkcija(np.dot(testavimo_pozymiai, svoriai) + poslinkis))
    testavimo_tikslumas = np.mean(testavimo_prognoze == testavimo_klase)
    testavimo_paklaida = np.mean((testavimo_klase - testavimo_prognoze) ** 2)
    return testavimo_tikslumas, testavimo_paklaida

def main():
    """Pagrindinė funkcija main."""
    mokymo_duomenys = "2uzd_MokymoDuomenys_DIP.data"
    validavimo_duomenys = "2uzd_ValidavimoDuomenys_DIP.data"
    testavimo_duomenys = "2uzd_TestavimoDuomenys_DIP.data"  
    
    # Epochų skaičiaus ir mokymo greičio įvedimas
    epochos = int(input("Įveskite epochų skaičių: "))
    mokymosi_greitis = float(input("Įveskite mokymo greitį (nuo 0 iki 1): "))
    
    # Duomenų nuskaitymas
    mokymo_pozymiai, mokymo_klase = nuskaityti_duomenis(mokymo_duomenys)
    validavimo_pozymiai, validavimo_klase = nuskaityti_duomenis(validavimo_duomenys)
    testavimo_pozymiai, testavimo_klase = nuskaityti_duomenis(testavimo_duomenys)
    
    # Modelio mokymas su mokymo duomenimis ir patikrinimas su validavimo duomenimis
    svoriai, poslinkis, mokymo_totalErrors_grafikui, validavimo_totalErrors_grafikui, mokymo_tikslumas_grafikui, validavimo_tikslumas_grafikui = paketinis_gradientinis_nusileidimas(
        mokymo_pozymiai, mokymo_klase, mokymosi_greitis=mokymosi_greitis, epochos=epochos, validavimo_pozymiai=validavimo_pozymiai, validavimo_klase=validavimo_klase
    )

    print("\nMokymo rezultatai:")
    print(f"Svoriai: {svoriai}")
    print(f"Poslinkis (bias): {poslinkis}")
    
    # Kreipiamasis į funkciją grafikų generavimui
    paketinio_gradientinio_nusileidimo_grafikai(range(epochos), mokymo_totalErrors_grafikui, validavimo_totalErrors_grafikui, mokymo_tikslumas_grafikui, validavimo_tikslumas_grafikui)

    # Rezultatų išvedimas su testavimo duomenimis
    testavimo_tikslumas, testavimo_paklaida = testavimas(testavimo_pozymiai, testavimo_klase, svoriai, poslinkis)
    print(f"Paklaida testavimo metu = {testavimo_paklaida:.6f}, Tikslumas testavimo metu = {testavimo_tikslumas:.4f}\n")

if __name__ == "__main__":
    """Pagrindinės funkcijos paleidimas."""
    main()
