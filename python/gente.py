gente = []
status = 1
while status == 1:
	a = input('Agregar Personas (Y/N): ')
	if a == 'y' or a == 'Y':
		nombre = input('Nombre: ')
		gente.append(nombre)
	elif a == 'n' or a == 'N':
		status = 0
for i in gente:
	print(i)