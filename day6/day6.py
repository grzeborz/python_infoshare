# elementy = { 1:"ola", 0:"ala",  2:"ela" }
#
# # print(elementy)
# # print(elementy[1])
#
# slownik = {"imie": "Adam", "nazwisko":"kowalski", "wiek":32}
#
# # klucze
# print(slownik.keys())
# # wartości
# print(slownik.values())
#
# # items() zwraca parę - klucz oraz wartość
# for klucz, wartosc in slownik.items():
#     print(f"Klucz: {klucz} ma wartość {wartosc}")
#
# if "adres" in slownik.keys():
#     print("Adres dostępny")
# else:
#     print("adres niedostępny")
#
# print(slownik)
# # jeśli przypiszemy wartość do nieistniejącego klucza
# # to zostanie on utworzony
# slownik["adres"] = "Gdańsk"
# print(slownik)
# # jeśli przypisujemy wartość do istniejącego klucza
# # to zmieniamy/nadpisujemy jego wartość
# slownik["adres"] = "Gdynia"
# print(slownik)

# dict_of_person = []
#
# rekordy = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
# {"imie": "Anna", "nazwisko":"nowak", "wiek":23},
# {"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
# {"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]
#
#
# for indeks, rekord in enumerate(rekordy):
#     print(f"Pod indeksem{indeks} a pod rekoredem :  {rekord}")
#


# movie_db = {}
#
# movie_db[2000] = ["Animatrix", "Transformers 1"]
# movie_db[2009] = ["Transformers 3"]
# movie_db[2010] = ["asasas","jrifrjpjfrp"]
# movie_db[2000].append("Matrix")
#
# for key, value in movie_db.items():
#    print(f"W roku {key} wyprodukowano \nnastępująco:")
#    for movie in value:
#        print(f"\t\t{movie}")


# print(movie_db[2000])

# print(f"{}, a film to: {movie_db.values()}")

#stwórz listę

list_of_movies = ["Obcy", "Predator", "Danow temu w trawie"]

#otwórz i zapisz do pliku filmy kazdy w nowym wierszu(linijce pliku

sciezka = "list_filmow.txt"

#standardowo
# with open("list_filmow.txt", "w+") as plik:
#     print(plik.tell())
#     for movie in list_of_movies:
#         plik.write(movie+ "\n")
#     plik.seek(0)
#     print(plik.read())

# #metoda writelines
# with open("list_filmow.txt", "w+") as plik:
#     print(plik.tell())
#     plik.writelines(list_of_movies + '\n')
#     plik.seek(0)
#     print(plik.read())


#filmy do pliku ze słownika

# movie_db = {}
#
# movie_db[2000] = ["Animatrix", "Transformers 1"]
# movie_db[2009] = ["Transformers 3"]
# movie_db[2010] = ["asasas","jrifrjpjfrp"]
# movie_db[2000].append("Matrix")
# #movie_db[2001].append("Matrix")
#
#
#
# with open("list_filmow.txt", "w+") as plik:
#     print(plik.tell())
#     for key, value in movie_db.items():
#         plik.write(f"W roku {key} wyprodukowano \nnastepujaco:")
#         for movie in value:
#             plik.write(f"\n\t\t{movie}\n")
#     plik.seek(0)
#     print(plik.read())


# dictionaries plus lists
# napisz program odczytujacy plik - policz ilosc wystepujacych poszczegolnych slow
# Wskazowki:
# default dict values
from collections import defaultdict
# set(
# list_dictionary = defaultdict(list)

# wypisz 10 najczęsciej i 10 najrzadziej wystepujacych slow




simple_dict = {1: "jeden", 2: "dwa"}

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartosc: {value}")

simple_dict[1] = "trzy"

for key, value in simple_dict.items():
    print(f"pod kluczem {key} jest wartosc: {value}")

    with open(tekst, "r") as plik:
        # print(plik.readlines(), end="")
        tekst_lista = plik.readlines()
        print(tekst_lista)
        tekst_splitted = []
        for word in tekst_lista:
            word = ''.join(x for x in word if x not in '()",\n?.')
            slowka = word.split()
            for slowo in slowka:
                tekst_splitted.append(slowo)
            dict_words = {}
            for word in tekst_splitted:
                if word in dict_words:
                    dict_words[word] += 1
                else:
                    dict_words[word] = 1
        print(dict_words)
