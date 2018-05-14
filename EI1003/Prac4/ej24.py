#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from modulomatrices import leerMatrizEnteros



 
def sumar_encima_diagonal(matriz):
    producte=0
    if len(matriz) ==len(matriz[0]):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if j>i:
                    producte+=matriz[i][j]

                    
        return producte
#****************************************************
nombreFichero = input('Introduce el nombre de un fichero: ')

matriz = leerMatrizEnteros(nombreFichero)
producte=sumar_encima_diagonal(matriz)
if producte!=None:
    print("La suma de los elementos por encima de la diagonal principal es {0}".format(producte))
else:
    print("Error. Se requiere una matriz cuadrada")      