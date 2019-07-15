# 10. zamiana temperatury
#     wejscie: temperatura w C lub F, np: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni" - jezeli podano w F to wypisz w C i odwrotnie
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

jednostka_temperatury = input("Podaj proszę jednostkę temperatury: ")
tempseratura = input("Podaj proszę temperaturę: ")

def zmiana_temperatury(jenostka, temperatura):
    '''
    Funkcja do konwersji temparatury
    :param jenostka:
    :param temperatura:
    :return:
    '''

