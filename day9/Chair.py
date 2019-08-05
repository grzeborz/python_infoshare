#Definicja klasy
class Krzeslo(object):

    #konstruktor klasy, dzięki któremu możemy utworzyć obiekt o odpowiednich atrybutach
    #jest to metoda double under score która wykonuje się automatycznie podczas wywołania konstrukcji: NazwaKlasy()
    def __init__(self, nazwa='Wing', ilosc_nog=4, material='sklejka', kolor='jasny', cena_netto=20, marza=10):
        self.ilosc_nog = ilosc_nog
        self.ilosc_podlokietnikow = 0
        self.oparcie = True
        self.wymiary = (80,40,40)
        self.producent = 'Bodzio'

        self.nazwa = nazwa
        self.material = material
        self.kolor = kolor
        self.cena_netto = cena_netto

        self.marza = marza

        self.cena_do_sprzedazy = None

    #metoda obiektu do pobierania informajcji na podstawie atrybutóœ
    def cena_sprzedazy(self):
        self.cena_do_sprzedazy = self.cena_netto * (1 + self.marza/100)

        return self.cena_do_sprzedazy

    def cena_brutto(self):
        return self.cena_sprzedazy() * 1.23

    def cena_brutto_euro(self):
        return self.cena_sprzedazy() * 4.30

    #przeciążanie znaku <
    def __lt__(self, other):
        if self.ilosc_nog < other.ilosc_nog:
            print("{} jest bardziej stabilny".format(other.nazwa))
        #ciało funkcji

    #definicja metody która będzie wykonana gdy na obiekcie użyjemy metody len()
    def __len__(self):
        return self.ilosc_nog

    #definicja metody która będzie wykonana gdy na obiekcie użyjemy metody len()
    def __add__(self, other):
        return self.ilosc_nog + other.ilosc_nog

    # definicja metody która będzie wykonana gdy na obiekcie użyjemy metody print()
    def __str__(self):
        return "jestem {} i mam {} nog".format(self.nazwa, self.ilosc_nog)

    def wyswietl(self, lang='pl'):
        if (lang == 'en'):
            return "I'm {} and I have {} legs".format(self.nazwa, self.ilosc_nog)
        elif (lang == 'pl'):
            return "Jestem {} i mam {} nog".format(self.nazwa, self.ilosc_nog)
        else:
            print('WARNNIG: Language "{}" not suported :)'. format(lang))
            return "Jestem {} i mam {} nog".format(self.nazwa, self.ilosc_nog)



#tworzenie obiektów (w tym momencie wywołuje się metoda __init__())
obiekt_1 = Krzeslo("Wing", 4)
#odpowiednik (którego nie używamy :)) wywołania
#obiekt_1 = Krzeslo.__init__("Wing", 4)

obiekt_2 = Krzeslo("Better Wing", 8)

print("{:*^80}".format(" Atrybuty i metody "))

#pobieranie atrybutu obiektu
print(obiekt_2.cena_do_sprzedazy)
#wywałonie metody obiektu
obiekt_2.cena_sprzedazy()
print(obiekt_2.cena_do_sprzedazy)

print("{:*^80}".format(" Przeciążanie metod "))

obiekt_1 < obiekt_2
## Better Wing jest bardziej stabilny

#dodawanie (magiczne wywołanie metody __add__())
print(obiekt_1 + obiekt_2)

#lub
print(obiekt_1.__add__(obiekt_2))

print("{:*^80}".format(" Sposoby na tekstową reprezentację obiektów "))

print(obiekt_2)
print("jestem {} i mam {} nog".format(obiekt_2.nazwa, obiekt_2.ilosc_nog)) #najmniej poprawny :)
print("-" * 40)
print(obiekt_2.wyswietl('pl')) #definiowane różnych metod jest okej gdy potrzebujemy różnych form wyświetlenia, albo parametryzacji
print(obiekt_2.wyswietl('en'))
print(obiekt_2.wyswietl('es'))

print("{:*^80}".format(" Metoda len() i __len__() "))

print(len(obiekt_1))
print(len("AAAAAA")) #string to też obiekt i też ma swoją definicję metody __len__()