# import math
# class Cerc:  # am creat raza Cerc
#
#     raza = None  # atribute de obiecte de clasa
#     culoare = 'Default'
#
#     def __init__(self, raza, culoare):  # am facut constructorul pentru raza
#
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):  # metoda pentru a printa culoarea si raza cercului
#
#         print(f'Cercul are culoarea: {self.culoare}')
#         print(f'Raza cercului este: {self.raza} cm')
#
#     def aria(self):  # metoda pentru calcul arie cerc
#
#         return print(f'Aria cercului este: {self.raza ** 2 * math.pi} cm^2')
#
#     def diametru(self):
#         return print(f'Diametrul cercului este: {self.raza * 2} cm')
#
#     def circumferunta(self):
#         return print(f'Circumferinta cercului este: {self.raza * 2 * math.pi} cm')
#
# cerc1 = Cerc(raza=7, culoare='Rosu')
# cerc2 = Cerc(raza=8, culoare='Galben')
# cerc1.descrie_cerc()
# cerc1.aria()
# cerc1.diametru()
# cerc1.circumferunta()
# cerc2.descrie_cerc()

def afiseaza_factura(self):
    total = self.pret_bucata * self.cantitate
    print(tabulate([[self.nume_produs, self.cantitate, self.pret_bucata, total, date.today()]],
                   headers=['Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))