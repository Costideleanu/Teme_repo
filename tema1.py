'''
Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''
# O variabila este o valoare ce va fi pastrata in memoria calculatorului
'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''
produs = 'calculator'
numar_bucati = 200
pret_bucata = 4599.90
promotie = True
'''
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
print(type(produs))
print(type(numar_bucati))
print(type(pret_bucata))
print(type(promotie))

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
pret_bucata = round(pret_bucata)
print(type(pret_bucata))

'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.

Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print(f'Am vrut sa cumpar un {produs}')
print(f'Am cumparat {numar_bucati} de calculatoare.')
print(f'Am platit {pret_bucata} pentru fiecare calculator.')
print(f'A fost la promotie? {promotie}')

'''
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''

nume = input('Introdu Numele: ')
prenume = input('Introdu Prenumele: ')
print(f'Numele complet are {len(nume + prenume)} caractere')

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.

'''
lungime = input('Lungimea dreptunghiului = ')
latime = input('Latimea dreptunghiului = ')
lungime = int(lungime)
latime = int(latime)
print(f'Aria dreptunghiului este {lungime * latime}')

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':

- afișează de câte ori apare cuvântul 'the';

'''
propozitie = 'Coral is either the stupidest animal or the smartest rock'
rezultat = propozitie.count(' the ')
'''
9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
'''
propozitie = 'Coral is either the stupidest animal or the smartest rock'
rezultat = propozitie.count(' the ')
print(rezultat)

'''
10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
'''

assert propozitie == str(propozitie)
print('Afiseaza daca contine doar litere')
assert propozitie == int(propozitie)
print('Propozitia nu contine doar litere.')