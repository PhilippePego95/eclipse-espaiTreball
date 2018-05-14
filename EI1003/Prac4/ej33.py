#autor: Philippe Gonzalez Miralles                        [25 Novembre]                            UJI

from moduloimagen import leerImagen, mostrarImagen


def girada_izquierda(matriz):
    
    fila= len(matriz)
    columna=len(matriz[0])
    
    nova=nueva_matriz(columna,fila,255)
    
    for i in range(fila):
        for j in range(columna):
            nova[len(matriz[0])-j-1][i]=matriz[i][j] 
  
    
            
    return nova

def nueva_matriz(nFila,nColumna,valor):
    
    matriz = [valor] * nFila
    for i in range(nFila):
        matriz[i] = [valor] * nColumna

    return matriz
                
#**********PROGRAMA*********************
nombreFichero = input("Introduce el nombre de la imagen: ")

matriz = leerImagen(nombreFichero)

nou=girada_izquierda(matriz)

mostrarImagen(nou)

