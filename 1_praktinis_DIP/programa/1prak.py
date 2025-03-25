import numpy as np
import matplotlib.pyplot as plt

def sugeneruoti_duomenis():
    """ Duomenų generavimas. """
    np.random.seed(40)                                   # Kad rezultatai būtų atkartojami
    klase_1 = np.random.randn(10, 2) + np.array([4, 5])  # Klasė 1: Taškai aplink tašką (4, 5)
    klase_2 = np.random.randn(10, 2) + np.array([8, 10]) # Klasė 2: Taškai aplink tašką (8, 10)
    return klase_1, klase_2

def atvaizduoti_taskus(klase_1, klase_2):
    """ Atvaizduojami tiesiškai atskirti taškai. """
    plt.scatter(klase_1[:, 0], klase_1[:, 1], color='blue', label='Klasė 1')
    plt.scatter(klase_2[:, 0], klase_2[:, 1], color='red',  label='Klasė 2')
    plt.xlabel('X ašis')
    plt.ylabel('Y ašis')
    plt.legend()
    plt.title('Tiesiškai atskirti duomenų įrašai')
    plt.grid(True)
    plt.show()

def zodynas(klase_1, klase_2):
    """ Išsaugomi duomenys pasinaudojant žodynu. """
    zodynas = {
        "klase_1": klase_1,
        "klase_2": klase_2
    }
    return zodynas

def slenkstine_funkcija(a):   
    """ Apibrėžiama slenkstinė aktyvacijos funkcija. Atitinkamai pagal sumą (a) grąžinamas 0 arba 1. """    
    return 1 if a >= 0 else 0
def sigmoidine_funkcija(a):
    """ Apibrėžiama sigmoidinė aktyvacijos funkcija. Pritaikoma sigmoidinės funkcijos formulė. """   
    sigmoidine_rezultatas = 1 / (1 + np.exp(-a))
    return 1 if sigmoidine_rezultatas >= 0.5 else 0

class Neuronas:
    """. Dirbtinio neurono klasė. """
    def __init__(self, w1, w2, b):
        self.w1 = w1 # Pirmos klasės įėjimo (x1) svoris
        self.w2 = w2 # Antros klasės įėjimo (x2) svoris
        self.b = b   # Poslinkis

    def a_apskaiciavimas(self, x1, x2):
        """ Skaičiuojama įėjimo reikšmių (x1, x2) ir svorių (w1, w2) sandaugų suma, prie kurios dar pridedamas poslinkis (b). """
        return x1 * self.w1 + x2 * self.w2 + self.b

    def spejimo_funkcija(self, x1, x2, aktyvacijos_funkcija):
        """ Atliekama prognozė: neuronas klasifikuoja įėjimo duomenis (x1 ir x2) į vieną iš dviejų klasių (0 arba 1). """
        a = self.a_apskaiciavimas(x1, x2)   
        # Atliekama prognozė pasirinktu metodu (aktyvacijos funkcija)                     
        if aktyvacijos_funkcija ==   "slenkstine":                  
            return slenkstine_funkcija(a)                              
        elif aktyvacijos_funkcija == "sigmoidine":
            return sigmoidine_funkcija(a) 

def svoriu_tinkamumo_patikra(w1, w2, b, duomenys, klases, aktyvacijos_funkcija):
    """ Tikrinama, ar svoriai bei poslinkis yra tinkami. Palyginami tikri duomenys su prognoze. """
    neuronas = Neuronas(w1, w2, b)
    for i, (x1, x2) in enumerate(duomenys): # Naudojami 1-ame punkte sugeneruoti duomenys
        spejamas_y = neuronas.spejimo_funkcija(x1, x2, aktyvacijos_funkcija)
        if spejamas_y != klases[i]:
            return False                    # Jei bent vienas taškas neteisingai klasifikuotas
    return True                             # Jei visi taškai teisingai klasifikuoti

def tieses_braizymas(w1, w2, b, spalva, label):
    """ Nubraižoma tiesė naudojant svorius ir poslinkį. """
    x_reiksmes = np.array([min(duomenys[:, 0]) - 1, max(duomenys[:, 0]) + 1])
    y_reiksmes = (-w1 * x_reiksmes - b) / w2
    plt.plot(x_reiksmes, y_reiksmes, color=spalva, label=label)


def pasirinkti_aktyvacijos_funkcija():
    """ Realizuojama galimybė pasirinkti aktyvacijos funkciją. """
    pasirinkimas = input("Pasirinkite norimą aktyvacijos funkciją (0 - sigmoidinė, 1 - slenkstinė):")
    if pasirinkimas.upper() == "0":
        print("Pasirinkote sigmoidinę aktyvacijos funkciją.")
        return "sigmoidine"
    elif pasirinkimas.upper() == "1":
        print("Pasirinkote slenkstinę aktyvacijos funkciją.")
        return "slenkstine"
    else:
        print("Nebuvo pasirinktas nei vienas iš variantų. Bus naudojama slenkstinė funkcija.")
        return "slenkstine"

def rasti_tinkamus_svoriu_rinkinius(duomenys, klases, aktyvacijos_funkcija):
    """ Ieškomi svorių rinkiniai, kurie klasifikuoja tinkamai"""
    tinkami_rinkiniai = []
    bandymu_skaicius = 0
    while len(tinkami_rinkiniai) < 3 and bandymu_skaicius < 10000:
        bandymu_skaicius += 1
        w1, w2, b = np.random.uniform(-10, 10, 3)
        if svoriu_tinkamumo_patikra(w1, w2, b, duomenys, klases, aktyvacijos_funkcija):
            tinkami_rinkiniai.append((w1, w2, b))
            print(f"Rastas tinkamas rinkinys {len(tinkami_rinkiniai)}: w1 = {w1:.2f}, w2 = {w2:.2f}, b = {b:.2f}")
    return tinkami_rinkiniai

def testuoti_rinkinius(tinkami_rinkiniai, duomenys, klases, aktyvacijos_funkcija):
    """ Tikrinami rasti rinkiniai. """
    for i, (w1, w2, b) in enumerate(tinkami_rinkiniai):
        neuronas = Neuronas(w1, w2, b)
        print(f"\nRinkinys {i + 1}: w1 = {w1:.2f}, w2 = {w2:.2f}, b = {b:.2f}")
        for j, (x1, x2) in enumerate(duomenys):
            spejamas_y = neuronas.spejimo_funkcija(x1, x2, aktyvacijos_funkcija)
            print(f"Taškas ({x1:.2f}, {x2:.2f}) – Prognozė: {spejamas_y}, Tikroji klasė: {klases[j]}")

def atvaizduoti_tieses_be_vektoriu(tinkami_rinkiniai, klase_1, klase_2):
    """ Atvaizduojami tiesiškai atskirti taškai, tiesės. """
    plt.scatter(klase_1[:, 0], klase_1[:, 1], color='blue', label='Klasė 1')
    plt.scatter(klase_2[:, 0], klase_2[:, 1], color='red', label='Klasė 2')
    plt.xlabel('X ašis')
    plt.ylabel('Y ašis')
    plt.legend()
    plt.title('Tiesiškai atskirti duomenų įrašai')
    plt.grid(True)
    plt.xlim(2, 12)
    plt.ylim(2, 12)
    spalvos = ['gray', 'green', 'pink']  
    for i, (w1, w2, b) in enumerate(tinkami_rinkiniai):
        tieses_braizymas(w1, w2, b, spalvos[i], f"Tiesė {i + 1}")
    plt.legend()
    plt.show()  

def atvaizduoti_tieses_su_vektoriais(tinkami_rinkiniai, klase_1, klase_2):
    """ Atvaizduojami tiesiškai atskirti taškai, tiesės, vektoriai. """
    plt.scatter(klase_1[:, 0], klase_1[:, 1], color='blue', label='Klasė 1')
    plt.scatter(klase_2[:, 0], klase_2[:, 1], color='red', label='Klasė 2')
    plt.xlabel('X ašis')
    plt.ylabel('Y ašis')
    plt.legend()
    plt.title('Tiesiškai atskirti duomenų įrašai')
    plt.grid(True)
    plt.xlim(2, 12)
    plt.ylim(2, 12)
    spalvos = ['gray', 'green', 'pink']
    for i, (w1, w2, b) in enumerate(tinkami_rinkiniai):
        tieses_braizymas(w1, w2, b, spalvos[i], f"Tiesė {i + 1}")
        x0 = 6
        y0 = (-w1 * x0 - b) / w2
        plt.quiver(x0, y0, w1, w2, angles='xy', scale_units='xy', scale=1, color=spalvos[i], width=0.005, label=f"Vektorius {i + 1}")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    """ Pagrindinė funkcija (main). """
    klase_1, klase_2 = sugeneruoti_duomenis()      
    atvaizduoti_taskus(klase_1, klase_2)           
    
    duomenys = np.vstack((klase_1, klase_2))    
    print(duomenys)   
    klases = np.array([0] * len(klase_1) + [1] * len(klase_2))
    
    aktyvacijos_funkcija = pasirinkti_aktyvacijos_funkcija() 
    
    tinkami_rinkiniai = rasti_tinkamus_svoriu_rinkinius(duomenys, klases, aktyvacijos_funkcija) 
    
    if tinkami_rinkiniai:
        testuoti_rinkinius(tinkami_rinkiniai, duomenys, klases, aktyvacijos_funkcija)
        if aktyvacijos_funkcija == "slenkstine":
            atvaizduoti_tieses_be_vektoriu(tinkami_rinkiniai, klase_1, klase_2)
            atvaizduoti_tieses_su_vektoriais(tinkami_rinkiniai, klase_1, klase_2)