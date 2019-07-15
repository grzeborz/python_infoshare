# oblicz czy rok jest przestępny

# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok = input("Podaj rok: ")
rok = int(rok)

def czy_rok_jest_przystepny(year_input):
    '''
    Funkcja do sprawdzania czy dany rok
    jest przystępny
    :param year_input:
    :return:
    '''
    if rok%4 == 0 and rok%100 != 0 or rok%400 == 0:
        print(f"Rok {rok} jest rokiem przystępnym")
    else:
        print(f"Rok {rok} niestety nie jest rokiem przystępnym")


print(czy_rok_jest_przystepny(rok))

#print(f"Rok {rok} jest rokiem przystępnym")


# zmieniamy stringa (input) na int
