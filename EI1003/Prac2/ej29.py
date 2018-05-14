num=float(input("Introduce un número: "))
menor=num
cont=0
num2=0
while num>0:
    cont=cont+1
    if menor>num:
        menor=num
    num=float(input("Introduce otro número: "))
    

if cont>0:
    print("Mínimo: ",menor) 
else:
    print("No se han introducido datos")   

