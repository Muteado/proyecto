import random
from .Textos import *
from .Variables import *
from .Tanques import *
#Habría que llamar esta funcion en relación al turno

class IA:
    def lanzamientoRobot(jugador):
        
        angulo[0] = random.randint(0,180)
        jugador.set_Angulo(angulo[0])


        velocidad[0] = random.randint(1,150)
        jugador.set_Velocidad(velocidad[0])

        
        Boton = random.randint(1,3)
        if Boton == 1:
            botonamarilloIA[0] = True
            botonnaranjaIA[0] = False
            botonmoradoIA[0] = False

        if Boton == 2:
            botonamarilloIA[0] = False
            botonnaranjaIA[0] = True
            botonmoradoIA[0] = False
        
        if Boton ==3:
            botonamarilloIA[0] = False
            botonnaranjaIA[0] = False
            botonmoradoIA[0] = True



        #bala = random.randint(0,2) #En realidad debe ser con el pos del mouse 
        #Llamar al movparabolico?
        #activar el espacio