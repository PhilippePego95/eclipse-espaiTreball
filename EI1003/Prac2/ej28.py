num=float(input("Introduce un número: "))
cont=0
num2=0
while num>0:
    cont=cont+1
    if num>num2:
        num2=num
    num=float(input("Introduce otro número: "))
    

if cont>0:
    print("Máximo: ",num2) 
else:
    print("No se han introducido datos")   

