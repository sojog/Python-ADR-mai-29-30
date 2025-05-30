

class Student:
    def __init__(self, nume, credite = 0):
        self.nume = nume
        self.credite = credite
        self.an = 1

    def __str__(self):
        return f"Studentul {self.nume} din anul {self.an} are {self.credite} credite"
    

    def trece_exemen(self, nr_cred):
        self.credite += nr_cred


    def este_integralist (self):
        return self.credite >= 10

mihai = Student("Mihai")
print(mihai)

andrei = Student("Andrei")
print(andrei)


mihai.trece_exemen(4)
print(mihai)

print(mihai.este_integralist())


mihai.trece_exemen(4)
print(mihai)

mihai.trece_exemen(3)
print(mihai)

print(mihai.este_integralist())