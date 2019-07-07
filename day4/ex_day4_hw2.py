# WSKAZÓWKI: nie musisz robić całego zadania na raz - rozbij sobie bardziej skomplikowane zadania na jak najmniejsze
# czesci, testuj i powiekszaj

# 1 stwórz kilka zmiennych różnych typów - int, float, boolean, string

# my_int = 35
# my_flo = 0.99991
# my_boo = True
# my_str = "Siemandero"
#
# l_var = [my_str, my_int, my_flo, my_boo]

# 2 za pomocą funkcji print() wypisz wartości powyższych zmiennych, podając ich typ (użyj funkcji type)
# pamiętaj o formatowaniu i znakach specjalnych, najlepiej aby pokazywać wartości wraz z typami zmiennych
# w nowej linii
# for x in l_var:
#     print(f'Zmienna o typie: {type(x)} posiada wartość "{x}"')

# przykład:
# Zmienna o wartości 35 jest typu int
# Zmienna o wartości 47.5 jest typu ...
# itd...

# pamiętaj o możliwości specjalnego formatowania tzw. interpolacji:
# https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36

# formatowanie (slajd z dnia 3 - od strony 3)

# 3. Wypisz zmienną typu float - dobrym przykladem bedzie liczba 1/17
# z dokładnością do 4 miejsc po przecinku
# https://stackoverflow.com/questions/8885663/how-to-format-a-floating-number-to-fixed-width-in-python

# print(f"Hej, mój float wygląda tak: {round((1/17),4)}")

# 4. Indeksowanie (slajd dzien 3 od strony 4)
# stwórz nową zmienną typu string oraz zmienną pomocniczą, do której przy pomocy indeksowania,
# przypiszesz odwrócony string pierwszej zmiennej (możesz przejrzeć slajd 4 z prezentacji dnia 3 i sprawdzic np w konsoli
# które indeksowanie odwraca)

# rever_my_str = my_str[::-1]
# print(f'Odwrócony string wygląda tak: "{rever_my_str}", natomiast oryginalny tak :"{my_str}"')

# my_string = "dsadasdad"
# my_string_backwords = ???

# 5. rozszerz zadanie 4 - sprawdź czy string jest palindromem

# def czekin_str(x):
#     if x == x[::-1]:
#         print('Zmienna jest palindromem')
#     else:
#         print("Zmienna niestety nie jest palindromem")
#
# czekin_str(rever_my_str)

# 6. przy pomocy funkcji input() rozszerz zadanie 5 tak aby uzytkownik wpisał słowo i program powiedział,
# czy wisane slowo jest palindromem

# str_input = input("Kierownikuuuu, podaj no jedno słowunio: ")
# def czekin_str_input(x):
#     if x == x[::-1]:
#         print('Zmienna jest palindromem')
#     else:
#         print("Zmienna niestety nie jest palindromem")
#
# czekin_str_input(str_input)

# pętle oraz instruckje warunkowe
# 7. wykorzystaj funkcje input() i zagraj z uzytkownikiem programu w grę RPG
# Poinformuj użytkownika że stoi na rozdrozu - moze isc prosto, w lewo, lub w prawo
# aby pójść prosto - musi wpisać "straight", w lewo - "left", w prawo = "right"
# w zależności od wyboru ścieżki, poinformuj użytkownika kogo spotkał (dla Twojej wyobraźni sky is the limit)
# jeżeli użytkownik nie wpisał poprawnie kierunku - napisz że nie umie się grać...
# (do rozwiazania przyda się if elif else)

###GRA

print("#########################################################################\n"
      "#####################                          ##########################\n"
      "#####################     GRA RPG DZIELNIA     ##########################\n"
      "#####################                          ##########################\n"
      "#########################################################################\n"
      "\n\n\n")
imie = input("Witaj na dzielni, tutaj każdy wie gdzie jego miejsce, jak masz na imię?")

while True:
    try:
        kierunek = input(f"Dobrze {imie}, stoisz jak nie lokals, bo między żabką, a monopolem, w którym kierunku idziesz? \n"
                 f"(masz do wyboru LEWO lub PRAWO), to jak?:")
    except ValueError:
        print("Kierowniku, spórbuj jeszcze raz: ")
        continue
    if kierunek.lower() == 'prawo':
        print("Spotykasz koło gospodyń dzielnicowych, próbują Tobie wcisnąć jakieś przepisy, zaprosić na wspólne pieczenie ciast\n"
              "Ty, mówiąc że zostawiłeś żelazko podłączone do gniazdka oddalasz się za najbliższym rogiem\n"
              "Co robisz dalej?")
        while True:
            try:
                krok2 = input("Idziesz PROSTO do boiska, w LEWO do najbliższego przejścia dla pieszych\n"
                              " czy w PRAWO w kierunku parku? (ew. w TYŁ do gospodyń)?")
            except ValueError:
                print("Kierowniku, spórbuj jeszcze raz: ")
                continue
            if krok2.lower() == 'prosto':
                print("Giniesz od rzuconego tulipana na odległość. Przechodziłeś w miejscu rozgrywanych zawodów osiedlowych")
                break
            elif krok2.lower() == 'lewo':
                print("Giniesz pod kołami szalonego kierowcy wózka widłowego który jechał do ziomka naprawić jego poloneza")
                break
            elif krok2.lower() == 'prawo':
                print("Przechodząc pod najbliższym drzewem atakuje i przegryza Ci tętnicę wściekła wiewiórka\n"
                      "Giniesz, leżąc pod najbliższą ławeczką")
                break
            elif krok2.lower() == 'tył':
                print("Kółko gospodyń okazuje się zakamuflowanym gangiem dzielnocowych kobiet w średnim wieku\n"
                      "po zaproszeniu do jednego z lokali zostajesz otruty nieświeżym Brownie z Wegańską Kawą\n"
                      "Giniesz od choroby popromiennej")
                break
            else:
                print("Kerownikuuu, nie umiemy czytać i pisać :D Jak już się nauczysz, wróć do mnie i pograj :P")
                break
    elif kierunek.lower() == 'lewo':
        print("Dochodzisz do najbliższego Urzędu Skarbowego, i nieopatrznie zostajesz uznany za programistę \n"
              "dostajesz za karę 90% VAT."
              "Giniesz od niewypłacalności")
        break
    else:
        print("Kerownikuuu, nie umiemy czytać i pisać :D Jak już się nauczysz, wróć do mnie i pograj :P")


# 8. rozszerz zadanie 7 w taki sposób, aby zachęcić użytkownika jeszcze raz do wyboru ścieżki, jeżeli
# nie wpisał komendy poprawnie
# (przyda się pętla while - mozesz zatrzymać skrypt ręcznie jeżeli w czasie wykonywania się zapętlił nie tak jak powinien)

# 9. Klasa range - przy użyciu pętli for in oraz użyciu range, wypisz tylko liczby podzielne przez 7 w zakresie 0-77
# wskazówka: przyda się warunek if oraz modulo %
# 4 % 2 == 0 -> true
#
# przez_7 = [x for x in range(0,77) if x % 7 == 0]
# for i in przez_7:
#     print(i)

# 10. listy - []
# wygeneruj 2 listy liczb o tych samych rozmiarach, ale różnych wartościach

# list1, list2 = [x**2 for x in list(range(20,30))],[y**2 for y in list(range(60,70))]
#
# print(list1)
# print(list2)

# 11. stwórz nową listę, używając dwóch list z zadania 10. lista ma zawierać liczby z listy pierwszej podniesione
# przemnozone przez liczbę o tym samym indeksie z listy drugiej

# l_monoz = []
# for elem_a, elem_b in zip(list1, list2):
#     x = elem_a * elem_b
#     l_monoz.append(x)
#
# print(l_monoz)
# [1, 2, 3]
# [3, 8, 2]
# -> [3, 16, 6]