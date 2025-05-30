

# OOP  -> CLASE si OBIECTE

# definitia unei clase (sablon)
class Animal:
    ## ARE - nume

    # __ -> functii magice
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"Animalul cu nume {self.nume} are {self.varsta} ani"

    ## FACE
    def saluta(self):
        print("Salut! Numele meu este: ", self.nume)




obiect1 = Animal("Micky", 3)
print(obiect1, obiect1.nume)


obiect2 = Animal("Tom", 5)
print(obiect2, obiect2.nume)


obiect1.saluta()
obiect2.saluta()