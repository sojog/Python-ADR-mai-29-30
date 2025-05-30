
v1 = [10, 20, 30] # lista ->  mutabil  (creare, adaugare, modific, sterg)
v2 = (10, 20, 30) # tuplu -> imutabil  (creare)

print(v1, type(v1))
print(v2, type(v2))

print(v1[0])
print(v2[0])

print(v1[-1])
print(v2[-1])

v2.append(10)
print(v2)

