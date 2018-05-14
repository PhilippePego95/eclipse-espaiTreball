#autor Philippe Gonzalez Miralles
def contar_divisores(num):  
   
    i=1
    suma=0
    while i<=num:
        if num%i==0:
            suma=suma+1
        i=i+1
    return suma
    
    
n=int(input("Introduce un número entero: "))
divisores=contar_divisores(n)
print("El número {0} tiene {1} divisores".format(n,divisores))
    