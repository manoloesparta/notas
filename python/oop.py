import random
import time

class Persona:

	def __init__(self,nombre):
		self.nombre = nombre
		self.vida = 50

	def atacar(self):
		return random.randint(0,10)

def main():
	Sam = Persona(input('Persona 1: '))
	Paul = Persona(input('Persona 2: '))
	suspenso = input('Suspenso (y/n): ')
	i = 1

	while Sam.vida > 0 and Paul.vida > 0:

		if i % 2 == 0:
			turno = Sam.nombre
			noturno = Paul.nombre
			dano = Sam.atacar()
			Paul.vida -= dano
			menos = Paul.vida
		else:
			turno = Paul.nombre
			noturno = Sam.nombre
			dano = Paul.atacar()
			Sam.vida -= dano
			menos = Sam.vida
		i += 1

		print(turno + ' ataca a ' + noturno)
		print('Daño: ' + str(dano))
		print(noturno + ' salud: ' + str(menos) + '\n')

		if suspenso == 'y':
			time.sleep(2)

	if Sam.vida > Paul.vida:
		print(Sam.nombre + ' gano!')
	else:
		print(Paul.nombre + ' gano!')

main()
