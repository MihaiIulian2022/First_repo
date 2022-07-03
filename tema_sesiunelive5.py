# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Funcție care să calculeze și să returneze suma a două numere
def suma_numere():
    a = int(input('introdu valorea numarului a: '))
    b = int(input('introdu valorea numarului b: '))
    su = a + b
    print(f'Suma numerelor este: {su}')
suma_numere()

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def tip_numar():
    x = int(input('Introdu un numar: '))
    if x % 2 == 0:
        print('TRUE')
    else :
        print('FALSE')
tip_numar()

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
def total_caractere():
      nume_complet = 'Lacriceanu Mihai Iulian'
      count = 0
      for i in range(len(nume_complet)):
          count = count + 1
      print(f'Numarul total de caractere din numele meu este: {count}')
total_caractere()

# 4. Funcție care returnează aria dreptunghiului
def aria_dreptunghi():
    l = int(input('Introdu latimea: '))
    L = int(input('Introdu lungimea: '))
    aria = l * L
    print(f'Aria dreptunghiului este: {aria}')
aria_dreptunghi()

# 5. Funcție care returnează aria cercului
def aria_cercului():
    pi = 3.14
    raza = int(input('introdu valoarea razei cercului: '))
    aria = pi * raza * raza
    print(f'aria cercului este: {aria}')
aria_cercului()

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
def cauta_caracter():
    string_test = 'Functiile sunt greu de invatat!'
    for litera in string_test:
         if litera == 'l':
             print('True')
         else :
             print('False')
cauta_caracter()

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
def string1(nume):
    contor_mic = 0
    contor_mare = 0
    for c in nume:
        if c.isupper() == True:
            contor_mare += 1
        elif c.islower() == True:
            contor_mic += 1
    print(f'nr de caractere upper este: {contor_mare}')
    print(f'nr de caractere lower este: {contor_mic}')

string2 = 'Ana aRe Mere si perE'
string1(string2)

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
# asta de mai jos nu merge, nu stiu ce sa i fac
def returnare_pozitiva(lista):
    lista_goala = []
    for numar in lista:
        if numar > 0:
            lista_goala.append(numar)
    return lista_goala

lista = [1, -2, 3, 8, 0, -5, 4, 7, -5]
print(returnare_pozitiva(lista))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.
def compara_numere():
    x = input('Introdu primul numar: ')
    y = input('Introdu al doilea numar: ')
    if x > y :
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
    elif x < y :
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else :
        print('Numerele sunt egale')
compara_numere()

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
def functie_set(un_numar, un_set):
    ok = False
    for i in un_set:
        if i == un_numar:
            ok = True
    if ok == True:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
    print('am adaugat numărul nou în set')
    return True

set_de_numere = {1, 2, 3, 4, 5, 6, 7}
nr_de_adaugat = 9
print(functie_set(nr_de_adaugat,set_de_numere))

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
#luni = {'Ianuarie': 31, 'Februarie': 28, 29 , 'Martie': 31, 'Aprilie': 30, 'Mai': 31, 'Iunie': 30, 'Iulie' : 31, 'August' : 31, 'Septembrie': 30,
#'Octombrie': 31, 'Noiembrie': 30, 'Decembrie':31}
#def luni_an():

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    print("Suma: ", a)
    print("Diferenta: ", b)
    print("Inmultirea: ", c)
    print("Impartirea: ", d)
calculator(5,7)
calculator(10,2)

# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def comparare(nr1, nr2, nr3):
    if nr1 > nr2 and nr1 > nr3:
        print(f'valoarea maxima este {nr1}')
    elif nr2 > nr1 and nr2 > nr3:
        print(f'valoarea maxima este {nr2}')
    else :
        print(f'valoarea maxima este {nr3}')
comparare(8, 5, 6)

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

# Exerciții Opționale - Bonus
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.
# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :