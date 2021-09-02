import pygame, sys
from pygame.locals import *

pygame.init()

# Crea la ventana
surface = pygame.display.set_mode((350, 250), pygame.RESIZABLE)

pygame.display.set_caption("Prueba de Redimensionado")

while True:
    surface.fill((255,255,255))

    # Dibuja un rectángulo rojo que redimensione la ventana como prueba.
    pygame.draw.rect(surface, (200,0,0), (surface.get_width()/3,
                                          surface.get_height()/3,
                                          surface.get_width()/3,
                                          surface.get_height()/3))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Este es el código que redimensiona la ventana
        if event.type == VIDEORESIZE:
            # Recrea la ventana con el nuevo tamaño
            surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)

