#autor: Philippe Gonzalez Miralles                        [24 Novembre]                            UJI

from moduloimagen import leerImagen




    
nombreFichero = input("Introduce el nombre de la imagen: ")

matriz = leerImagen(nombreFichero)

def promedio_entorno(matriz,i,j):
    a=matriz[i][j+1]
    b=matriz[i][j-1]
    q=matriz[i][j]
    c=matriz[i-1][j+1]
    d=matriz[i-1][j-1]
    e=matriz[i-1][j]
    f=matriz[i+1][j+1]
    g=matriz[i+1][j-1]
    j=matriz[i+1][j]
    
    tot=(a+b+c+d+e+f+g+j+q)/9
    return tot


fila=int(input("Introduce un número de fila: "))
columna=int(input("Introduce un número de columna: "))
promedio=promedio_entorno(matriz,fila,columna)

print("El promedio en el entorno del punto ({0},{1}) es {2:.2f}".format(fila,columna,promedio))
