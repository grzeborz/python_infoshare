# WSKAZÓWKI: nie musisz robić całego zadania na raz - rozbij sobie bardziej skomplikowane zadania na jak najmniejsze
# czesci, testuj i powiekszaj

# 1 stwórz kilka zmiennych różnych typów - int, float, boolean, string

int_variable = 35

# 2 za pomocą funkcji print() wypisz wartości powyższych zmiennych, podając ich typ (użyj funkcji type)
# pamiętaj o formatowaniu i znakach specjalnych, najlepiej aby pokazywać wartości wraz z typami zmiennych
# w nowej linii

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

# 4. Indeksowanie (slajd dzien 3 od strony 4)
# stwórz nową zmienną typu string oraz zmienną pomocniczą, do której przy pomocy indeksowania,
# przypiszesz odwrócony string pierwszej zmiennej (możesz przejrzeć slajd 4 z prezentacji dnia 3 i sprawdzic np w konsoli
# które indeksowanie odwraca)

my_string = "dsadasdad"
my_string_backwords = ???

# 5. rozszerz zadanie 4 - sprawdź czy string jest palindromem
# 6. przy pomocy funkcji input() rozszerz zadanie 5 tak aby uzytkownik wpisał słowo i program powiedział,
# czy wisane slowo jest palindromem

# pętle oraz instruckje warunkowe
# 7. wykorzystaj funkcje input() i zagraj z uzytkownikiem programu w grę RPG
# Poinformuj użytkownika że stoi na rozdrozu - moze isc prosto, w lewo, lub w prawo
# aby pójść prosto - musi wpisać "straight", w lewo - "left", w prawo = "right"
# w zależności od wyboru ścieżki, poinformuj użytkownika kogo spotkał (dla Twojej wyobraźni sky is the limit)
# jeżeli użytkownik nie wpisał poprawnie kierunku - napisz że nie umie się grać...
# (do rozwiazania przyda się if elif else)

# 8. rozszerz zadanie 7 w taki sposób, aby zachęcić użytkownika jeszcze raz do wyboru ścieżki, jeżeli
# nie wpisał komendy poprawnie
# (przyda się pętla while - mozesz zatrzymać skrypt ręcznie jeżeli w czasie wykonywania się zapętlił nie tak jak powinien)

# 9. Klasa range - przy użyciu pętli for in oraz użyciu range, wypisz tylko liczby podzielne przez 7 w zakresie 0-77
# wskazówka: przyda się warunek if oraz modulo %
# 4 % 2 == 0 -> true

# 10. listy - []
# wygeneruj 2 listy liczb o tych samych rozmiarach, ale różnych wartościach

# 11. stwórz nową listę, używając dwóch list z zadania 10. lista ma zawierać liczby z listy pierwszej podniesione
# przemnozone przez liczbę o tym samym indeksie z listy drugiej

# [1, 2, 3]
# [3, 8, 2]
# -> [3, 16, 6]