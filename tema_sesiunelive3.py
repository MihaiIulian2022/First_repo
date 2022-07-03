# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
#
# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# Afișeaz-o:
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# 2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
# Găseste 2 variante să le unești într-o singură listă.
lista_unita = lista1 + lista2
print(lista_unita)

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
lista_unita.sort()
print(lista_unita)

# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
if len(lista_unita) != 0 :
    print('lista nu este goala')
else :
    print('lista este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista_unita.clear()
print(lista_unita)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if len(lista_unita) != 0 :
    print('lista nu este goala')
else :
    print('lista este goala')

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor
# print(dict1)
# Ex: ‘Ana a luat nota {x}’
print('Ana a luat nota: ' + str(dict1['Ana']))
print('Gigel a luat nota: ' + str(dict1['Gigel']))
print('Dorel a luat nota: ' + str(dict1['Dorel']))
# Doar nota o vei lua folosindu-te de cheie

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1['Dorel'] = 6
print(dict1.get('Dorel'))

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
dict1.pop('Gigel')
print(dict1)
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
dict1['Ionica'] = 9
# ● Printează noii elevi
print(dict1)

# 12. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
zile_sapt.add('luni')
# ● Afișeaza zile_sapt
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt) :
    print('weekend este un subset al zilelor saptamanii')
else :
    print('weekend nu este un subset al zilelor saptamanii')

# 14. Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt.difference(weekend))

# 15. Afișază intersecția elementelor din aceste 2 seturi.
print(zile_sapt.intersection(weekend))

# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
#
# ● Declară o Listă cu 5 jucători
echipa = ['Edi', 'Geo', 'Ene', 'Vali', 'Tudor']
schimbari_efectuate = 0
schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# ceva cu: if isinstance()???

# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item îs în list python”

