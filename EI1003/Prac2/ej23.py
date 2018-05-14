num=int(input("Introduce un número entero: "))
i=1
suma=0
while i<=num:
    if i%3 !=0 and i%5 !=0 :
        suma=suma+i
    i=i+1
print("La suma es {0}".format(suma))
    