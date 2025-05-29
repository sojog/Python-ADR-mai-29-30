
def rezolva(bancnote, suma):
    for banc in bancnote:
        print(f"Bancnota de {banc}:  {suma // banc}")
        suma %= banc


rezolva([10, 5, 2, 1], 128)

rezolva([10, 5, 2, 1], 139)

rezolva([50, 20, 5, 1], 139)