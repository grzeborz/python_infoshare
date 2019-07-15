# napisz funkcje obliczajaca pole kwadratu
bok = int(input("Podaj dlugosc boku kwadratu: "))

def kinia_do_kwadratu(dlugosc_boku):
	pole_kwadratu = dlugosc_boku ** 2
	return pole_kwadratu
	
print(f"Pole kwadratu wynosi {kinia_do_kwadratu(bok)} centymetrów kwadratowych.")