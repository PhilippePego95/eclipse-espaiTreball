#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from modulomatrices import leerMatrizEnteros



 
def sumar_columna(matriz,columna):
    suma=0
    for i in range(len(matriz)):
        suma+=matriz[i][columna]
    return suma
#****************************************************
nombreFichero = input('Introduce el nombre de un fichero: ')

matriz = leerMatrizEnteros(nombreFichero)
for i in range(len(matriz[0])):
    suma=sumar_columna(matriz,i)
    print("La suma de los elementos en la columna {0} es {1}".format(i,suma))

        