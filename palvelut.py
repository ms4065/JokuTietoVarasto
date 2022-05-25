class Asiakas:
    """
    nimi: str
    asiakasnro: int
    ika: int
    """

    def __init__(self, nimi, ika, asiakasnro = []):
        self.ika = ika
        self.nimi = nimi
        self.asiakasnro = asiakasnro


    def set_ika(self, ika):
        
        if ika == False:
            raise ValueError("Anna uusi ikä")
        if ika == True:
            self.ika = int(ika)

    def set_nimi(self, nimi):
        if nimi == False:
            raise ValueError("Anna uusi nimi")
        if nimi == True:
            self.nimi = str(nimi)


    def get_ika(self):
        return int(self.ika)

    def get_nimi(self):
        return str(self.nimi)

    def get_asiakasnro(self):
        txt = "f'{42:03}'"
        return txt.format(self.asiakasnro)

        
    def luo_nro():
        for x in range(8):
            self.asiakasnro.append(random.randint(0, 9))
        




class Palvelu(Asiakas):

    asiakkaat = []

    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
                 

    def lisaa_asiakas(self, Asiakas):
        if Asiakas == False:
            raise "Anna uusi Asiakas"
        if Asiakas == True:
            self.asiakkaat.append(Asiakas)
        

    def poista_asiakas(self, Asiakas):
        try:
           self.asiakkaat.remove(Asiakas)
        except:
            pass
        

    def luo_asiakasrivi(self, Asiakas):
        txt = "f'{nimi}, {asiakasnro} on {ika} -vuotias.".format('', asiakas.nimi())
        print(txt)

        
    def tulosta_asiakkaat(self):
        for asiakas in self.asiakkaat:
            print(self.luo_asiakasrivi(asiakas))   




class ParempiPalvelu(Palvelu):

    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, etu):
        if etu == False:
            raise "Anna uusi etu"
        if etu == True:
            self.edut.append(etu)

    def poista_etu(self, etu):
        try:
            self.edut.remove(etu)
        except:
            pass

    def tulosta_edut(self):
        print(self.edut)
