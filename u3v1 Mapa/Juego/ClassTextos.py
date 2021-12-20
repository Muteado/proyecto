import pygame

class Textos:
    #Crea fuentes
    def fuentes(font,size):
        fuente = pygame.font.SysFont(font, size)
        return fuente
    
    #Genera el txt en la pantalla
    def texto_pantalla_rect(texto,fuente,color,pantalla,x,y):
        #Dibuja texto en pantalla
        objetoTXT = fuente.render(texto, 1, color) #uno para el borde suave
        rectTXT = objetoTXT.get_rect() #toma el rectangulo del texto
        rectTXT.topleft = (x, y) #pone el txt arriba a la izq
        pantalla.blit(objetoTXT, rectTXT) #agrega todo a la pantalla