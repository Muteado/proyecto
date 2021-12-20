from .Rectangulos import *
from .Variables import *

class BotonesOpciones:
    def botonesopciones(boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16):
        #Dibuja los rectangulos de los botones
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton1,0)#Jugadores IA
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton2,0)#Jugadores IA
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton3,0)#Jugadores IA
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton4,0)#Jugadores IA
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton5,0)#Balas
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton6,0)#Balas
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton7,0)#Balas
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton8,0)#Balas  
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton9,0)#Pantalla
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton10,0)#Pantalla
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton11,0)#Pantalla
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton12,0)#Pantalla
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton13,0)#Entorno
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton14,0)#Entorno
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton15,0)#Entorno
        Rectangulos.dibujaRectangulos(Pant, Amarillo, boton16,0)#Entorno

        #Dibuja los rectangulos de los textos

        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 150, 250, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 250, 250, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 350, 250, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo((Pant.get_width()/2)-550, 450, 250, 50),0)

        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 150, 250, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 250, 250, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 350, 150, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(470, 450, 250, 50),0)


        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 150, 150, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 250, 150, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 350, 150, 50),0)
        Rectangulos.dibujaRectangulos(Pant, Amarillo, Rectangulos.rectangulo(910, 450, 150, 50),0)