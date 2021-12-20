from .Variables import *
from .Textos import Textos
from .Rectangulos import Rectangulos

class DatosEsquinas:
    #Funcion para generar los bloques de las esquinas
    def generarBloques(posIniX,posIniY,largoBloq,altoBloq,jugador):
        #Dibuja rectangulos negros
        for PosY in range(0,29,21):
            pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    PosY#posIniY
                    ,largoBloq+2,altoBloq+2))
        #Dibuja rectangulos azules sobre el negro, generando un margen negro de 2 pixeles
        for PosYA in range(0,29,21):
            pygame.draw.rect(Pant, jugador.color,
                    (posIniX,
                    PosYA+1#posIniY
                    ,largoBloq,altoBloq))
 
        #Genera textos azules
        Textos.texto_pantalla_rect('Ángulo :', Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+5)
        Textos.texto_pantalla_rect('Velocidad :', Textos.fuentes(None,23), Blanco, Pant, posIniX+5,posIniY+26)
        

    #Funcion para mostrar en pantalla los datos ingresados por el jugador
    def textosEsquinas(texto,rectangulo):
        #Dibuja el borde del rectangulo
        Rectangulos.dibujaRectangulos(Pant,Negro,rectangulo,2)#2 pixeles de grosor el rectangulo (solo borde)
        #Fuente a usar en el texto
        fuente = Textos.fuentes(None,23)
        #Muestra el texto en pantalla, en el rectangulo
        txtenPantalla = fuente.render(texto,True,Blanco)
        #Actualiza el rectangulo cada vez que se ingresa texto, 
        # agrandando el rectangulo None el texto es muy grande
        Pant.blit(txtenPantalla, (rectangulo.x+5,rectangulo.y+5))
        #Toma el largo del texto para agrandar el rectangulo de ser necesario
        rectangulo.w = txtenPantalla.get_width()+10
        
