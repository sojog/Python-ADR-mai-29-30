
while True:
    x = input("Introduceti un numar \n")
    print(x, type(x))

    if x.isnumeric():
        x = int(x)
        print(x, type(x))
    else:
        print("numarul nu poate fi transformat")