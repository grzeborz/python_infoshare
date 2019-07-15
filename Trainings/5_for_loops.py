# policz samogloski i spolgloski
zdanie = input("Podaj jakieś zdanie: ")

samogloski = 0
spolgloski = 0

lista_samogl = "aeiouyąęó"

for litera in zdanie:
	if litera in lista_samogl:
		samogloski +=1
	else:
		spolgloski +=1
# tutaj nalezy napisac kod ;)


print(f"Samoglosek: {samogloski}, spółgłosek: {spolgloski}")