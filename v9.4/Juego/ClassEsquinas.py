from .ClassRectangulos import Rectangulos
from .ClassTextos import Textos
from .Variables import *
from .ClaseBotones import *
import pygame


class DatosEsquinas:
    def generarBloques(posIniX,posIniY,largoBloq,altoBloq):


        #Bloques azules
        #Dibuja rectangulos negros
        for PosY in range(0,29,21):
            pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    PosY#posIniY
                    ,largoBloq+2,altoBloq+2))
            
        #Dibuja rectangulos azules sobre el negro, 
        # generando un margen negro de 2 pixeles
        for PosYA in range(0,29,21):
            pygame.draw.rect(Pant, Azul,
                    (posIniX,
                    PosYA+1#posIniY
                    ,largoBloq,altoBloq))
        
        #Bloques rojos
        #Dibuja rectangulos negros
        for PosY in range(0,29,21):
            pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    PosY#posIniY
                    ,largoBloq+2,altoBloq+2))
        #Dibuja rectangulos azules sobre el negro, 
        # generando un margen negro de 2 pixeles
        for PosYA in range(0,29,21):
            pygame.draw.rect(Pant, Rojo,
                    (Pant.get_width()-largoBloq+1,
                    PosYA+1#posIniY
                    ,largoBloq,altoBloq))
        
        # Dibuja los rectangulos de disparo del tanque azul
        Rectangulos.botones(Pant, Amarillo, (605,5,30,20))
        Rectangulos.botones(Pant, Naranja, (640,5,30,20))
        Rectangulos.botones(Pant, Morado, (675,5,30,20))
        
        #Genera textos azules
        Textos.texto_pantalla_rect('Ángulo :', Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+5)
        Textos.texto_pantalla_rect('Velocidad :', Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+26)
        #Genera textos rojos
        Textos.texto_pantalla_rect('Ángulo :', Textos.fuentes(None,23), Blanco, Pant, Pant.get_width()-largoBloq+5,posIniY+5)
        Textos.texto_pantalla_rect('Velocidad :', Textos.fuentes(None,23), Blanco, Pant, Pant.get_width()-largoBloq+5,posIniY+26)

        #vida tanques
        #Textos.texto_pantalla_rect(vidaAzul, Textos.fuentes(None,23), Negro, Pant, X_Tanque_Azul, Y_Tanque_Azul)

    def textosEsquinas(texto,rectangulo,color,activo):
        #Cambia el color del recuadro en caso de ser clickeado para saber que está activo
        
        if activo == True:
            if color == Rojo:
                color = Azul
            else:
                color = Rojo
        #Mantiene el color None el rectangulo no está activo
        else:
            color = color
        #Dibuja el borde del rectangulo
        Rectangulos.dibujaRectangulos(Pant,color,rectangulo,2)#2 pixeles de grosor el rectangulo (solo borde)
        #Fuente a usar en el texto
        fuente = Textos.fuentes(None,23)
        #Muestra el texto en pantalla, en el rectangulo
        txtenPantalla = fuente.render(texto,True,Blanco)
        #Actualiza el rectangulo cada vez que se ingresa texto, 
        # agrandando el rectangulo None el texto es muy grande
        Pant.blit(txtenPantalla, (rectangulo.x+5,rectangulo.y+5))
        #Toma el largo del texto para agrandar el rectangulo de ser necesario
        rectangulo.w = txtenPantalla.get_width()+10
        
