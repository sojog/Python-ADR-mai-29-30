

class Masina:

    def __init__(self, km, numar, serie, cp):

        # public -> accesibil in afara clasei
        self.km = km

        # protected/internal -> neaccesibil in afara clasei, dar accesibil in clasa mostenita
        self._numar = numar
        self._cp = cp


        # private -> neaccesibil in afara clasei, si neaccesibil in clasa mostenita 
        self.__serie = serie

    def __str__(self):
        return f"Masina cu numarul { self._numar}"

class MasinaElectrica(Masina):
    def __init__(self, autonomie, km, numar, serie, cp):
        super().__init__(km, numar, serie, cp)
        self.autonomie = autonomie


    def __str__(self):
        return super().__str__() + f" are autonomie de {self.autonomie} km"






bmw = Masina(100, "B32fsd", "SERIE123", 100)
# IN afara clasei
print(bmw.km)
print(bmw._numar)

bmw._numar = "fjhsdkjfhs"
print(bmw._numar)

print(bmw._Masina__serie )


tesla = MasinaElectrica(321,200, "BC32fsd", "SERIE000", 400)
print(tesla)