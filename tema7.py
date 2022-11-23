'''
 ABSTRACTION
 Clasa abstractă FormaGeometrica
 Conține un field PI=3.14
 Conține o metodă abstractă aria (opțional)
 Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
 probabil am colturi’

 INHERITANCE
 Clasa Pătrat - moștenește FormaGeometrica
 constructor pentru latură

 ENCAPSULATION
 latura este proprietate privată
 Implementează getter, setter, deleter pentru latură
 Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
 implementezi metoda abstractă aria)

 Clasa Cerc - moștenește FormaGeometrica
 constructor pentru rază
 raza este proprietate privată
 Implementează getter, setter, deleter pentru rază
 Implementează metoda cerută de interfață - în calcul folosește field PI
 mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
 abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''
class FormaGeometrica():
    PI = 3.14

    def arie(self):
        raise NotImplementedError
    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):
       def __int__(self,latura):
           self.__latura=latura
       def latura(self):
           return self.__latura
       def get_latura(self):
           print((f'Latura are {self.__latura}'))
           return self.__latura
       def set_latura(self):
           print(f'Noua latura este {self.latura}')
           self.__latura = latura_noua
       def latura(self):
           print(f'Am sters latura')
           self.__latura = None
           self.__latura = latura
       def __init__(self,latura):
           self.latura=latura
       def arie(self):
            return self.latura* self.latura



patrat1 = Patrat(4)
print(patrat1.arie())
print(patrat1.descrie())
patrat2 = patrat1
patrat2.latura = 8
print(patrat2.arie())
del patrat2.latura

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.raza=raza
    def raza(self):
        return self.__raza
    def raza(self):
        print(f'Raza este {self.__raza}')
        return self.__raza
    def raza(self,raza):
        print(f'Noua raza este {raza}')
        self.__raza = raza
    def raza(self):
        print(f'Am sters raza')
        self.__raza = None
    def arie(self):
      return self.raza * self.raza * self.PI


cerc1 = Cerc(10)
print(cerc1.arie())
cerc2 = cerc1
cerc2.raza = 14
print(cerc2.arie())
del cerc2.raza




class Patrat_nou:
    def __init__(self,lungime_latura):
        self.lungime_latura = lungime_latura
    def perimetru(self):
        return 4 * (self.lungime_latura)
    def aria(self):
        return self.lungime_latura * self.lungime_latura
    def descrie(self):
        return('Eu nu am colturi')

patrat_nou1 = Patrat_nou(7)
print(patrat_nou1.perimetru())
print(patrat_nou1.aria())
print(patrat_nou1.descrie())


class Cerc_nou:
    def __init__(self,raza):
        self.raza = raza
    def perimetru(self):
        return 2 * 3.14 * self.raza
    def aria(self):
        return 3.14 * self.raza * self.raza



cerc_nou1 = Cerc_nou(12)
print(cerc_nou1.perimetru())
print(cerc_nou1.aria())

