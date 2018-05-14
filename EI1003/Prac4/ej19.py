#autor: Philippe Gonzalez Miralles                        [22 Novembre]                            UJI

from modulomatrices import leerMatrizEnteros

nombreFichero = input('Introduce el nombre de un fichero: ')

def sumar_elementos(matriz):
    
    suma=0
    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
            suma+=int(matriz[fila][col])
            
    return suma
matriz = leerMatrizEnteros(nombreFichero)
 
suma=sumar_elementos(matriz)
print("La suma de todos los elementos en la matriz es",suma)

        