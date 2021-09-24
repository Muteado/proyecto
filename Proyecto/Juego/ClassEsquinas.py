from .ClassRectangulos import Rectangulos
from .ClassTextos import Textos
from .Variables import Azul, Blanco, Negro, Pant, Rojo
import pygame


class DatosEsquinas:
    def generarBloques(posIniX,posIniY,largoBloq,altoBloq):
        #Bloques azules
        #Dibuja rectangulos negros
        for PosY in range(0,43,21):
            pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    PosY#PosIniY
                    ,largoBloq+2,altoBloq+2))
            
        #Dibuja rectangulos azules sobre el negro, 
        # generando un margen negro de 2 pixeles
        for PosYA in range(0,43,21):
            pygame.draw.rect(Pant, Azul,
                    (posIniX,
                    PosYA+1#PosIniY
                    ,largoBloq,altoBloq))
        
        #Bloques rojos
        #Dibuja rectangulos negros
        for PosY in range(0,43,21):
            pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    PosY#PosIniY
                    ,largoBloq+2,altoBloq+2))
        #Dibuja rectangulos azules sobre el negro, 
        # generando un margen negro de 2 pixeles
        for PosYA in range(0,43,21):
            pygame.draw.rect(Pant, Rojo,
                    (Pant.get_width()-largoBloq+1,
                    PosYA+1#PosIniY
                    ,largoBloq,altoBloq))

        #Genera textos azules
        Textos.texto_pantalla_rect('Ángulo :', Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+5)
        Textos.texto_pantalla_rect('Velocidad :',Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+26)
        Textos.texto_pantalla_rect('Metros:', Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+46)
        Textos.texto_pantalla_rect('Disparar', Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+66)
        #Genera textos rojos
        Textos.texto_pantalla_rect('Ángulo :', Textos.fuentes(None,23), Blanco, Pant, Pant.get_width()-largoBloq+5,posIniY+5)
        Textos.texto_pantalla_rect('Velocidad :', Textos.fuentes(None,23), Blanco, Pant, Pant.get_width()-largoBloq+5,posIniY+26)
        Textos.texto_pantalla_rect('Metros:', Textos.fuentes(None,23), Blanco, Pant, Pant.get_width()-largoBloq+5,posIniY+46)
        Textos.texto_pantalla_rect('Disparar', Textos.fuentes(None,23), Blanco, Pant, Pant.get_width()-largoBloq+5,posIniY+66)

    def textosEsquinas(texto,rectangulo,color,activo):
        #Cambia el color del recuadro en caso de ser clickeado para saber que está activo
        if activo == True:
            if color == Rojo:
                color = Azul
            else:
                color = Rojo
        #Mantiene el color si el rectangulo no está activo
        else:
            color = color
        #Dibuja el borde del rectangulo
        Rectangulos.dibujaRectangulos(Pant,color,rectangulo,2)#2 pixeles de grosor el rectangulo (solo borde)
        #Fuente a usar en el texto
        fuente = Textos.fuentes(None,23)
        #Muestra el texto en pantalla, en el rectangulo
        txtenPantalla = fuente.render(texto,True,Blanco)
        #Actualiza el rectangulo cada vez que se ingresa texto, 
        # agrandando el rectangulo si el texto es muy grande
        Pant.blit(txtenPantalla, (rectangulo.x+5,rectangulo.y+5))
        #Toma el largo del texto para agrandar el rectangulo de ser necesario
        rectangulo.w = txtenPantalla.get_width()+10
