# from sys import argv
#
# program_name, first_arg, second_arg = argv
#
# print(f"Pierwszy argument: {first_arg}, drugi argument: {second_arg}")


# 2. Napisz funkcję, powtarzającą słowo x razy (2 parametry - slowo oraz ile razy powtorzyc)
# (bedzie potrzebna petla for in oraz klasa range)

# first_arg = input("Kierowniku, zapodaj słówko: ")
# second_arg = input("Kieronikuuuu, a ile razy powtórzyć? Wpisz liczbę: ")

# def powtorka(text, liczba):
#     for x in range(0, int(liczba)):
#         print(text)
#
# powtorka(first_arg, second_arg)

# 3. Napisz funkcje, ktora rozbije zdanie na slowa i kazde z nich wypisze w nowej linii (bedzie potrzebna petla for in)
# def split_sentence_to_words(sentence):
#    words = str(first_arg).split(" ")
#    for word in words:
#        print(word)
#
# split_sentence_to_words(first_arg)
# 4. Napisz funkcję, która przyjmuje dowolną ilość parametrów - zaloz ze beda podawane liczbowe, funkcja ma wypisywac
# te parametry, uzywajac petli for in

# def arg_liczbowe(*args):
#     for arg in args:
#         print(arg)
#
# arg_liczbowe(23424,4564,456,456,45645,645,645,645,6,456,45,645,6,45,645,64)

#moja funkcja z geeksforgeeks
# laist1, laist2 = [x**2 for x in list(range(10,20))],[y**2 for y in list(range(60,70))]
# laist3 = [x**2 for x in list(range(20,30))]
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         for x in value:
#             print("%s == %s" % (key, x))
#
# myFun(first=laist1, mid=laist2, last=laist3)

# 5. Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funckji

# def arg_liczbowe(*args):
#     suma = 0
#     for arg in args:
#         suma = suma + arg
#     print(f'ODP: Suma argumentów funkcji wynosi: {suma}')
#
# arg_liczbowe(23424,4564,456,456,45645,645,645,645,6,456,45,645,6,45,645,64)

# 6. Inside - out - napisz dwie funckje - dodawanie (np o nazwie add) oraz mnozenie dwoch liczb (np o nazwie multiply), nastapnie wywolaj operację
# multiply(add(2, 6), 2)

# def add(first_number, second_number):
#    """
#    This is how we document our code
#    :param first_number:
#    :param second_number:
#    :return: sum of the params
#    """
#    return first_number + second_number
#
# def multiply(first_number, second_number):
#     return first_number * second_number
#
# print(f'Wynik funkcji multiply wynosi: {multiply(add(2, 6), 2)}')


# 7. Napisz funkcję rozbijajaca zdanie na slowa (ma zwracac liste ze slowami) oraz funkcje sortujaca liste slow,
# nastepnie wywolaj sortowanie na slowach podanego przez uzytkownika zdania

# lista_zdanie = []
#
# def rozb_zdanie(sentence):
#     words = str(first_arg).split(" ")
#     for word in words:
#         print(word)
#         lista_zdanie.append(word)
#         lista_zdanie.sort()
#     print(f'Zdanie 7. Odp: Zrobiłem w jednej funkcji, wyszło szybciej, a oto wynik: {lista_zdanie}')
#
# rozb_zdanie(first_arg)


# 8 Zaimportuj modul (plik) i uzyj funkcji z tego modulu
#  help(nazwa_pliku) - zadokumentuj troche kodu!


from modul import multiply as mm
from modul import add
help(mm)
help(add)
opracja = mm(5,6)
print(opracja)

# import os
# from sys import argv
#
# program_name, first_arg, second_arg = argv

# reader = open('modul.py', 'r')
# filename = __name__
# filepath = __file__
# full_path = os.getcwd()
# try:
#     reader.write(f'{filename}\n {filepath}\n {full_path}')
# finally:
#     reader.close()
#
# imie_słuchacza = input('Podaj imie: ')
#
# with open('modul.py', 'r') as a_reader:
#     a_reader.read()