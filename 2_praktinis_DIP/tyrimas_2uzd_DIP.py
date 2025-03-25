import matplotlib.pyplot as plt

def paketinio_gradientinio_nusileidimo_grafikai(epochos, mokymo_paklaidos, validavimo_paklaidos, mokymo_tikslumas, validavimo_tikslumas):
    """Paketinio gradientinio nusileidimo modelio grafikų generavimas"""
    plt.figure(figsize=(12, 6))

    plt.suptitle('Paketinio gradientinio nusileidimo grafikai', fontsize=16)

    # Paklaidos grafikas
    plt.subplot(1, 2, 1)
    plt.plot(epochos, mokymo_paklaidos, label='Mokymo paklaida')
    plt.plot(epochos, validavimo_paklaidos, label='Validavimo paklaida')
    plt.xlabel('Epochos')
    plt.ylabel('Paklaida')
    plt.title('Paklaidos priklausomybė nuo epochų skaičiaus')
    plt.legend()

    # Klasifikavimo tikslumo grafikas
    plt.subplot(1, 2, 2)
    plt.plot(epochos, mokymo_tikslumas, label='Mokymo tikslumas')
    plt.plot(epochos, validavimo_tikslumas, label='Validavimo tikslumas')
    plt.xlabel('Epochos')
    plt.ylabel('Tikslumas')
    plt.title('Klasifikavimo tikslumo priklausomybė nuo epochų skaičiaus')
    plt.legend()

    plt.tight_layout()
    plt.savefig('paketinis_gradientinis_nusileidimas1.png')  
    plt.show()

def stochastinio_gradientinio_nusileidimo_grafikai(epochos, mokymo_paklaidos, validavimo_paklaidos, mokymo_tikslumas, validavimo_tikslumas):
    """Stochastinio gradientinio nusileidimo modelio grafikų generavimas"""
    plt.figure(figsize=(12, 6))

    plt.suptitle('Stochastinio gradientinio nusileidimo grafikai', fontsize=16)

    # Paklaidos grafikas
    plt.subplot(1, 2, 1)
    plt.plot(epochos, mokymo_paklaidos, label='Mokymo paklaida')
    plt.plot(epochos, validavimo_paklaidos, label='Validavimo paklaida')
    plt.xlabel('Epochos')
    plt.ylabel('Paklaida')
    plt.title('Paklaidos priklausomybė nuo epochų skaičiaus')
    plt.legend()

    # Klasifikavimo tikslumo grafikas
    plt.subplot(1, 2, 2)
    plt.plot(epochos, mokymo_tikslumas, label='Mokymo tikslumas')
    plt.plot(epochos, validavimo_tikslumas, label='Validavimo tikslumas')
    plt.xlabel('Epochos')
    plt.ylabel('Tikslumas')
    plt.title('Klasifikavimo tikslumo priklausomybė nuo epochų skaičiaus')
    plt.legend()

    plt.tight_layout()
    plt.savefig('stohastinis_gradientinis_nusileidimas1.png')  
    plt.show()