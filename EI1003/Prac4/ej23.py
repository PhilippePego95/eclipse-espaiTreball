#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from modulomatrices import leerMatrizEnteros



 
def producto_diagonal_secundaria(matriz):
    producte=1
    if len(matriz) ==len(matriz[0]):
        for i in range(len(matriz)):
            producte*=matriz[i][len(matriz)-i-1]
        return producte
#****************************************************
nombreFichero = input('Introduce el nombre de un fichero: ')

matriz = leerMatrizEnteros(nombreFichero)
producte=producto_diagonal_secundaria(matriz)
if producte!=None:
    print("El producto de los elementos en la diagonal secundaria es {0}".format(producte))
else:
    print("Error. Se requiere una matriz cuadrada")      