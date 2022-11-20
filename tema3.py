'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face

suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.

'''
note_muzicale = ['do', 're', 'mi', 'fa', 'so', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
'''
2. De câte ori apare ‘do’?
'''
note_muzicale.count('do')
print(note_muzicale.count('do'))

'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
'''
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2 #varianta 1
print(lista3)
lista1.extend(lista2) #varianta 2
print(lista1)
'''
4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
lista3 = [3, 1, 0, 2, 6, 5, 4]
lista3.sort()
print(lista3)
lista3.pop(0)
print(lista3)

'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.

'''
lista3 = [3, 1, 0, 2, 6, 5, 4]
print(lista3)
if len(lista3) == 0:
    print('lista este goala')
else:
    print('lista nu este goala')

'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.

'''
lista3 = [3, 1, 0, 2, 6, 5, 4]
lista3.clear()
print(lista3)

'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.

'''

print(lista1)
if len(lista3) == 0:
    print('lista este goala')
else:
    print('lista nu este goala')

'''
8. Având dicționarul 
Folosește o funcție că să afișezi Elevii (cheile)
'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
elevi = dict1.keys()
print(elevi)
'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print('Ana a luat nota' ,dict1.get('Ana'))
print('Gigel a luat nota' ,dict1.get('Gigel'))
print('Dorel a luat nota' ,dict1.get('Dorel'))

'''
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Gigel'] = 6
print('Gigel a luat nota' ,dict1.get('Gigel'))

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
dict1.pop('Gigel')
print(dict1)
dict1.update({'Ionica' : 9})
print(dict1)

'''
12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if 'luni' in weekend:
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

'''
14. Afișează diferențele dintre aceste 2 seturi.
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
dif = zile_sapt.difference(weekend)
print(dif)

'''
15. Afișază intersecția elementelor din aceste 2 seturi.
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

inter = zile_sapt.intersection(weekend)
print(inter)
