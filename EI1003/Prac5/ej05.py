#autor: Philippe Gonzalez Miralles                        [5 Decembre]                            UJI
from modulomatrices import leerMatrizEnteros

class Coche:
    
    def __init__(self):
        self.tiempo=0
        self.distancia=0
        self.velocidad=0
        
    def acelerar(self,rapid):
        self.velocidad+=rapid
        
    def decelerar(self,lento):
        self.velocidad-=lento 
           
    def actualizar(self,tiempo):
        self.tiempo+=tiempo 
        self.distancia+=(tiempo)*self.velocidad
         
    def consultar_tiempo(self):
        return self.tiempo
    
    def consultar_distancia(self):
        return self.distancia
    
    def consultar_velocidad_actual(self):
        return self.velocidad
    
    def consultar_velocidad_media(self):
        if self.tiempo!=0:            
            return self.distancia  / self.tiempo

#******************************************************
objectiu=int(input("Introduce el objetivo de la carrera en km: "))
vel=int(input("Introduce la velocidad inicial en km/h: "))
nombreFichero = input('Introduce el nombre del fichero de planes de carrera: ')
matriz = leerMatrizEnteros(nombreFichero)
coche=[]
lista_distancia=[0]

for w in range(len(matriz)):
    coche.append(Coche())
    coche[w].acelerar(vel)
    
lista_distancia*=len(matriz)
    
final=False
t=1
maxim=0
e=0
while final==False:
    print("\nResultados tras",t,"h:")

    i=0
    
    while i<len(matriz):

        if e>len(matriz[i])-1:
            e=0
     
        coche[i].acelerar(matriz[i][e])
        coche[i].actualizar(1)
        
        distancia=coche[i].consultar_distancia()
        velActual=coche[i].consultar_velocidad_actual()
        
        if distancia >maxim:
            maxim=distancia
      
        lista_distancia[i]=coche[i].consultar_distancia()
        print("Coche {0}: alcanza el km {1} a {2} km/h".format(i,distancia,velActual))
        i+=1
    e+=1 
    t+=1
    for j in range(len(lista_distancia)):
        
        if lista_distancia[j]>=objectiu:
            final=True
            
print("\nCoches ganadores: ",end="")
           
for i in range(len(lista_distancia)):
  
    if lista_distancia[i]==maxim:
        print(i,end=" ")
        





