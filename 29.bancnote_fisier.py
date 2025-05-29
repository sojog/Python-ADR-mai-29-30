

bancnote = []
with open("bancnote.txt") as freader:
    continut = freader.read()
    bancnote = continut.splitlines() # \n
    print(bancnote)

suma = 128

for banc in bancnote:
    print(f"Bancnota de {banc}:  {suma // int(banc)}")
    suma %= int(banc)