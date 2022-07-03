# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# O variabila este un spatiu din memorie in care se pot stoca date, valori


# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă
# Observație: Valorile vor fi alese de tine după preferințe.
# - string
var_string = '455'
# - int
var_int = 2022
# - float
var_float = 99.5
# - bool
var_bool = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_bool))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.

var_float = round(var_float)
print(var_float)
print(type(var_float))

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f'In anul {var_int} s au platit {var_string} lei si {var_float} lei pentru taxe')
print('Familia a reusit sa stranga ' + var_string + str(var_float) + str(var_int) + ' lei')
print(int(var_string) + var_int + int(var_float))
print(float(var_string) + float(var_int) + var_float)

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'
nume = input('Nume: ')
prenume = input('Prenume: ')
print(f'Lacriceanu Mihai are ' + str(len(nume)+len(prenume)) + ' caractere')


# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
lungime = float(input('lungime: '))   # sau int in loc de float daca folosim numere intregi
latime = float(input('latimea: '))    # idem comentariu de mai sus
print(f'Aria deptunghiului este: ' + str(lungime*latime))

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - citește de la tastatură un int x;
# - afișează stringul fără ultimele x caractere.
# ex: Dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'.
test_string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduce un numar '))
print(test_string[0:len(test_string)-x:1])

# 9. Același string:
# a. declară un string nou care să fie format din primele 5 caractere + ultimele 5;
print(test_string.index('rock'))
test_string_nou = test_string[0:6] + test_string[52:]
print(test_string_nou)

# b. afișează de câte ori apare cuvântul 'the';
print(test_string.count(' the '))

# c. înlocuiește ‘the’ cu ‘THE’ peste tot - printează rezultatul;
print(test_string.replace('the', 'THE'))

# d. salvează într-o variabilă și afișează indexul de start al cuvântului ‘rock’;
# - hint: este o funcție care te ajută să faci asta;
var = test_string.index('rock')
print(var)
# folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvânt.
# Output: 'Coral is either the stupidest animal or the smartest'
print(test_string[0:53])

# 10. Exercițiu:
# - citește de la tastatură un string;
# - verifică dacă primul și ultimul caracter sunt la fel.
# Observație: se va folosi un assert.
# Atenție: se dorește că programul să fie case insensitive - 'apA' e acceptat.
string_ex10 = input('Introdu un string de la tastatura ')
print(string_ex10[0])
print(string_ex10[len(string_ex10)-1])
assert string_ex10[0] == string_ex10[len(string_ex10)-1], 'primul caracter si ultimul nu sunt la fel '


# 11. Având stringul '0123456789':
# - Afișează doar numerele pare;
# - Afișează doar numerele impare;
# - hint: folosește slicing, controlează din pas.
pentru_procesat = '0123456789'
print(pentru_procesat[0:10:2])
print(pentru_procesat[1:10:2])

# 12. Utilizand stringul de la 9.d.
string_ex12 = 'Coral is either the stupidest animal or the smartest4'
# - folosește un assert că să verifici dacă acest string conține doar numere;
# - hint: merge cu slicing? Probabil că nu... Ce mai știi atunci legat de
# string? Poate găsești o funcție ajutătoare.

# ceva asemanator cu asta?
# assert string_ex12.isdigit(





# Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
# nevoie de Google).

# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
from math import *
exercitiu1: str = input('Introdu un string de dimensiune impara: ')
if len(exercitiu1) % 2 !=0 :
    print(exercitiu1[floor(len(exercitiu1) / 2)])
else : print('Stringul introdus este de dimensiune para ')

# 2. Folosind assert, verifică dacă un string este palindrom.
string_pentru_palindrom = input('Introdu un string pentru a verifica daca este palindrom: ')
assert string_pentru_palindrom == string_pentru_palindrom[::-1], f'Stringul {string_pentru_palindrom} nu este palindrom'

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
exercitiu3 = input('Introdu un string pentru ex3: ')
variabila1, variabila2 = exercitiu3.split()
print(variabila1)
print(variabila2)

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
exercitiu4 = input('Introdu un string: ')
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
var_ex = exercitiu4[0]
print(var_ex)
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
print(exercitiu4.upper())


# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

# am incercat ceva dar nu ii dau de cap, o sa pun in comentarii
# from getpass import getpass
# user_name = input('Introdu de la tastatura un user ')
# password = getpass('Introdu parola ')
# print(f'Parola pentru userul {user_name} este {password}')