
#Libreria math que aun no se muy bien para que se usa pero sirve para las funciones matematicas
from math import *
# Esta libreria sirve para funcionar como un interprete del algebra por lo que caché pero no se en que parte se usa

#β=int(input("Ingrese el angulo de disparo entre 0° y 180°: ")) #Angulo de disparo
β=45
#vi=int(input("Ingrese la velocidad de disparo: ")) #Velocidad del disparo
vi=40
θ=((β*pi)/180) #Angulo de disparo multiplicado por pi y dividido en 180 que es el angulo de disparo
#g=9.81 # m/s**2 #gravedad de la tierra
a=tan(θ) #tangente del angulo ingresado
b=((9.81)/((2*vi**2)*cos(θ)**2)) #formula que usa la gravedad, velocidad inicial ingresada y el angulo de inicio que ingresamos
ymax=(vi**2)*(sin(θ)*sin(θ))/(2*9.81) # el movimiento que hace la bala, esto marca el punto maximo que alcanza el disparo
xmax=(vi**2)*(sin(2*θ))/(9.81) # La distancia maxima que hace la bala al usar la velocidad y el angulo inicial
tmax=(vi*sin(θ))/(9.81) # tiempo que tarda la bala en llegar al punto mas alto
tv=2*(tmax) # El tiempo que pasa en el aire la bala

#####################################################################################################
print("La altura maxima alcanzada es: ",ymax)
print("La distancia recorrida es: ",xmax)
print("El tiempo que se demora en llegar la bala es: ",tmax)
print("El tiempo que la bala pasa en el aire es: ",tv)
###################################### DE AQUI PARA ABAJO NO SE PARA QUE SIRVE #################################################

#x=0

'''distanciax = []
distanciay = []
def f(x):
    weas[x] = a*x-b*x**2
    return f(x+1)


x=0
y=0
    
distancia1 = xmax
distancia2 = ymax'''
'''for x in distanciax:
    print("pico")
    distanciax.append(distancia1)
    distanciay.append(distancia2)
    
for y in distanciay:
    print("pico")
    print(distanciax[y])
    print(distanciay[y])
 '''
'''while x != distancia1:
    print(x)
    x+1
    distanciax.append(distancia1)
    distanciay.append(distancia2)        
'''
'''for x in weas:
    weas.append(xmax)
    print(x)'''

'''x=np.linspace(0,xmax) # No entiendo para que funciona
print()

def f(x): # No entiendo lo que hace esta funcion
    return(a*x-b*x**2)#print(a*x-b*x**2)
f(x)
 
'''
#f(x)
#print()

