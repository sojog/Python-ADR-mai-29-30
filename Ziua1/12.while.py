

secret = 123
introdus = input("Introduceti valoarea ")

while secret != introdus:
    print("Nu ai ghicit")
    introdus = input("Introduceti valoarea ")
    print("Ai introdus", introdus, type(introdus))
    introdus = int(introdus)
    print("Ai introdus", introdus, type(introdus))

print("Ai ghicit")