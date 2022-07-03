# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu .
# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
# else.
# if si else este o modalitate prin care in urma verificarii unei conditii, instruim programul sa execute un anumit set
# de instructiuni, daca conditia este adevarata se executa un set de instructiuni iar daca este falsa se executa un alt
# set de instructiuni

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = int(input('Introdu un numar natural: '))
if x >= 0 :
    print('Este un numar natural')
else :
    print('Nu este un numar natural')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x > 0 :
    print('Este un numar pozitiv')
elif x < 0 :
    print('Este un numar negativ')
else : print('Este un numar netru')

# 4. Verifică și afișează dacă x este între -2 și 13.
if x > -2 and x < 13 :
    print('numarul introdus este in intervalul cautat')
else :
    print('numarul introdus nu este in intervalul cautat')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5
y = int(input('Introdu un numar y: '))
if x - y < 5 :
    print('Diferenta dintre x si y este mai mica de 5')
else :
    print('Diferenta dintre x si y nu este mai mica de 5')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not(x > 5 and x < 27) :
    print('x nu este in intervalul 5-27')
else :
    print('x este in intervalul 5-27')

# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.
if x == y :
    print('x si y sunt egale')
elif x > y :
    print('x este mai mare ca y')
else :
    print('x este mai mic ca y')

# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# o sa pun x1, y1, z1 ca si laturi
x1 = int(input('introdu valoare lui x1: '))
y1 = int(input('introdu valoare lui y1: '))
z1 = int(input('introdu valoare lui z1: '))
if x1 == y1 == z1 and x1 != 0 :
    print('triunghiul este echilateral')
elif (x1 == y1 or y1 == z1 or x1 == z1) and x1 != 0 :
    print('triunghiul este isoscel')
else :
    print('triunghiul este oarecare')

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu.
litera = input('introdu o litera: ')
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u' or litera == 'ă' or litera == 'î' or litera == 'â' :
    print('litera introdusa este vocala')
else :
    print('litera introdusa nu este vocala')

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = int(input('introdu nota: '))
if nota > 9 and nota <= 10 :
    print('nota elevului este A')
elif nota <= 9 and nota > 8 :
    print('nota elevului este B')
elif nota <= 8 and nota > 7 :
    print('nota elevului este C')
elif nota <= 7 and nota > 6:
    print('nota elevului este D')
elif nota <= 6 and nota > 4:
    print('nota elevului este E')
elif nota <= 4 :
    print('nota elevului este F')
else :
    print('nota elevului este incorect introdusa')

# Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.
# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
numar = int(input('introdu un numar: '))
count = 0
if (numar == 0):
    count = count + 1
else:
    while (numar):
        count = count + 1
        numar = numar // 10
if (count >= 4):
    print(f'Numarul are minim 4 cifre')
else:
    print(f'Numarul nu are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre.

# 3.Verifică dacă x este număr par sau impar (x e int).
x_ex3 = int(input('introdu un numar intreg: '))
if x_ex3 % 2 == 0 :
    print('numarul intreg introdus este par')
else :
    print('numarul intreg introdus este impar')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
# o sa pun x2, y2, z2
x2 = int(input('Introdu un nr intreg x2: '))
y2 = int(input('Introdu un nr intreg y2: '))
z2 = int(input('Introdu un nr intreg z2: '))
if x2 > y2 and x2 > z2 :
    print('x2 este cel mai mare numar')
elif y2 > x2 and y2 > z2 :
    print('y2 este cel mai mare numar')
else :
    print('z2 este cel mai mare numar')

# 5.
# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
x_ex5 = int(input('introduce unghiul: '))
y_ex5 = int(input('introduce unghiul: '))
z_ex5 = int(input('introduce unghiul: '))
if (x_ex5 > 0 and x_ex5 < 180) and (y_ex5 > 0 and y_ex5 < 180) and (z_ex5 > 0 and z_ex5 < 180) and (x_ex5 + y_ex5 + z_ex5 == 180) :
    print('triunghiul este valid')
else :
    print('triunghiul nu este valid')

# Exerciții Bonus (may need google) .
# 1.Verificare îmbarcare persoane
# Ține minte următoarele date:
# - Vârstă;
# - Însoțit de mama;
# - Însoțit de tata;
# - Pașaport;
# - Act permisiune mama;
# - Act permisiune tata.

# Condiții de îmbarcare
# - Dacă pers are vârstă peste 18 ani și are pașaport.
# - Dacă pers are sub 18 ani, are pașaport și e însoțită de ambii părinți.
# - Dacă pers are sub 18 ani, are pașaport, e însoțită de cel puțin un părinte
# și are permisiune în scris de la celalat părinte.
# ● Aici vreau să testezi codul cu toate variantele posibile.
# ● Să generezi cazuri de test și expected result, apoi să rulezi codul și să
# completezi actual results.

# Ex:
# Vârstă 19 ani, nu am pașaport => Nu mă pot îmbarca.
# Vârstă 17 ani, am pașaport, ambii părinți => Mă pot îmbarca.
# Etc
varsta = int(input('Introdu varsta persoanei: '))
insotit_de_mama = input('insotit de mama? d/n')
insotit_de_tata = input('insotit de tata? d/n')
pasaport = input('are pasaport? d/n')
act_permisiune_mama = input('are permisiune de la mama? d/n')
act_permisiune_tata = input('are permisiune de la tata? d/n')
if varsta >= 18 and pasaport == 'd' :
    print('te poti imbarca')
elif varsta < 18 and pasaport == 'd' and insotit_de_mama == 'd' and insotit_de_tata == 'd' :
    print('te poti imbarca')
elif varsta < 18 and pasaport == 'd' and ((insotit_de_mama == 'd' and act_permisiune_tata == 'd') or (act_permisiune_mama and insotit_de_tata)) :
    print('te poti imbarca')
else :
    print('nu te poti imbarca')

# orice varsta mai mare sau egala cu 18 ani, are pasaport => se poate imbarca
# orice varsta mai mare sau egala cu 18 ani, nu are pasaport => nu se poate imbarca
# sub 18 ani, nu are pasaport => nu se poate imbarca
# sub 18 ani, are pasaport => nu se poate imbarca
# sub 18 ani, are pasaport, e insotit de ambii parinti => se poate imbarca
# sub 18 ani, are pasaport, e fara parinti => nu se poate imbarca
# sub 18 ani, are pasaport, e insotit doar de mama => nu se poate imbarca
# sub 18 ani, are pasaport, e insotit doar de tata => nu se poate imbarca
# sub 18 ani, are pasaport, e insotit doar de mama, are permisiune de la tata => se poate imbarca
# sub 18 ani, are pasaport, e insotit doar de mama, nu are permisiune de la tata => nu se poate imbarca
# sub 18 ani, are pasaport, e insotit doar de tata, are permisiune de la mama => se poate imbarca
# sub 18 ani, are pasaport, e insotit doar de ta, nu are permisiune de la mama => nu se poate imbarca


# 2. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random.
# Ne imaginam că dăm cu zarul și salvăm acest număr în dice_roll.
# Ia un număr ghicit de la utilizator.
# Verifică și afișază dacă utilizatorul a ghicit 3 opțiuni:
# - Ai pierdut. Ai ales un număr mai mic. Ai ales x dar a fost y.
# - Ai pierdut. Ai ales un număr mai mare. Ai ales x dar a fost y.
# - Ai ghicit. Felicitări? Ai ales x și zarul a fost y.
import random
sequence=(1, 2, 3, 4, 5, 6)
random.choice(sequence)
nr_ales = int(input('introdu un numar de pe zar adica intre 1 si 6: '))
if random.choice(sequence) == nr_ales :
    print(f'Felicitari! Ai ales {nr_ales} si zarul a fost {random.choice(sequence)}')
elif random.choice(sequence) > nr_ales :
    print(f'Ai ales un număr mai mic. Ai ales {nr_ales} dar a fost {random.choice(sequence)}.')
else :
    print(f'Ai ales un număr mai mare. Ai ales {nr_ales} dar a fost {random.choice(sequence)}')

# nu e bine la asta cu zarul, am facut niste teste si nu imi da bine
# ma dau batut, macar ma intereseaza daca e ok ideea, sa nu fiu asa demoralizat :))