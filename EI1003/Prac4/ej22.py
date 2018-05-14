#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from modulomatrices import leerMatrizEnteros



 
def sumar_diagonal(matriz):
    suma=0
    if len(matriz) ==len(matriz[0]):
        for i in range(len(matriz)):
            suma+=matriz[i][i]
        return suma
#****************************************************
nombreFichero = input('Introduce el nombre de un fichero: ')

matriz = leerMatrizEnteros(nombreFichero)
suma=sumar_diagonal(matriz)
if suma!=None:
    print("La suma de los elementos en la diagonal principal es {0}".format(suma))
else:
    print("Error. Se requiere una matriz cuadrada")      