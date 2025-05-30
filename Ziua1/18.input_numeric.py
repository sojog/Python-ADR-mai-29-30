

nr = input("Introdu un numar\n")

while not nr.isnumeric():
    nr = input("Introdu o valoare care poate fi transformta in int\n")

nr = int(nr)
print( nr ** 3)