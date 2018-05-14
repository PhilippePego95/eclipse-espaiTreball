#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from moduloimagen import leerImagen, mostrarImagen



def binarizada(matriz,umbral):
    matriz2=nueva_matriz(len(matriz),len(matriz[0]),0)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<=umbral:
                
                matriz2[i][j]=0
            else:
                matriz2[i][j]=255
    return matriz2
                
def nueva_matriz(nFila,nColumna,valor):
    matriz = [valor] * nFila
    for i in range(nFila):
        matriz[i] = [valor] * nColumna
            
    return matriz

nombreFichero = input("Introduce el nombre de la imagen: ")
umbral=int(input("Introduce el umbral: "))

matriz = leerImagen(nombreFichero)
binar=binarizada(matriz,umbral)
mostrarImagen(binar)
#print(matriz)
