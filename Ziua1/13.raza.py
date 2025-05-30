"""Creaţi un program care va cere de la utilizator valoarea razei şi va afisa aria cercului."""

# \n  -> new line
# \ -> escaping
raza = input("Introduceti raza \n")
raza = int(raza)

# Conventie -> LITERE MARI == CONSTANTA
PI = 3.14 

print("Aria = ", raza ** 2 * PI)

print("Aria = " +  str(raza ** 2 * PI))


print(f"Aria = {raza ** 2 * PI}" )