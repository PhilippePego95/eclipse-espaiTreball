from math import sqrt

class Muestra:
    def __init__(self,t,x,y):
        self.t=t
        self.x=x
        self.y=y

    
    def distancia(self,x1,y1):
        return sqrt((x1-self.x)**2+(y1-self.y)**2)
    
def leer_muestras(fitxer):
    fichero=open(fitxer,"r")
    lista=[]
    for linea in fichero:
        datos=linea.rstrip().split("#")
        t=float(datos[0])
        x=float(datos[1])
        y=float(datos[2])
        muestra=Muestra(t,x,y)
        lista.append(muestra)
      
    fichero.close()
    return lista

def distancia_total(lista):
    suma=0
    for i in range(len(lista)-1):
        suma+=lista[i].distancia(lista[i+1].x,lista[i+1].y)
    return suma

def mayor_distancia(lista):
    distancia=0
    for i in range(len(lista)-1):
        suma=lista[i].distancia(lista[i+1].x,lista[i+1].y)
        if suma>distancia:
            distancia=suma
    return suma




lista=leer_muestras("robot.txt")
print("------------------------------------------------")
print("La distancia total és:",distancia_total(lista))
print("------------------------------------------------")
print("la major distancia és:",mayor_distancia(lista))
print("------------------------------------------------")
    
    
    