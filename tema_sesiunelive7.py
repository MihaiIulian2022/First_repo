# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    @classmethod
    def descrie(self):
        print('Cel mai probabil am colturi')

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        aria = self.__latura**2
        return aria

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura
        print(f'Setter: Noua latura este {self.__latura}')

    @latura.deleter
    def latura(self):
        self.__latura = None
        print(f'Deleter: Am sters latura')

# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        print(f'Aria este {self.PI * self.__raza ** 2}')

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza
        print(f'Setter: Noua raza este {self.__raza}')

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui
    def descrie(self):
        print('Eu nu am colturi')

p1 = Patrat(20)
p1.descrie()
p1.aria()
p1.latura = 30
p1.aria()
del p1.latura
p1.descrie()

print('-----------------------')

c1 = Cerc(10)
c1.aria()
c1.raza
c1.raza = 50
del c1.raza

c1.descrie()
