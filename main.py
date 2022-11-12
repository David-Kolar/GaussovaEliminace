class Rovnice:
    def __init__(self, val):
        self.radek = val[:]

    def __sub__(self, other):
        if isinstance(other, Rovnice):
            return self.__add__(other.__mul__(-1))
        else:
            raise TypeError("Nelze odecti")
    def __add__(self, other):
        if isinstance(other, Rovnice):
            for i in range(len(self.radek)):
                self.radek[i] += other.radek[i]
            return Rovnice(self.radek)
        else:
            raise TypeError("Nelze secist")
    def compare(self, other):
        if isinstance(other, Rovnice):
            pass
        else:
            raise TypeError("Nelze porovnat")

    def __mul__(self, other):
        if isinstance(other, int):
            for i in range(len(self.radek)):
                self.radek[i] *= other
            return Rovnice(self.radek)
        else:
            raise TypeError("Nelze vynasobit")
    def __rmul__(self, other):
        return self.__mul__(other)

def nacti_input():
    pocet_radku = int(input())
    matice = []
    for _ in range(pocet_radku):
        radek = [int(val) for val in input().split()]
        matice.append(Rovnice(radek))
    return matice

matice = nacti_input()

