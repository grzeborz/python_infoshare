import os

# print(os.listdir())

# os.path.isdir()
# os.path.isfile()


# dict_name = ['moj_modul.py', 'directory', 'test.py', '__pycache__']

# lista = []
# lista = ['test']
# def is_dir_or_file(lista):
#     """
#     Fuction checking if the object is a directiory or file
#     :param lista:
#     :return:
#     """
#     if len(lista) == 0:
#         print("Katalog jest pusty 1")
#
#     for name in lista:
#         checking = os.path.isdir(name)
#         # print(checking)
#         if checking is True:
#             print(f"Katalog: {name}")
#         else:
#             print(f"Plik: {name}")
### lista
# def listdir():
#     """
#     Fuction checking if the object is a directiory or file
#     :param lista:
#     :return:
#     """
#     lista = os.listdir()
#     lista_elem = []
#
#     if len(lista) == 0:
#         return "Katalog jest pusty 1"
#
#     for name in lista:
#
#         checking = os.path.isdir(name)
#         if checking is True:
#             lista_elem.append(f"Katalog: {name}")
#         else:
#             lista_elem.append(f"Plik: {name}")
#     return lista_elem

##słownik
def listdir():
    """
    Fuction checking if the object is a directiory or file
    :param lista:
    :return:
    """
    lista = os.listdir()
    dict_elem = {}

    if len(lista) == 0:
        return "Katalog jest pusty 1"

    for name in lista:
        checking = os.path.isdir(name)
        if checking is True:
            dict_elem["Katalog:"] = (name)
            # if item in dict_elem.items():
            #     dict_elem["Katalog:"].append(item)
        else:
            dict_elem["Plik:"] = (name)
    return dict_elem
print(listdir())

# is_dir_or_file(lista)

# if(list[0] == True):
#     print('Error')
#     exit()
# wynik = 10/0

# try:
#     lista[0]
#     wynik = 10/0
#     #w try kod jest wykonywan po kolei i pierwszy napotkany bład jest logowany
# except IndexError:
#     print('Katalog jest pusty')
#     exit()
# except ZeroDivisionError:
#     print('Nie dziel przez zero')
#     exit()
# except:
#     print('Nieznany błąd')
#     exit()
#
# for name in lista:
#     if os.path.isdir(name):
#         print(f"Katalog: {name}")
#     else:
#         print(f"Plik: {name}")

#
# if not lista:
#     print("Katalog jest pusty 2")
