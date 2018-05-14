num=int(input("Introduce un número entero: "))
i=1
suma=0
while i<=num:
    if num%i==0:
        suma=suma+i
    i=i+1
print("La suma de los divisores de {0} es {1}".format(num,suma))