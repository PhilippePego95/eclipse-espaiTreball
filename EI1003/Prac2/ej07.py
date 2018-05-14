a=int(input("Introduce el primer número: "))
menor=a

a=int(input("Introduce el segundo número: "))
if menor>a:
    menor=a
 
a=int(input("Introduce el tercer número: "))
if menor>a:
    menor=a
   
print("El menor es: ",menor)