# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
import math
class Cerc:
    # atribute/fields
    raza = None
    culoare = None

    # constructor pentru cele doua atribute
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # metode
    def descrie_Cerc(self):
        print(f'Raza cercului este {self.raza} iar culoarea cercului este {self.culoare}')

    def aria(self):
        print(f'Aria cercului este {math.pi*self.raza**2}')

    def diametru(self):
        print(f'Diametrul cercului este {self.raza*2}')

    def circumferinta(self):
        print(f'Circumferinta cercului este {math.pi*self.raza*2}')

cerc1 = Cerc(9, 'galben')
cerc2 = Cerc(8, 'verde')
cerc1.descrie_Cerc()
cerc2.descrie_Cerc()
cerc1.aria()
cerc2.aria()
cerc1.diametru()
cerc2.diametru()
cerc1.circumferinta()
cerc2.circumferinta()


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().
class Dreptunghi:
    # atribute/fields
    lungime = None
    latime = None
    culoare = None

    # constructor
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # metode
    def descrie(self):
        print(f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}')

    def aria(self):
        print(f'Aria dreptunghiului este {self.lungime*self.latime}')

    def perimetru(self):
        print(f'Perimetrul dreptunghiului este {self.lungime*2 + self.latime*2}')

    def schimba_culoare(self):
        noua_culoare = input('introdu o noua culoare: ')
        self.culoare = noua_culoare

dreptunghi_de_proba = Dreptunghi(8,5,'verde')
dreptunghi_de_proba.descrie()
dreptunghi_de_proba.aria()
dreptunghi_de_proba.perimetru()
dreptunghi_de_proba.schimba_culoare()
dreptunghi_de_proba.descrie()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
class Angajat:
    # atribute/fields
    nume = None
    prenume = None
    salariu = None

    # constructor
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    # metode
    def descrie(self):
        print(f'Angajatul {self.nume} {self.prenume} are salariul {self.salariu} lei')

    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este {self.salariu}')

    def salariu_anual(self):
        print(f'Salariul anual este {self.salariu*12}')

    def marire_salariu(self, procent):
        print(f'Marirea salariului este {self.salariu*procent/100}')

angajat1= Angajat('Lacriceanu', 'Mihai', 5000)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(10)

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
class Cont:
    # atribute/fields
    iban = None
    titular_cont = None
    sold = None

    # constructor
    def __init__(self, iban, titular_cont, sold):
         self.iban = iban
         self.titular_cont = titular_cont
         self.sold = sold

    # metode
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        # print(f'Contul {self.iban} se debiteaza cu suma de {suma}')
        # print(f'Noul sold este {self.sold-suma}')
        self.sold = self.sold - suma
    def creditare_cont(self, suma):
        # print(f'Contul {self.iban} se crediteaza cu suma de {suma}')
        # print(f'Noul sold este {self.sold + suma}')
        self.sold = self.sold + suma

cont1 = Cont('ro01','Lacriceanu Mihai', 3000)
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.afisare_sold()
cont1.creditare_cont(1000)
cont1.afisare_sold()

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date
today = date.today()
class Factura:
    #atribute/fields
    seria = 'SR'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    # constructor pentru tot exceptand seria
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self,cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print(f'Factura seria {self.seria} numar {self.numar}\n'
          f'Data: {date.today()}\n'
          f'Produs | cantitate | pret bucata | Total\n'
          f'{self.nume_produs}| {self.cantitate} | {self.pret_buc}  |  {self.pret_buc * self.cantitate}')

factura1 = Factura(1, 'mouse', 1, 15)
factura1.schimba_cantitatea(20)
factura1.schimba_pretul(20)
factura1.schimba_nume_produs('tastatura')
factura1.genereaza_factura()

# nu merge la ex1 optional asta, nu stiu ce sa i fac si ma enerveaza :))

# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
class Masina:
    # atribute/fields
    marca = 'BMW'
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'rosu', 'albastru', 'galben', 'verde', 'roz'}
    inmatriculata = False

    # constructor
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    # metode
    #   def descrie(self):


# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict
