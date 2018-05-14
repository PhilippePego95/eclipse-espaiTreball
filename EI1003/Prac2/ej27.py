num=float(input("Introduce un número: "))
cont=0
sum1=num
while num>0:
    
    num=float(input("Introduce otro número: "))
    if num>0:
        sum1=sum1+num
    cont=cont+1
if cont>0:
    rest=float(round(sum1/cont))
    print("Media: ",rest) 
else:
    print("No se han introducido datos")   

