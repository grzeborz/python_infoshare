# def do_nufffin(x,y, imie="Ala", wiek = 18):
#     """Funkcja która nie robi absolutnie nic,
#     najpewniej byłaby używana przez memicznych
#     władców internetu, 4chan i 9gag"""
#     pass
# import do_nuffin from do_nuffin
# print(do_nuffin.__doc__)
# print(do_nufffin(23, 30, 23, imie="Iza"))
#
# imie = ["Jola", "marcysia"]
#
# def zmien_imie():
#     #imie.append(x)
#     imie = ["Teresa"]
#
# print(imie)
#
# print(zmien_imie())
#
# print(imie)


# napisz funkcję sumujący wszystkie elementy w liscie

# lst_num = [x**2 for x in list(range(10,20))]
# print(lst_num)
#
# def sum_list(x):
#     sum = 0
#     for i in x:
#         sum = sum + i
#     print("Wynik sumy to: ", sum)
#     return sum
#
# sum_list(lst_num)



#drugi sposób

# def sum_od_numbers(elements_list):
#     """
#     this function will return the list of
#     numers
#     :param elements_list:
#     :return:
#     """
#     suma = sum([elements_list])
#     return suma
#
# sum_od_numbers(lst_num)

# znajdz najwiekszy / najmniejszy element w liscie - napisz dwie funkcje

# def max_elem(x):
#     liczba = 0
#     for i in x:
#         if i > liczba:
#             liczba = i
#         else:
#             pass
#     print(f"Największa liczba to: {liczba}")
#
# def min_elem(list_of_numbers):
#     """
#     List returned a minimal value
#      from list elements
#     :param list_of_numbers:
#     :return:
#     """
#     minimalna = min([i for i in list_of_numbers])
#     print(f"Najmniejsza liczba to: {minimalna}")
#
# max_elem(lst_num)
# min_elem(lst_num)

# 2 sposoby - najpierw ręcznie, następnie sprytnie

# funkcja ktory zmieni zdanie w liste wyrazow
# zdanie = "Ala ma kota, kot ma Ale"
#
# zadanie_pokrojone_split = zdanie.split()
# print(zadanie_pokrojone_split)
# def zdanie_petla(x):
#     lista_wyrazow = []
#     for wyraz in zdanie:
#         lista_wyrazow.append(wyraz)
#     print(lista_wyrazow)
#
# zdanie_petla(zdanie)
# napisz funckję przyjmujaca liste stringow,
# a zwracakaca liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2
# lst_string = ['abc', 'xyz', 'aba', '1221']
#
# def list_of_list_elem_lenght(list_of_elements):
#     """
#     Function to create a output by
#     printing lenght of its elements
#     :param list_of_elements:
#     :return:
#     """
#     l_slow = 0
#     for x in list_of_elements:
#         # print(x)
#         # print(x[0])
#         if len(x) >= 2:
#             # print(len(x))
#             if x[0] ==x[-1]:
#                 l_slow = l_slow + 1
#     print(f"Liczba słów wynosi: {l_slow}")
#
#     # 4 zadanie:
# def how_many_valid_strings(list_of_strings):
#     counter = 0
#
#     for word in list_of_strings:
#         if (len(word) >= 2 and word[0] == word[-1]):
#             counter += 1
#
#     return counter
#
# print(how_many_valid_strings(['aba', 'sdsda', '12221', 'bbbbb']))

# l_wyrazow = 0
# liczba_do_sumy =[x[0] for x in enumerate(list_of_elements)]
# l_wyrazow = l_wyrazow+liczba_do_sumy
#
# print(l_wyrazow)
# liczba_strinow = 0
# for x in enumerate(list_of_elements):
#     [x for x[0] in enlist_of_elements]
#     # print(x)
#     # for idx in x[0]:
#     #     print("IDX", idx)
#     #     # liczba_strinow = int(liczba_strinow) + int(idx)
#     #     # print(liczba_strinow)
#     # # print(x)

# list_of_list_elem_lenght(lst_string)
#
# # program znajdujacy wartosci, ktre wystepuja tylko raz
# lista_a = [10,20,30,20,10,50,60,40,80,50,40]
#
# def get_numbers_occured_once(list_of_numbers):
#    list_of_valid_numbers = []
#
#    for number in list_of_numbers:
#        if list_of_numbers.count(number) == 1:
#            list_of_valid_numbers.append(number)
#
#    return list_of_valid_numbers
#
#
# print(get_numbers_occured_once(lista_a))
#
# def wyszukaj_unikalne(list_of_elem):
#     """
#     Unikalne wyprintuje
#     :param list_of_elem:
#     :return:
#     """
#     lst_uniq = []
#     for x in list_of_elem:
#         if x not in lst_uniq:
#             lst_uniq.append(x)
#         else:
#             pass
#     print(f"Pierszy sposó: {lst_uniq}")
#
# wyszukaj_unikalne(lista_a)
#
# def unikaty(elements_of_list):
#     unique = set(elements_of_list)
#     print(f"Drugi sposó: {unique}")
#
# unikaty(lista_a)

# program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
# podpowiedz - del lub pop()
# lista_b = [10,20,30,20,10,50,60,40,80,50,40]
#
# def unikaty_w_miejscu(list_elem):
#     unikalne = set(list_elem)
#     print(f"Usuwanie w miejscu: {unikalne}")
#
# unikaty_w_miejscu(lista_b)
# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

# def wspolny_elem(list_1, list_2):
#     """
#     Function that compares two lists
#     :param list_1:
#     :param list_2:
#     :return:
#     """
#     for x in list_1:
#         # print(x)
#         # print([y for y in list_2])
#         if x in [y for y in list_2]:
#             print('True')
#             break
#         else:
#             pass
#     print(f"Listy posiadają wspólny element a jest nim {x}")
# wspolny_elem(lista_a, lista_b)

# stworz macierz (4 x 5), ktorej wszystkie komorki wypelnione sa znakiem *

# def generate_matrix():
#     result = []
#     for i in range(4):
#         col = []
#         for j in range(5):
#             col.append('*')
#         result.append(col)
#     return result
#
#
# print(generate_matrix())

# def random_tab(n : int):
#    return [[ran.randint(-9,9) for x in range(n)] for y in range(n)]
#
# random_tab(5)
# g = '*'
# print(g*5)
#
#
# s = [g for g in list(range(4))]
# print(s)
#
# import numpy as np
# #print(np.matrix('g *5; g * 4'))
#
# # print(np.array(range(20)).reshape((4,5)))
#
# macierz = np.array(range(20)).reshape((4,5))
#
# def mazierz_z_gwiazdek(x):
#     for i in x:
#         i = '*'
#         print(i)
#
#     print(x)
#
# mazierz_z_gwiazdek(macierz)
#
#
# print((range(20)):(range(20))][(range(20)):(range(20))])

# matrix_list = [[d:d]:[f:f]]
# print(matrix_list)
# wybierz losowo element z listy
# wskazowka - import random

# oblicz częstość elementów w liście (ile razy)
# jedna wersja zwykla pętle, ify itd
# my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]
#
dict_unique = {}
# for i in my_list:
#     if i in dict_unique:
#         dict_unique[i] += 1
#     else:
#         dict_unique[i] = 1
#
#
# print(f"Pierszy sposó: {dict_unique}")


# druga - moze jest jakis modul gotowy???
my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]

def liczba_elem(elements_in_list):
    for i in my_list:
        if i in dict_unique:
            dict_unique[i] += 1
        else:
            dict_unique[i] = 1
    return dict_unique
print(liczba_elem(dict_unique))

print([i for i in liczba_elem(my_list)])

# baza_film = {2000:"SpiderMan", 2001: "Van Helsing", 2003:"God Father"}
#
# baza_film[2000] = ["Animatrix", "Transformers 1"]
# baza_film[2009] = ["Transformers 3"]
#
# # baza_film[2000
#
# def dict_name(dict):
#     """
#     Function for printing dictionary elements
#     :param dict:
#     :return:
#     """
#     for key,item in dict.items():
#         # print(f"W roku {key} powstał film {item}")
#         print(f"W roku {key} powstał film {[item for  key in dict.items()]}")
#
# dict_name(baza_film)
#
# baza_film[2001]= "Doom"
#
# dict_name(baza_film)
#
# print(alll = [])