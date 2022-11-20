'''
1.Funcție care să calculeze și să returneze suma a două numere
'''
a = int(input('a = '))
b = int(input('b = '))
def suma(a, b):
     print(a+b)

suma(a,b)

'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''
#
def numar(valoare =int(input('Numarul este:'))):
    if valoare %2==0:
        return True
    else:
        return False
rezultat = numar()
print(rezultat)

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
def numar_caractere(nume, prenume, nume_mijlociu):
    caractere = len(nume + prenume + nume_mijlociu)
    return caractere

caractere = numar_caractere('Deleanu','Constantin','Costi')
print(caractere)


'''
4. Funcție care returnează aria dreptunghiului
'''
def aria_dreptungi(lungime,latime):
    arie = lungime * latime
    return arie
arie = aria_dreptungi(7,5)
print(arie)

'''
5. Funcție care returnează aria cercului
'''
def aria_cercului(r):
    aria2 = 3.14 * r ** 2
    return aria2
aria2 = aria_cercului(10)
print(aria2)

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
'''
string = str(input('introdu sring:  '))
caracter = input('introdu caracter:  ')
def gaseste_caracter():
    if caracter in string:
        return True
    else:
        return False
rez = gaseste_caracter()
print(rez)

'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''
def string(a):
    d={'upper':0, 'lower':0}
    for c in a:
        if c.isupper():
           d['upper']+=1
        elif c.islower():
           d['lower']+=1
        else:
           pass

    print ('Nr de caractere upper case exte:', d['upper'])
    print ('Nr de caractere lower case este:', d['lower'])

string('Maine voi cumpara o Dacia Duster.')

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''

inputList = [-2, 8, -1, 7, 4, 6,-9]
def getPositiveElementsList(inputList):
    positiveList = []
    for element in inputList:
        if element > 0:
            positiveList.append(element)
    return positiveList
result = getPositiveElementsList(inputList)
print(result)

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
# '''
def lista_numere(x,y):
    if x >y:
        print(f'Primul numar {x} este mai mare decat al doilea lea numar {y} ')
    elif x < y:
        print((f'Al doilea numar {y} este mai mare decat primul numar {x}'))
    else:
        print('Numerele sunt egale')
x = int(input('Introduceti numar: '))
y = int(input('Introduceti numar: '))
lista_numere(x,y)

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''

def numar_set(x, set_numar):
    if x in set_numar:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        set_numar.add(x)
        print('am adaugat numărul nou în set')
        return True
x = 8
set_numar = {1,3,5,7,9}

result = numar_set(x,set_numar)
print(set_numar)
