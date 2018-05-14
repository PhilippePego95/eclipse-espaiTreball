num=float(input("Introduce un número: "))
menor=num
major=num
opc=0
cont=0
num2=0

while num>0:
    cont=cont+1
    num2=num2+num
    if menor<num:
        major=num
    if menor>num:
        menor=num
    num=float(input("Introduce otro número: "))
    
if cont>0:
    opc=num2/cont

    print("Media: ",opc)
    print("Mínimo: ",menor) 
    print("Máximo: ",major) 
 
else:
    print("No se han introducido datos")   

