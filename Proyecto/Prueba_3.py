import pygame,sys,random

#Llama los modulos de pygame
pygame.init()

##VARIABLES ESTATICAS##
size_ventana=(960,540)
celeste_Fondo=(135, 206, 235)
verde=(0,145,63)
rojo=(255,0,0)
rosado=(255,0,193)
morado=(143,0,255)
azul=(0,0,255)
amarillo=(255,221,0)
colores=[verde,rojo,rosado,morado,azul,amarillo]
reloj=pygame.time.Clock()

#Define la ventana
screen = pygame.display.set_mode(size_ventana)
#Nombre venttana
pygame.display.set_caption("Proyecto 1")
#Icono ventana
#icon = pygame.image.load("tanque misil.png").convert_alpha()
#Convert alpha tiene algo que ver con los pixeles
#Pone el icono
#pygame.display.set_icon(icon)


#Primer objeto
coord_X=300
coord_Y=300
size_primobj=50
vel_X=2
vel_Y=2
color=random.choice(colores)


##PRUEBA PAUSE##
def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                        pause = False
        reloj.tick(15)  

##BUCLE JUEGO##
tamoactivo = True
while tamoactivo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tamoactivo = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                    pause = True
                    paused()
    #Fondo color celeste
    screen.fill(celeste_Fondo)        
    """#Lineas#
    for x in range(60,960,60):
        pygame.draw.line(screen,verde,[x,320],[x,540],10)
    for y in range(320,540,60):
        pygame.draw.line(screen,verde,[0,y],[960,y],10)"""

    #Movimiento objeto prim
    if (coord_X>=905 or coord_X<=0):
        vel_X *= -1
        #Agregar un if pa que no salga el mismo color
        color=random.choice(colores)
    if (coord_Y>=490 or coord_Y<=0):
        vel_Y *= -1
        color=random.choice(colores)
    coord_X+=vel_X
    coord_Y+=vel_Y
    print(coord_X,coord_Y,color)
    #Primer objeto
    pygame.draw.rect(screen, color,(coord_X,coord_Y,size_primobj,size_primobj))
    #Muestra los cambios en la pantalla
    pygame.display.flip()
    #reloj.tick(60)




















    
