# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:49:52 2021

@author: Alfajor
"""

import turtle as t
import time
import random as r
#ventana
actualizacion = 0.1

ventana = t.Screen()
ventana.title("hola puta")
ventana.bgcolor("black")
ventana.setup(width=600,height= 600)
ventana.tracer(0)


#objetos
#serpiente
cabeza = t.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
#cola
cola = []


#comida
comida = t.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)




#funciones
def arriba():
    cabeza.direction= "up"
def abajo():
    cabeza.direction= "down"
def izquierda():
    cabeza.direction= "left"
def derecha():
    cabeza.direction= "right"


#movimiento

def mov():    
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
        
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
        
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)


#teclado

ventana.listen()
ventana.onkeypress(arriba,"Up")
ventana.onkeypress(abajo,"Down")
ventana.onkeypress(izquierda,"Left")
ventana.onkeypress(derecha,"Right")



#ciclo principal

while True:
    ventana.update()
    
    if cabeza.distance(comida)<20:
        x= r.randint(-280, 280)
        y= r.randint(-280, 280)
        comida.goto(x,y)
        #nueva cola
        nuevo = t.Turtle()
        nuevo.speed(0)
        nuevo.shape("square")
        nuevo.color("grey")
        nuevo.penup()
        cola.append(nuevo)
        print("cola añadida")
        
    #mover cuerpo (esta parte no cache bien)
    totalseg = len(cola)
    for index in range(totalseg -1,0,-1):
        x=cola[index -1].xcor()
        y=cola[index -1].ycor()
        cola[index].goto(x,y)
        
        
    if totalseg > 0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        cola[0].goto(x,y)
        
    
    
    mov()
    time.sleep(actualizacion)
    





