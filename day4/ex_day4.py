#typ referencyjny w pythonie
#wskazujemy na to samo miejsce w pamięci
old_list = [1,2,3]
new_list = old_list

old_list[0] = 4
print(old_list)
print(new_list)


old_number = 4
new_number = old_number

old_number = 6

print(old_number)
print(new_number)

#to jest typ rposty i dlatego zachowuje się tak że przepisuje wartości bez odwoływania się do innego miejsca w pamięci
#typ wartościowy

new_list = list.copy(old_list)
nowa_lista = list(old_list)
nowsza_lista = old_list[:]

import copy

nowka_lista = copy.deepcopy(old_list)

old_list[1] = 8

print(new_list)
print(nowa_lista)
print(nowsza_lista)
print(nowka_lista)
print(old_list)

print(type(nowka_lista))
print(type(copy.deepcopy(old_list)))

lista_referecyna = list(range(0,10))
print(lista_referecyna)
lista_kwadraty = []
for i in lista_referecyna:
    i = i ** 2
    lista_kwadraty.append(i)
    #print(i)

print(lista_referecyna)
print(lista_kwadraty)


#inny sposób
old_listK = list(range(0,10))

for index,i in enumerate(old_listK):
   old_listK[index]=i*i
print(old_listK)

#jeszcze inny pomysł

lista_kwadraty_plain = [x**2 for x in lista_referecyna]
print(lista_kwadraty_plain)

# def turn_to_power(list, power=1):
#     return [number**power for number in list]


import numpy as np
array_kwadraty_numpy = np.power(lista_referecyna, 2)
print(array_kwadraty_numpy)
lista_kwadraty_numpy = list(array_kwadraty_numpy)
print(lista_kwadraty_numpy)


lista_kwadr_inno = [print(f'Drukowanie w kwadracie: {int(x)-100}') or x -100 for x in lista_kwadraty_numpy if x != x%2]
print(f'Liczba: {lista_kwadr_inno}', end='\n')

# old_list_excluded_20_to_25=[x for x in old_list if x not in range (20,25)]
# print(f'Old list not in range 20 to 24: {old_list_excluded_20_to_25}')
#
# old_list_rased_by_10=[x+10 for x in old_list]
# print(f'Old list raised by 10: {old_list_rased_by_10}')




##########################
stara = list(range(10))
print(stara)
inno = [print(f'Drukowanie bez : "{x}" i drukowanie w kwadracie: "{int(x)**2}"') or x**2 for x in list(range(1,10)) if x > 2 and x  < 6]

uno, duo = [x**2 for x in list(range(20,30))],[y**2 for y in list(range(60,70))]
print(uno)
print(duo)

eska = []
for elem_a, elem_b in zip(uno, duo):
    x = elem_a * elem_b
    eska.append(x)

print(eska)

words = ["EdsaEFEFe", "BiggER", "DrudSK"]
bigger_font = [word.upper() for word in words]
small_font = [word.lower() for word in words]

print(words)
print(bigger_font)
print(small_font)

#############

#listy zagnieżdzone i kopiowanie całych list zagnieżdzonych
import copy

list_zagn = [[[2,3,45],2,3,4]]
print(list_zagn)
nested = list_zagn.copy()
nested_deep = copy.deepcopy(list_zagn)
print(nested_deep)

nested_deep[0][0][1] = 36


print(list_zagn)
print(nested_deep)


uno, duo = [x**2 for x in list(range(20,30))],[y**2 for y in list(range(60,90))]
print(uno)
print(duo)

eska = []
for elem_a, elem_b in zip(uno, duo):
    x = elem_a + elem_b
    eska.append(x)

print(eska)



#########################

#    PRAWDA I FAŁSZ

# 1. True and True
#True 1
# 2. False and True
#False 1
# 3. 1 == 1 and 2 == 1
#False 1
# 4. "test" == "test"
#True 1
# 5. 1 == 1 or 2 != 1
#True 1
# 6. True and 1 == 1
#True 1
# 7. False and 0 != 0
#False 1
# 8. True or 1 == 1
#True 1
# 9. "test" == "testing"
#False 1
# 10. 1 != 0 and 2 == 1
#False 1
# 11. "test" != "testing"
#True 1
# 12. "test" == 1
#False 1
# 13. not (True and False)
#True 1
# 14. not (1 == 1 and 0 != 1)
#False 1
# 15. not (10 == 1 or 1000 == 1000)
#True 0 should be False bo not(True) = False
# 16. not (1 != 10 or 3 == 4)
#False 1
# 17. not ("testing" == "testing" and "Zed" == "Cool Guy")
#True 1
# 18. 1 == 1 and (not ("testing" == 1 or 1 == 0))
#True 1
# 19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
#True 0 should be False bo False and False
# 20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
#False 1



