'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
for marca in mașini:
    print(marca)

for marca in mașini:
    print(f'Mașina mea preferată este {marca} ')

marca = len(mașini)
i = 0
while i < marca:
    print(f'Mașina mea preferată este {mașini[i]}')
    i += 1

'''
2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
''''''
masini = ['Audi', 'Volvo', 'BMW','Mercedes','Aston Martin','Lăstun',
'Fiat', 'Trabant', 'Opel']
for marca in range(1,len(masini)-1):
    masinaUPP = masini[marca].upper()
    masini[marca] = masinaUPP
else:
    print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
masini = ['Audi', 'Volvo', 'BMW','Mercedes','Aston Martin','Lăstun','Fiat', 'Trabant', 'Opel']

for marca in masini:
    if marca == 'Mercedes':
        print(f'am găsit mașina {marca} dorită de dvs.')
        break
    else:
        print(f'Am găsit mașina {marca}. Mai căutam.' )

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''
masini = ['Audi', 'Volvo', 'BMW','Mercedes','Aston Martin','Lăstun','Fiat', 'Trabant', 'Opel']
for marca in masini:
    if marca == 'Lăstun' or marca =='Trabant':
        continue
    print(f'S-ar putea să vă placă mașina {marca}.')

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.
'''
masini = ['Audi', 'Volvo', 'BMW','Mercedes','Aston Martin','Lăstun','Fiat', 'Trabant', 'Opel']
masini_vechi = []
for marca in masini:
    if marca == 'Lăstun' or marca =='Trabant':
        masini_vechi.append(marca)

for marca in range(len(masini)):
    if masini[marca] == 'Lăstun'or masini[marca] == 'Trabant':
        masini[marca] = 'Tesla'

for marca in masini_vechi:
    print(f'Modele vechi: {marca} ')

for marca in masini:
    print(f'Modele noi: {marca}')

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
}
'''
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
for masina,pret in pret_masini.items():
    if pret >=15000:
        break
    print(masina)

for masina,pret in pret_masini.items():
    print(masina,pret)

for masina,pret in pret_masini.items():
    if pret >=15000:
        break
    print(f' Pentru un buget de sub 15000 euro puteți alege mașină {masina}')

for masina in pret_masini:
    print(masina)
'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr = 0

for numar in numere:
    print(numar)

for numar in numere:
    if numar == 3:
        nr += 1
print(f'Numarul 3 apare de:  {nr}')


'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    print(numar)
suma = 0
for numar in numere:
    suma += numar
print(suma)

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    print(numar)
numar_mare = numere[0]
for number in numere:
    if number > numar_mare:
        numar_mare = number
print(numar_mare)

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    print(numar)
numere = [-abs(number) for number in numere]
print(numere)