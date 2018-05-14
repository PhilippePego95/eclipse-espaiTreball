#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from modulomatrices import leerMatrizEnteros



 
def sumar_fila(matriz,fila):
    suma=0
    for i in range(len(matriz[fila])):
        suma+=matriz[fila][i]
    return suma
#****************************************************
nombreFichero = input('Introduce el nombre de un fichero: ')

matriz = leerMatrizEnteros(nombreFichero)
for i in range(len(matriz)):
    suma=sumar_fila(matriz,i)
    print("La suma de los elementos en la fila {0} es {1}".format(i,suma))

        