#autor: Philippe Gonzalez Miralles                        [25 Novembre]                            UJI

from moduloimagen import leerImagen, mostrarImagen

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

def nueva_matriz(nFila,nColumna,valor):
    
    matriz = [valor] * nFila
    for i in range(nFila):
        matriz[i] = [valor] * nColumna

    return matriz
def borde(matriz,nova,numero):
    
    #anem a ficar el borde 
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            #pintar  borde si i o j son 0
            if i==0 or j==0:
                nova[i][j]=numero
            if j==len(matriz[0])-1 or i==len(matriz)-1:
                nova[i][j]=numero   
    
def difuminada(matriz,numero):
    #creem la nova matriu
    nova=nueva_matriz(len(matriz),len(matriz[0]),255)
    #li fique borde
    borde(matriz,nova,numero)
    for i in range (len(matriz)-1):
        for j in range(len(matriz[0])-1):
            #per a saber que no anem a tocar el marc
                if i!=0 and j!=0 and j!=len(matriz[0])-1 and i!=len(matriz)-1:
                    nova[i][j]=round(promedio_entorno(matriz,i,j))
        
                 
    return nova
#***************************************************

   
nombreFichero = input("Introduce el nombre de la imagen: ")

matriz = leerImagen(nombreFichero)

numero=int(input("Introduce el valor del borde: "))

nou=difuminada(matriz, numero)

mostrarImagen(nou)

