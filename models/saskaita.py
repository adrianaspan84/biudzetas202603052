import pickle
from models.pajamos import Pajamos
from models.islaidos import Islaidos

class Saskaita:
    def __init__(self):
        self.zurnalas = self.nuskaityti()

    def irasyti(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def nuskaityti(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def prideti_pajamas(self):
        suma = int(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        pajamos = Pajamos(suma, siuntejas, info)
        self.zurnalas.append(pajamos)
        self.irasyti()

    def prideti_islaidas(self):
        suma = int(input("Suma: "))
        isigyta = input("Įsigyta prekė/paslauga: ")
        info = input("Papildoma informacija: ")
        islaidos = Islaidos(suma, isigyta, info)
        self.zurnalas.append(islaidos)
        self.irasyti()

    def paskaiciuoti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is Pajamos:
                balansas += irasas.suma
            if type(irasas) is Islaidos:
                balansas -= irasas.suma
        print("Balansas:", balansas)
