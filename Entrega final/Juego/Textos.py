import pygame

class Textos:
    def fuentes(font,size):
        """Crea una fuente pygame para usarla al imprimir en pantalla.

        Parametros:
            font (fuente): El nombre de la fuente a usar, debe estar instalada en el dispositivo.
            size (int, float): Tamaño de la fuente a usar.

        Returns:
            fuente: pygame.font.SysFont
        """
        fuente = pygame.font.SysFont(font, size)
        return fuente

    def texto_pantalla_rect(texto,fuente,coloracio,pantalla,x,y):
        """Muestra el texto en pantalla

        Parametros:
            texto (str): El texto a mostrar.
            fuente (pygame.font): Fuente del texto.
            coloracio (int/rgb): Color del texto.
            pantalla (pygame.display): Pantalla pygame donde se ubicará el texto.
            x (int): Valor en el eje X de la pantalla.
            y (int): Valor en el eje Y de la pantalla.
        """
        objetoTXT = fuente.render(texto, 1, coloracio)
        rectTXT = objetoTXT.get_rect()
        rectTXT.topleft = (x, y)
        pantalla.blit(objetoTXT, rectTXT)