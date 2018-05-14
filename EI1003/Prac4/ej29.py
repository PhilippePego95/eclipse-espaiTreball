#autor: Philippe Gonzalez Miralles                        [24 Novembre]                            UJI

from moduloimagen import leerImagen, mostrarImagen



def reflejar_horizontal(matriz):
    fila= len(matriz)
    columna=len(matriz[0])
    
    for i in range(fila):
        for j in range(columna//2):
            
            #matriz[i][j]
            aux=matriz[i][len(matriz[0])-j-1]
            matriz[i][len(matriz[0])-j-1]=matriz[i][j]
            matriz[i][j]=aux

                
    
nombreFichero = input("Introduce el nombre de la imagen: ")

matriz = leerImagen(nombreFichero)
reflejar_horizontal(matriz)
mostrarImagen(matriz)
#print(matriz)
