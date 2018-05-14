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
    

money=float(input("Introduce cuántos euros quieres como saldo inicial de tu cuenta: "))
c1=Cuenta(money)
opc=1

while opc!=4:
    print("\n1. Hacer un ingreso")
    print("2. Pedir un reintegro")
    print("3. Consultar el saldo")
    print("4. Salir")
    opc=int(input("Elige una opción: "))
    
    if opc==1:
        money=float(input("Introduce cuántos euros quieres ingresar: "))

        c1.ingresar(money)
    elif opc==2:
        money=float(input("Introduce cuántos euros quieres que se te reintegren: "))

        c1.reintegrar(money)
    elif opc==3:
        print("El saldo actual es {0:.2f} euros ".format(c1.consultar_saldo()))
    else:
        print("¡Adiós!")
        