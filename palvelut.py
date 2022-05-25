import random

class Asiakas:
    """
    nimi: str
    asiakasnro: int
    ika: int
    """

    def __init__(self, nimi, ika):
        self.ika = ika
        self.nimi = nimi
        self.asiakasnro = self.luo_nro()


    def set_ika(self, ika):
        
        if ika == False:
            raise ValueError("Anna uusi ikä")
        if ika == True:
            self.ika = int(ika)

    def set_nimi(self, nimi):
        if nimi == False or nimi == "":
            raise ValueError("Anna uusi nimi")
        if nimi == True:
            self.nimi = str(nimi)


    def get_ika(self):
        return self.ika

    def get_nimi(self):
        return self.nimi

    def get_asiakasnro(self):
        return self.asiakasnro

    def luo_nro(self):
        lista = []

        uusinumero = ""
        for x in range(2):
            uusinumero = uusinumero + str(random.randint(0,9))
        lista.append(int(uusinumero))
        for y in range(2):
            uusinumero = ""
            for x in range(3):
                uusinumero = uusinumero + str(random.randint(0,9))
            lista.append(int(uusinumero))
        return lista




class Palvelu():

    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.asiakkaat = []
                 

    def lisaa_asiakas(self, asiakas):
        if asiakas == False or asiakas == None:
            raise ValueError("Anna uusi Asiakas")
        else:
            self.asiakkaat.append(asiakas)
        

    def poista_asiakas(self, asiakas):
        try:
           self.asiakkaat.remove(asiakas)
        except:
            pass
        

    def luo_asiakasrivi(self, asiakas):
        txt = f"{asiakas.nimi} ({asiakas.get_asiakasnro()[0]}-{asiakas.get_asiakasnro()[1]}-{asiakas.get_asiakasnro()[2]}) on {asiakas.ika}-vuotias."
        return txt
        

        
    def tulosta_asiakkaat(self):
        print("\nTuotteen " + self.tuotenimi + " asiakkaat ovat: ")
        for asiakas in self.asiakkaat:
            print(self.luo_asiakasrivi(asiakas))   




class ParempiPalvelu(Palvelu):

    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, etu):
        if etu == False or etu == None:
            raise ValueError("Anna uusi etu")
        else:
            self.edut.append(etu)

    def poista_etu(self, etu):
        try:
            self.edut.remove(etu)
        except:
            pass

    def tulosta_edut(self):
        print("\nTuotteen " + self.tuotenimi + " edut ovat: ")
        for etu in self.edut:
            print(etu)
