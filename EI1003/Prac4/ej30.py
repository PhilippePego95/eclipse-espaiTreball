#autor: Philippe Gonzalez Miralles                        [24 Novembre]                            UJI

from moduloimagen import leerImagen, mostrarImagen



def reflejar_vertical(matriz):
    fila= len(matriz)
    columna=len(matriz[fila//2])
    
    for j in range(columna):
        for i in range(fila//2):
            
            #matriz[i][j]
            aux=matriz[len(matriz)-i-1][j]
            
            matriz[len(matriz)-i-1][j]=matriz[i][j]
            matriz[i][j]=aux

                
    
nombreFichero = input("Introduce el nombre de la imagen: ")

matriz = leerImagen(nombreFichero)



(reflejar_vertical(matriz))
mostrarImagen(matriz)

