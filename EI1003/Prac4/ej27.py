#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from moduloimagen import leerImagen, mostrarImagen
def aplicar_filtro_negativo(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            #if matriz[i][j]== "255":
                
            matriz[i][j]=255- matriz[i][j]
                

nombreFichero = input("Introduce el nombre de la imagen: ")
matriz = leerImagen(nombreFichero)
aplicar_filtro_negativo(matriz)
mostrarImagen(matriz)
#print(matriz)
