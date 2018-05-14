num=int(input("Introduce un número entero: "))
i=1
suma=0
while i<=num:
    if num%i==0:
        suma=suma+1
    i=i+1
if suma==2:
    print("Es primo")
else:
    print("No es primo")