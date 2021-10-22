from Juego.Variables import *
#implementacion de las diferentes balas

def tipobala(eleccionbala,c105,cperforante,c60):
	if eleccionbala == 1 and c105 > 0:
		#municion 105 mm
		balaaux = 50
		c105 = c105 - 1
	elif eleccionbala == 2 and cperforante > 0:
		#municion perforante
		balaaux = 40
		cperforante = cperforante - 1
	elif eleccionbala == 3 and c60 > 0: 
		#municion 60 mm
		balaaux = 30
		c60 = c60 - 1
	else:
		print("No te quedan mas balas")
