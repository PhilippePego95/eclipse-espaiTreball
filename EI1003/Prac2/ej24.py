num=int(input("Introduce un número entero: "))
i=1
suma=0
while i<=num:
    if num%i==0:
        suma=suma+1
    i=i+1
print("El número {0} tiene {1} divisores".format(num,suma))