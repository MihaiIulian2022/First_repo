# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Având lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
for i in range(len(masini)):
    print(f'Masina mea preferata este: {masini[i]}')
    i += 1

# ● Fă același lucru cu un for each.
for masina in list(masini):
    print('Masina mea preferata este: {masina}')

print(f'---------------------------------------------')
# ● Fă același lucru cu un while.
x = 0
while x <= len(masini)-1:
    print(f'Masina mea preferata este: {masini[x]}')
    x += 1

# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
for i in range(len(masini)):
    if masini[i] == 'Audi' :
        print(masini[i])
    elif masini [i] == 'Opel':
        print(masini[i])
    else :
        print(masini[i].upper())

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
for masina in masini:
    if masina == 'Mercedes' :
        print(f'Am gasit masina {masina} dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# - Printează S-ar putea să vă placă mașina x.
for masina in masini:
    if masina == "Trabant" or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
masini_vechi = []
for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        print('Modele vechi:', masini_vechi)

# 6. Având dict:
pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de pana in {buget} euro puteti alege masina: {masina}')

# 7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
s = 0
for i in range(len(numere)) :
    if numere[i] == 3 :
        s += 1
print(f'Cifra 3 apare de {s} ori')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
suma = 0
for i in range(len(numere)) :
    suma = suma + numere[i]
print(f'Suma numerelor este {suma}')

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_max = numere[0]
for numar in numere:
    if numar > nr_max:
        nr_max = numar
print(f'Cel mai mare numar din lista este: {nr_max}')


# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
for i in range(len(numere)) :
    if numere[i] > 0 :
        numere[i] = numere[i]-2*numere[i]
print(f'Dupa modificarea numerelor din pozitiv in negativ vom avea {numere}')

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4


# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!

import random

numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_secret is None :
    numar = int(input('Introdu un numar: '))
    if numar > numar_secret:
        print('Nr secret e mai mic')
    elif numar < numar_secret:
        print('Nr secret e mai mare')
    else:
        print('Felicitări! Ai ghicit!')
        break

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333
# x = int(input('introdu un numar: '))
# for i in range(x) :
 #    print(range(x))

rows = int(input('Introdu un numar: '))
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
        print('')

# 5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(tastatura_telefon[i], end=' ')