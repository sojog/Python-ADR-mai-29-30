# Intr-un string se află niste numere despărtite de virgulă. 
# Acele numere trebuie citite într-o listă. 
# Elementele liste care apar o singură dată trebuie adunate. 
# Creati o functie prin care calculati suma acestora.

def identificare_nr_unic(numere):
    lista_unica = []
    for i in numere: 
        if numere.count(i) == 1:
            lista_unica.append(i)

    return lista_unica

lista = [2, 3, 4, 5, 3, 5, 6, 3, 4, 7]
print(identificare_nr_unic(lista))



def identificare_nr_unic(numere):
    lista_unica = []
    lista_non_unice = []
    # 0, 2
    # 1, 3
    for index, element in enumerate(numere): 
        elementul_este_duplicat = False
        for i in range(index + 1, len(numere)):
            if numere[i] == element:
                elementul_este_duplicat = True
        
        if not elementul_este_duplicat and element not in lista_non_unice:
            lista_unica.append(element)
        else: 
            lista_non_unice.append(element)

    return lista_unica

lista = [2, 3, 4, 5, 3, 5, 6, 3, 4, 7]
print(identificare_nr_unic(lista))