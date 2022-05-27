import random

class Asiakas:
    """
    nimi: str
    asiakasnro: int
    ika: int
    """

    def __init__(self, nimi, ika):
        self._ika = ika
        self._nimi = nimi
        self._asiakasnro = self.luo_nro()


    def set_ika(self, ika):
        
        if ika == False:
            raise ValueError("Anna uusi ikä")
        if ika == True:
            self._ika = int(ika)

    def set_nimi(self, nimi):
        if nimi == False or nimi == "":
            raise ValueError("Anna uusi nimi")
        if nimi == True:
            self._nimi = str(nimi)


    def get_ika(self):
        return self._ika

    def get_nimi(self):
        return self._nimi

    def get_asiakasnro(self):
        return self._asiakasnro

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
    """
    tuotenimi: str
    asiakasrivi: str
    asiakkaat: Asiakas[]
    """

    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self._asiakkaat = []
                 

    def lisaa_asiakas(self, asiakas):
        if asiakas == False or asiakas == None:
            raise ValueError("Anna uusi Asiakas")
        else:
            self._asiakkaat.append(asiakas)
        

    def poista_asiakas(self, asiakas):
        try:
           self._asiakkaat.remove(asiakas)
        except:
            pass
        

    def luo_asiakasrivi(self, asiakas):
        txt = f"{asiakas._nimi} ({asiakas.get_asiakasnro()[0]}-{asiakas.get_asiakasnro()[1]}-{asiakas.get_asiakasnro()[2]}) on {asiakas._ika}-vuotias."
        return txt
        

        
    def tulosta_asiakkaat(self):
        print("\nTuotteen " + self.tuotenimi + " asiakkaat ovat: ")
        for asiakas in self._asiakkaat:
            print(self.luo_asiakasrivi(asiakas))   




class ParempiPalvelu(Palvelu):
    """
    edut: str[]
    """

    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self._edut = []

    def lisaa_etu(self, etu):
        if etu == False or etu == None:
            raise ValueError("Anna uusi etu")
        else:
            self._edut.append(etu)

    def poista_etu(self, etu):
        try:
            self._edut.remove(etu)
        except:
            pass

    def tulosta_edut(self):
        print("\nTuotteen " + self.tuotenimi + " edut ovat: ")
        for etu in self._edut:
            print(etu)
