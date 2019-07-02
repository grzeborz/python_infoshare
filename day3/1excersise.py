# zdanie = "encykopedia"
#
# print("drukuje 4 znak: ",zdanie[4])
# print("drukuje 3 znak od końca: ",zdanie[-3])
# print("drukuje od pozycji nr 2 do nr 8: ",zdanie[2:8])
# print("drukuje od początku do pozycji nr 7: ",zdanie[:7])
# print("drukuje od 8 pozycji do końca: ",zdanie[8:])
# print("drukuje od 1 do 7 co dwa znaki: ",zdanie[1:7:2])
# print("drukuje co jeden od tyłu: ",zdanie[::-1])
# print("drukuje co jeden, czyli normalnie: ",zdanie[::1])
# print("drukuje co drugi znak: ",zdanie[::2])
# print("drukuje co drugi znak od tyłu: ",zdanie[::-2])
# #[STARTOWA POZYCJA : KONCOWA POZYCJA : KROK )

# #temperature = 28
# temperature = int(input("Miszczu, podaj temperaturke: "))
# #CTRL + Q - tedy podaje dokumntacje do funkcji lub metody
#
# goraco = int(input("Miszczu, podaj temperaturke jak jest Tobie gorąco: "))
# cieplo = int(input("Miszczu, podaj temperaturke jak jest Tobie cieplo: "))
# niecieploniezimno = int(input("Miszczu, podaj temperaturke jak jest Tobie ani cieplo ani zimno: "))
#
# if (temperature >= goraco):
#     print("Miszczu, jest gorąco")
# elif (temperature >= cieplo):
#     print("Miszczu, jest ciepło")
# elif (temperature >= niecieploniezimno):
#     print("Miszczu, nie jest ciepło ani zimno")
# else:
#     print("Miszczu, jest zimno")
#
# print("Miszczu, kopsnij piątaka")

#####
#Zadanie
#####

# napisz program ktory przyjmuje zdanie od uzytkownika (input)
#
# jezeli napis zaczyna sie na litere 'a' - powiedz uzytkownikowi ze zaczyna sie od pierwszej litery alfabetu
# jezeli na litere 'z' - powiedz uzytkownikowi ze zaczyna sie od ostatniej litery alfabetu
# w przeciwnym razie powiedz ze zaczyna sie od innej litery niz 'a' i 'z'
# wyraz = input("Miszczu, podaj wyraz: ")
#
# if wyraz[0].lower() == 'a':
#     print("Miszczuniu, Twoj wyraz zaczyna się na literę 'A' która jest pierwszą literą alfabetu.")
# elif wyraz[0] == 'z' or wyraz[0] == 'Z':
#     print("Miszczuniu, Twój wyraz zaczyna się na literę 'Z' która jest ostatnią literą alfabetu")
# else:
#     print(f"Miszczuniu, Twój wyraz zaczyna się na literę \"{wyraz[0]}\" czyli innej niż A i Z.")
#
# print("Miszczu, kopsnij piątaka.")

# #zdanie = "Ala msa kota"
# zdanie = input("Miszczuniu, podaj zdanie: ")
# #wyraz_szukany = "Ala"
# wyraz_szukany = input("Miszczuniu, jakiego wyrazu szukamy: ")
#
# wyrazy_rozdzielone = zdanie.lower().split()
#
# if wyraz_szukany.lower() in wyrazy_rozdzielone:
#     print(f"Kierowniku, w zdaniu \"{zdanie}\" znajduje się wyraz \"{wyraz_szukany}\"")
# else:
#     print(f"Kierowniku, NAJGORZEJ, w \"{zdanie}\" nie ma szukanego wyrazu \"{wyraz_szukany}\"")
# print("Kochanieńki, robota wykonana, kopsnij piątaka")

#temperature >= 20  and humidity <80

# lista = [list(range(1,4)),list(range(4,7)),list(range(7,10))]
# print(lista)
# print(lista[1][2])
#print(lista([1][:])([2][:]))

######
#ZADANIA
######

#repeatHowManyTimes = int(input("Please tell me how many times to repeat..."))

# for index in range(repeatHowManyTimes): #funkcja range jest po to by wygenerować liczbę do przeliczania
#    print(f"Hello, it's me for {index} time")

# 0 przypisz do zmiennej o odpowiedniej nazwie nazwy miesiaca (January, February) - mozna uzyc skrotow Jan, Feb itd...
miesiace = ('jan', 'feb', 'march', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
# wypisz nazwy miesiaca funkcja print()
# print(miesiace)
# nazwy miesiaca musza byc oddzielone enterem (znak specjalny \n)
#
# for i in miesiace:
#     print(i)

# 1 wypisz co druga literę z napisu - uzyj petli for:
# text = "Python is a fantastic snake"
#print(text[::2])

# for i in text[0::2]:
#     print(i)


# 1.1 skrot - przeczytaj https://docs.python.org/release/2.3.5/whatsnew/section-slices.html i wypisz co druga litere, tym razem w krotszy sposob
#print(text[::2])
# 1.2 wypisz teraz co trzecią literę :wink:
#print(text[::3])

# 2 wyszukaj w dokumentacji jak rozbić powyższy tekst na listę słów a nastepnie wydrukuj ta liste (for slowo in lista)

# lista_wyrazow = text.split()
# for i in lista_wyrazow:
#     print(i)
# you need to use method on text to seperate words
#word_list = text.?

#for word in word_list:
# you need to print here

# 3 zmien program z punktu drugiego tak, aby uzytkownik sam wpisal jakis tekst, ktory program mu rozbije na liste slow

# lista_wyrazow_do_wpisania = input("Kierowniku, wpisz jakies zdanie, takie nie za długie, nie za krótkie: ")
# lista_wyrazow_rozdzielona = lista_wyrazow_do_wpisania.split()
# for i in lista_wyrazow_rozdzielona:
#     print(i)
#     print()

#parametry podajemy CTRL + P


text_input = "Python is a fantastic snake"
dlugosc = len(text_input)
lista_indeksow = range(0,dlugosc,2)
print(dlugosc)
print(lista_indeksow)


for i in lista_indeksow:
    print(text_input[i], end="") #end jest po to by pokazać jaki znak jest na końcu