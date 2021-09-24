class Datos:
    def __init__(self):
        pass

#Bloques
'''
def generar_bloques_esquinas(posIniX,posIniY,largoBloq,altoBloq):
    #BLOQUE AZUL
    pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    posIniY
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Azul,
                    (posIniX+1,
                    posIniY+1
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    posIniY+21
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Azul,
                    (posIniX+1,
                    posIniY+22
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (posIniX,
                    posIniY+42
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Azul,
                    (posIniX+1,
                    posIniY+43
                    ,largoBloq,altoBloq))#Angulo B
    draw_text('Ángulo : ', font3, Blanco, Pant, posIniX+5, posIniY+1)
    draw_text('Velocidad : ', font3, Blanco, Pant, posIniX+5, posIniY+25)
    draw_text('Metros : ', font3, Blanco, Pant, posIniX+5, posIniY+46)

    #BLOQUE ROJO
    pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    posIniY
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Rojo,
                    (Pant.get_width()-largoBloq+1,
                    posIniY+1
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    posIniY+21
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Rojo,
                    (Pant.get_width()-largoBloq+1,
                    posIniY+22
                    ,largoBloq,altoBloq))#Angulo B
        
    pygame.draw.rect(Pant,Negro,
                    (Pant.get_width()-largoBloq,
                    posIniY+42
                    ,largoBloq+2,altoBloq+2))#Angulo N
    pygame.draw.rect(Pant,Rojo,
                    (Pant.get_width()-largoBloq+1,
                    posIniY+43
                    ,largoBloq,altoBloq))#Angulo B
        
    draw_text('Ángulo : ', font3, Blanco, Pant, Pant.get_width()-largoBloq+5, posIniY+1)
    draw_text('Velocidad : ', font3, Blanco, Pant, Pant.get_width()-largoBloq+5, posIniY+25)
    draw_text('Metros : ', font3, Blanco, Pant, Pant.get_width()-largoBloq+5, posIniY+46)
idth()-largoBloq+5, posIniY+46)

'''
#Datos
'''
def texto_esquinas(texto_usuario,rectanguloTXT,color,activo):
    if activo == True:
        color = Rojo
    else:
        color = color
        #print(texto_usuario)
    pygame.draw.rect(Pant,color,rectanguloTXT,2)
    textoenPant = font3.render(texto_usuario,True,Blanco)
    Pant.blit(textoenPant,(rectanguloTXT.x+5,rectanguloTXT.y+5))
    rectanguloTXT.w = textoenPant.get_width()+10
    
'''