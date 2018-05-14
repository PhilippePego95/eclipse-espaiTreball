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
        
        
coche = Coche()
coche.acelerar(100)
coche.actualizar(1.5)
coche.decelerar(40.1)
coche.actualizar(0.5)
print("Tiempo: {0}".format(coche.consultar_tiempo()))
print("Distancia: {0}".format(coche.consultar_distancia()))
print("Velocidad actual: {0}".format(coche.consultar_velocidad_actual()))
print("Velocidad media: {0}".format(coche.consultar_velocidad_media()))

        