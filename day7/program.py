# # from day7.moj_modul import is_dir_or_file
#
# import moj_modul
# import os
#
# # print(is_dir_or_file())
# print("Program wywołujący moduł")
# print(30 * '=')
#
# print(os.listdir())
# print(30 * "=")
#
# # moj_modul.listdir()
# #lista
# # for elem in moj_modul.listdir():
# #     print(f"{elem}")
#
# #słownik:
#
#
#
#
#
#
#
# artykul = "text.txt"

# with open(artykul, "a") as plik:
#     print("A")

# with open(artykul, "w") as plik:
#     print("W")

# with open(artykul, "r+") as plik:
#     print("R")

# try:
#     with open(artykul, "r+") as plik:
#         print("R")
# except FileNotFoundError:
#     print("Nie ma pliku")
# except IOError:
#     print("Jednak")
# finally:
#     print("Zamkniecie")



# for l in range(0,99,33):
#     print(l)


# lista_a = [1, 2, ‘trzy’ 4]
# lista_b = list('jeden', 'dwa', 3, 4)
# lista_c = lista_b[::-1]


# nazwisko = 'Kowalski'
# print(nazwisko[1:7:2])

# indeks = 0
# for litera in 'Kotek':
#     print(indeks, litera)
#     break
#     indeks +=1
# print(indeks)

# wynik = 3
# a = ['ala', 'jeden', wynik]
# wynik = 43
# b = a.copy()
# a.append('Ola')
# print(a)
# print(b)

# i = 100
# while i >= 100:
#     print(i)
# i -= 1
#
# print(i)

# def funcka_a(numer, opcja):
#     pass


# imie = "ola"
#
# def duza_litera(imie="ala"):
#     imie = imie.capitalize()
#     return imie
# print(duza_litera())

# osoby = {0:"O", 1:"A"}
# osoby.update({4:'A'})
# print(osoby)

# imie = "Kamila"
#
# if imie[0].isupper() and not imie[-1].isupper():
#     print("Ala")
# elif imie == "Kamila":
#     print("K")