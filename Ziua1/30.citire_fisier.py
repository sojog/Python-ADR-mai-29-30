f = open("bancnote.txt")
continut = f.read()
print(continut)
f.close()


with open("bancnote.txt") as f:
    continut = f.read()
    print(continut)


with open("bancnote.txt") as f:
    continut = f.readlines()
    print(continut)