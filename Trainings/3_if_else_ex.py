# 10. zamiana temperatury
#     wejscie: temperatura w C lub F, np: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni" - jezeli podano w F to wypisz w C i odwrotnie
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

typ_t = input("podaj skale temperatury[C° lub F°]: ")
temp = int(input("podaj temperature: "))

def obliczanie_temp(typ, stopnie):
	"""funkvja do obliczania temp
	"""
	if typ_t.upper() == "C":
		temp_f = (temp+32)*1.8000
		print(f"Temperatura w F° to {(temp_f)} stopni")
	elif typ_t.upper() == "F":
		temp_c = (temp-32)/1.8000
		print(f"Temperatura w C° to {(temp_c)} stopni")
	else:
		print("Blad")
		
print(obliczanie_temp(typ_t, temp))
		

