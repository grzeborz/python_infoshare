# Easy:
#
# 1. Przypisz do zmiennej o nazwie float_but_int wartosc dzielenia 50 / 2. Jakiego typu jest wynik (do sprawdzenia typu type(zmienna))?
#   Sprawdz przy pomocy metody wbudowanej w otrzymany wyzej typ czy liczba jest calkowita (dokumentacja - dir(nazwa_zmiennej) lub help(typ)), dokumentacja Python

float_but_int = 50/2
print(float_but_int)
print(type(float_but_int))
print(float_but_int.is_integer())


# 2. (Kalkulator, albo Python) - liczba zapisana w systemie binarnym na 8 bitach - 11011010 to w systemie dziesietnym liczba:

print(int('11011010', 2))

# 3. Przypisz do 3 zmiennych pojedyncze slowa "Sun", "is", "setting", polacz je w jeden ciag znaków, ale tak, aby kazde slowo bylo w nowej linii, kazda nowa linia ma miec jedno
# wiecej wciecie tabulatora, tak aby wygladalo to nastepujaco:
#
# Sun
#               is
#                              setting

word_1 = "Sun"
word_2 = "is"
word_3 = "setting"

print(f"{word_1}\n\t{word_2}\n\t\t{word_3}")
print("{}\n\t{}\n\t\t{}".format(word_1, word_2, word_3))

# Medium:
#
# 4. zapoznaj sie z metoda input() w Python - wyszukaj w dokumentacji i sprawdz dzialanie. Funkcja print zachec uzytkownika, aby podal liczbe, nastepnie wypisz kwadrat oraz szescian tej liczby
# Postaraj sie o odpowiedni wyglad odpowiedzi, opisujacy uzyskane wyniki, np.
# Szescian liczby x wynosi x^3, natomiast kwadrat x^2

y = int(input('Wstaw liczbe:'))
print(f'Szescian liczby {y} wynosi {y ** 3} natomiast kwadrat {y ** 2}')
print('Szescian liczby' + ' ' + str(y) + ' ' 'wynosi ' + str(y ** 3) + ' natomiast kwadrat ' + str(y ** 2))

# Challenging:
# 5. Warunek if - przy pomocy metody input pobierz od uzytkownia wartosc temperatury. Ustaw 3 minimalne temperatury jako zmienne - zimna, ciepla, goraca (np. 10 stopni, 20 stopni, 30 stopni)
# i na podstawie temperatury podanej przez uzytkownika, wyswietl czy jest zimno, cieplo, czy goraco

z = int(input ("Podaj aktualna temperature:"))
temp1=10
temp2=20
temp3=30

if z<temp1:
   print('Jest zimno')
elif z > temp1 and z< temp2:
   print('Jest cieplo')
else:
   print('Jest goraco')

# 6. Petla while
#
# Oblicz silnie z podanej przez uzytkownika (metoda input) liczby - wyszukaj algorytm na silnie i napisz - przydadza sie zmienne, warunek if, operator *=

source_number = int(input('Podaj liczbę, aby obliczyć silnię:\n>'))

if source_number == 0:
    print(f'Silnia liczby {source_number} wynosi 1')
else:
    result = 1
    while(source_number>=1):
        result = result * source_number
        source_number = source_number-1
    print(f'Silnia liczby {source_number} wynosi {result}')