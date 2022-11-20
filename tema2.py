'''
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.
 - If else e o declarație condițională care execută un bloc de cod când o anumită condiție a fost îndeplinită.
'''
'''
2. Verifică și afișează dacă x este număr natural sau nu.
'''
x = int(input('x = '))
if x >= 0:
    print(f'{x} este numar natural')
else:
    print(f'{x} nu este numar natural')

'''
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''
if x == 0:
    print(f'{x} este numar neutru.')
elif x > 0:
    print(f'{x} este numar pozitiv.')
else:
    print(f'{x} este numar negativ')
'''
4. Verifică și afișează dacă x este între -2 și 13.
'''
if x >= -2 and x <= 13:
    print('numarul se incadreaza intre -2 si 13')
else:
    print('numarul nu se incadreza intre -2 si 13')
'''
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''
y = int(input('y = '))
z = x - y
print(z)
if z < 5:
    print('true')
else:
    print('false')

'''
6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''

if x >= 5 and not x >= 27:
    print('numarul este cuprins')
else:
    print('numarul nu este cuprins')

'''
7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''
x = int(input('x = '))
y = int(input('y = '))
if x == y:
    print('sunt egale')
elif x > y:
    print(f'{x} este mai mare')
else:
    print(f'{y} este mai mare')

'''
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x == y and y == z:
    print('triunghiul este isoscel')
elif x == y and not y == z:
    print('triunghiul este echilateral')
elif x == z and not y == z:
    print('triunghiul este echilateral')
elif y == z and not x == z:
    print('triunghiul este echilateral')
else:
    print('triunghiul este oarecare')


'''
9. Citește o literă de la tastatură.

Verifică și afișează dacă este vocală sau nu
'''

litera = str(input('introdu litera '))
if litera in ('a', 'e', 'i', 'o', 'u',):
    print(f'{litera} este vocala')
else:
    print(f'{litera} este consoana')

'''
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
nota = float(input('introdu nota'))
if nota > 9:
    print('A')
elif nota > 8:
    print('B')
elif nota > 7:
    print('C')
elif nota > 6:
    print('D')
elif nota > 4:
    print('E')
else:
    print('F')
