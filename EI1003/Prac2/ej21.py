num=int(input("Introduce un número entero: "))
i=0
while i<num:
    i+=1
    cuadrado = i**2
    if cuadrado<num:
        print("El cuadrado de {0} es {1}".format(i,cuadrado))
