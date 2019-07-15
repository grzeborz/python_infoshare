# obl. ilość l. parzystych i nieparzystych w zakresie

zakres = range(23746)

parzyste = 0
nieparzyste = 0

for liczba in zakres:
	if liczba%2 == 0:
		parzyste +=1
	else:
		nieparzyste +=1
#     tutaj nalezy napisac kod

print(f"Liczb parzystych: {parzyste}, liczb nieparzystych: {nieparzyste}")



