import time


def decorator(func):
    def wrapper(*args, **kargs):
        print("Inainte de a chema functia originala")
        start_time = time.time()
        rezultat = func(*args,  **kargs)
        print("Dupa ce chem functia originala")
        stop_time = time.time()
        print(f"Functia a fost executat in {stop_time - start_time}")

        return rezultat
   
    return wrapper


@decorator
def adunare(x, y):
    time.sleep(3)
    return x + y

def scadere(x, y):
    return x - y

print(adunare(2, 3))