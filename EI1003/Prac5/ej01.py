#autor: Philippe Gonzalez Miralles                        [1 Decembre]                            UJI
class Cuenta:
    def __init__(self, saldo):
        self.saldo=saldo
        
    def ingresar(self,nuevo):
        self.saldo+=nuevo
    
    def reintegrar(self,nuevo):
        self.saldo-=nuevo
    
    def consultar_saldo(self):
        return self.saldo
    

c1=Cuenta(0)
c2=Cuenta(1000)

c1.ingresar(100)
c2.reintegrar(20)
print("Saldos: {0} y {1}".format(c1.consultar_saldo(),c2.consultar_saldo()))