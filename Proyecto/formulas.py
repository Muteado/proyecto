#La libreria contiene trigonometria para sacar sen, cos y tan
import numpy as np
#Libreria math que aun no se muy bien para que se usa pero sirve para las funciones matematicas
from math import *
# Esta libreria sirve para funcionar como un interprete del algebra por lo que caché pero no se en que parte se usa
from sympy import *
from sympy.plotting import *



β=45 #Angulo de disparo

vi=90 #Velocidad del disparo

pico = 0 #entrar a los ciclos

θ=((β*3.14)/180) #Angulo de disparo multiplicado por pi y dividido en 180 que es el angulo de disparo


g=9.81 # m/s**2 #gravedad de la tierra


a=np.tan(θ) #tangente del angulo ingresado

b=((g)/((2*vi**2)*np.cos(θ)**2)) #formula que usa la gravedad, velocidad inicial ingresada y el angulo de inicio que ingresamos


ymax=(vi**2)*(np.sin(θ)*np.sin(θ))/(2*g) # el movimiento que hace la bala, esto marca el punto maximo que alcanza el disparo
xmax=(vi**2)*(np.sin(2*θ))/(g) # La distancia maxima que hace la bala al usar la velocidad y el angulo inicial

tmax=(vi*np.sin(θ))/(g) # tiempo que tarda la bala en llegar al punto mas alto
tv=2*(tmax) # El tiempo que pasa en el aire la bala

#####################################################################################################

if pico == 0:


    # Salidas de los datos calculados
    #print (str("La altura máxima  alcanzada por el proyectil es: Ymax")+" = "+str(ymax)+" m")
    #print (str("El alcance máximo horizontal  del proyectil es: Xmax")+" = "+str(xmax)+" m")
    
    print ("................................................................................")
    print ("................................................................................")
    
    print ("La altura máxima (m) alcanzada por el proyectil es: Ymax =",format(ymax,".2f"))
    print ("El alcance máximo horizontal(m) del proyectil es: Xmax =",format(xmax," .2f"))
    
    print ("................................................................................")
    print ("................................................................................")
    
    print ("El tiempo máximo t1max (s) que alcanza el proyectil para el ángulo β es: t1max =",format(tmax,".2f"))
    print ("El tiempo de vuelo t1v(s) que alcanza el proyectil para el angulo β es: t1v =",format(tv,".2f"))
    
    print ("................................................................................")
    print ("................................................................................")

###################################### DE AQUI PARA ABAJO NO SE PARA QUE SIRVE #################################################
x=np.linspace(0,xmax,500) # No entiendo para que funciona
print()

def f(x): # No entiendo lo que hace esta funcion
    return(a*x-b*x**2)#print(a*x-b*x**2)
f(x)
 

print()

