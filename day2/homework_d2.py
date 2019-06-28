# 1. Przypisz do zmiennej o nazwie float_but_int wartosc dzielenia 50 / 2. Jakiego typu jest wynik (do sprawdzenia typu type(zmienna))?
#ODP 1.1.
float_but_int = 50/2
#ODP 1.2.
print('wynik zmiennej: ', float_but_int)
print('zmienna float_but_int jest typu: ', type(float_but_int))
#   Sprawdz przy pomocy metody wbudowanej w otrzymany wyzej typ czy liczba jest calkowita (dokumentacja - dir(nazwa_zmiennej) lub help(typ)), dokumentacja Python

#wydrukowuję dostępne opcje:
#print(dir(float_but_int))
#print(help(float_but_int))

#Odp. 1.3
print('Czy zmienna liczbą calkowita? Odpowiedz: ', float_but_int.is_integer())
###
# 2. (Kalkulator, albo Python) - liczba zapisana w systemie binarnym na 8 bitach - 11011010 to w systemie dziesietnym liczba:

print(int('11011010', 2))

#lub prosty program:
bin_to_10 = str(input("Podaj liczbe w systemie binarnym: "))
print(int(bin_to_10, 2))


###
# 3. Przypisz do 3 zmiennych pojedyncze slowa "Sun", "is", "setting", polacz je w jeden ciag znaków, ale tak, aby kazde slowo bylo w nowej linii, kazda nowa linia ma miec jedno
# wiecej wciecie tabulatora, tak aby wygladalo to nastepujaco:
#
# Sun
#               is
#                              setting
sun, sunis, setting = 'Sun', 'is', 'setting'

print(f' {sun} \n\t {sunis} \n\t\t {setting}')

# Medium:
#
# 4. zapoznaj sie z metoda input() w Python - wyszukaj w dokumentacji i sprawdz dzialanie. Funkcja print zachec uzytkownika, aby podal liczbe, nastepnie wypisz kwadrat oraz szescian tej liczby
# Postaraj sie o odpowiedni wyglad odpowiedzi, opisujacy uzyskane wyniki, np.
# Szescian liczby x wynosi x^3, natomiast kwadrat x^2
#
liczba = input("Podaj magiczna liczbę: ")
print(f'Uzytkowniku pythona, szescian magicznej liczby {liczba} wynosi {int(liczba)**3}, natomaist kwadrat {int(liczba)**2}')


# Challenging:
#
# 5. Warunek if - przy pomocy metody input pobierz od uzytkownia wartosc temperatury. Ustaw 3 minimalne temperatury jako zmienne - zimna, ciepla, goraca (np. 10 stopni, 20 stopni, 30 stopni)
# i na podstawie temperatury podanej przez uzytkownika, wyswietl czy jest zimno, cieplo, czy goraco
#
temperatura = input("Kierowniku, jaka dziś temperatura? Wartość wpisz po prawej: ")
if int(temperatura) < 10:
    print("Kieroooowniku, to dziś zimiutko. Ubierz palto")
elif int(temperatura) > 11 and int(temperatura) < 29:
    print("Kieroooowniku, to dziś optymalnie.")
else:
    print("Kieroooowniku, to dziś gorycooo. Ubierz sandały i skarpety")

# 6. Petla while
#
# Oblicz silnie z podanej przez uzytkownika (metoda input) liczby - wyszukaj algorytm na silnie i napisz - przydadza sie zmienne, warunek if, operator *=

silnia = int(input("Kierownikuuu, obliczymy silnię tylko kopsnij liczbę: "))
i=0
suma=1
while(silnia !=i):
    i += 1
    suma = suma * i
print(suma)
print(f"Kierownikuuu, twoja liczba to {suma}.")
