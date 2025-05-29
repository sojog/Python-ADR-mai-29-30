bancnote = []

for i in range(4):
    banc = input("Introdu bancnota \n")
    banc = int(banc)
    bancnote.append(banc)
    print(bancnote)

suma = 128

for banc in bancnote:
    print(f"Bancnota de {banc}:  {suma // banc}")
    suma %= banc