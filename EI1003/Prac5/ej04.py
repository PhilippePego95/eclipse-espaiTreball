#autor: Philippe Gonzalez Miralles                        [1 Decembre]                            UJI

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
        self.distancia+=((tiempo)*self.velocidad)
    
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
coche = Coche()

opc=1

print("Tu coche está inicialmente parado")

while opc!=5:
    
    print("\n1. Acelerar")
    print("2. Decelerar")
    print("3. Actualizar")
    print("4. Consultar")
    print("5. Salir")
    
    opc=int(input("Elige una opción: "))
    
    if opc==1:
        rapid=float(input("Introduce cuántos km/h quieres acelerar: ")) 
        coche.acelerar(rapid)
        
    elif opc==2:
        lento=float(input("Introduce cuántos km/h quieres decelerar: "))
        coche.decelerar(lento)

    elif opc==3:
        hores=float(input("Introduce cuántas horas han pasado: "))
        coche.actualizar(hores)
        
    elif opc==4:
        print("El tiempo trascurrido es {0:.2f} h".format(coche.consultar_tiempo()))
        print("La distancia recorrida es {0:.2f} km".format(coche.consultar_distancia()))
        print("La velocidad actual es {0:.2f} km/h".format(coche.consultar_velocidad_actual()))
        
        if coche.consultar_velocidad_media()!=None:
            print("La velocidad media es {0:.2f} km/h".format(coche.consultar_velocidad_media()))
            
        else:
            print("No puedo calcular la velocidad media si no ha trascurrido tiempo")
            
    else:
        print("¡Adiós!")    
     

          
    
    

        