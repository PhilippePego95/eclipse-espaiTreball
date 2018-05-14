#autor Philippe Gonzalez Miralles                      (2 Novembre 2017)                                  UJI

def son_amigos(n1,n2):
    
    num1=sumar_divisores_propios(n1)
    
    num2=sumar_divisores_propios(n2)

    return n1==num2 and n2==num1
    
    
def sumar_divisores_propios(num):
    i=1
    suma=0
    while i<num:
        if num%i==0:
            suma=suma+i
        
        i=i+1
   
    return suma    

repetir =True

while repetir:
    nA=int(input("Introduce un número entero a: "))
    nB=int(input("Introduce un número entero b: "))
    
    if son_amigos(nA, nB):
        print("Los dos números son amigos")
    else:
        print("Los dos números no son amigos")
        
        
    resp=input("¿Seguimos comprobando amistades (S/N)? ")    
    if resp=="N"or resp=="n":
        repetir=False
        
print("¡Adiós!")
    