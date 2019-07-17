# jako prace domową - przejrzyj zadania - examples z folderu Trainings - przykłady nie zaczynaja sie od numeru
# oraz rozwiaz zadania z folderu Trainings (pliki zaczynajace sie od numerow)

# oraz:

# 1 stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
# może być słownik miejskiego slangu ;)
words_dict = {}
# words_dict["kasiora"] = "pieniadze"
# words_dict["rozkminiac"] = "Zastanawiac"
# words_dict["obcinac"] = "Przygladac sie"
# words_dict["kimac"] = "Spac"
# words_dict["poginac"] = "chodzic"
# words_dict["klimat"] = "Atmosfera"
# words_dict["Piora "] = "włosy"
# words_dict["szama"] = "jedzenie"
# words_dict["styka"] = "dosyc"
# words_dict["kiermana"] = "Kieszen"
# words_dict["kitrac"] = "Chowac"
# words_dict["sikor "] = "zegarek"
# words_dict["sztama"] = "Zgoda"
# words_dict["balet"] = "impreza"
words_dict["elo"] = "czesc"
words_dict["hajs"] = "pieniadze"
words_dict["sikor"] = "zegarek"
words_dict["kimac"] = "spac"
print(words_dict)

# 2 zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# np kasiora - Opis slowa kasiora, w nowej linii nastepna para


with open("miejski_slang.txt", "w+") as plik:
    print(plik.tell())
    for key, value in words_dict.items():
        plik.write(f"{key} {value}\n")
    plik.seek(0)
    print(plik.read())


# 3 zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example

with open("miejski_slang_CSV.csv", "w+") as plik:
    print(plik.tell())
    for key, value in words_dict.items():
        plik.write(f"{key} | {value}\n")
    plik.seek(0)
    print(plik.read())

# 4 zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# odczytaj plik i sprawdz czy poprawnie zapisano dane

import pickle

with open("pickle_1.pickle", "wb") as plik:
    pickle.dump(words_dict, plik)

with open("pickle_1.pickle", "rb") as plik:
    wczytywanie_dict = pickle.load(plik)
print(f"Pickle = {wczytywanie_dict}")

# 5 odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# (powiedz uzytkownikowi ile razy wystepuje)

artykul = article.txt

# 6 utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# na poczatku programu zaladuj slownik z pliku pickle
# (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany