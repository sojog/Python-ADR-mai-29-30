
# 128 -> 10 * 12 + 1 * 5 + 1 * 2 + 1 * 1 

bancnote = [10, 5, 2, 1]
suma = 128

for banc in bancnote:
    print(f"Bancnota de {banc}:  {suma // banc}")
    suma %= banc

