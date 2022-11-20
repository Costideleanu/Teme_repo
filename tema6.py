'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''
class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def descrie_cerc(self):
        return (f'{self.culoare} si {self.raza}')
    def aria(self):
        return (3.14 * self.raza * self.raza)
    def diametru(self):
        return 2 * self.raza
    def circumeferinta(self):
        return (2 * 3.14 * self.raza)

cerc1 = Cerc(10, 'Albastru')
print(cerc1.descrie_cerc())
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumeferinta())

'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return (self.lungime, self.latime, self.culoare)
    def aria(self):
        return (self.lungime * self.latime)
    def perimetru(self):
        return (2 * self.lungime) + (2 * self.latime)
    def schimbă_culoarea(self, noua_culoare):
        self.culoare = noua_culoare



dreptunghi1 = Dreptunghi(12, 6, 'Negru')
print(dreptunghi1.descrie())
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
print(dreptunghi1.schimbă_culoarea('Alb'))
print(dreptunghi1.descrie())

'''
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

class Angajat:
    nume = None
    prenume = None
    salariul = None

    def __init__(self,nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return (self.nume, self.prenume, self.salariu)
    def nume_complet(self):
        return self.nume +" "+ self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu * 12
    def marire_salariu(self,procent):
        return (self.salariu / 100 * procent)


angajat_nou = Angajat('Popa','Marius',3450)
print(angajat_nou.descrie())
print(angajat_nou.nume_complet())
print(angajat_nou.salariu_lunar())
print(angajat_nou.salariu_anual())
print(angajat_nou.marire_salariu(25))

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return (f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self,suma):
        return self.sold - suma
    def creditare_cont(self, suma):
        return self.sold + suma

cont_nou = Cont('DE68500105178297336485','Georgescu Paul', 3430)
print(cont_nou.afisare_sold())
print(cont_nou.debitare_cont(650))
print(cont_nou.creditare_cont(755))