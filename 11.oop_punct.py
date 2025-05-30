"""Trebuie creată clasa Point care sa abstractizeze un punct dintr-un plan (coordonate x si y)
Clasa deţine următoarele caracteristici:
Punctul x si punctul y
Clasa deţine următoarele implementari:
show - se printeaza coordinatele punctului;
move - se muta coordonatele;
setToOrigin - se seteaza coordinatele (0, 0);
dist - distanta intre doua puncte"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Punctul la coordonatele ({self.__x}, {self.__y})"
    

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_value):
        if isinstance(new_value, int):
            self.__x = new_value




p1 = Point(2, 3)
print(p1)

print(p1.x)

p1.x = 30
print(p1.x)

p1.x = "mare"
print(p1.x)