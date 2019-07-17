# program, ktory wypisze liczby (z zakresu 0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# propozycja uzycia petli while - ale kazde rozwiazanie jest dobre ;)

zakres = range(0,100)

liczba = 0
while liczba < 100:
	if liczba == 0:
		print(liczba)
		liczba +=1
	else:
		print(liczba)
		liczba = liczba + liczba
		