def resolver(problemas,x):
	problemas = problemas.split(" ")
	while x < len(problemas):
		del problemas[x]
		x += 1
	for i in problemas:
		if problemas[i].isdigit():
			problemas[i] = int(problemas[i])
	return problemas
print(resolver(input("Ecuacion: "),1))