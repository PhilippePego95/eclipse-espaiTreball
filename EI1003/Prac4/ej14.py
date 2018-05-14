#autor: Philippe Gonzalez Miralles                        [22 Novembre]                            UJI

def leer_alturas():
    print("Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...")

    i=0
    altura=input("Altura en metros en el punto kilométrico {0}: ".format(i))
    altures=[]
    while len(altura)>0:
        altures.append(int(altura))
        i+=1
        altura=input("Altura en metros en el punto kilométrico {0}: ".format(i))

    return altures
def calcular_desniveles(lista):
    desnivell=[]
    for i in range(len(lista)-1):
        desnivells=int(lista[i+1])-int(lista[i])
        desnivell.append(desnivells)
    return desnivell

def posición_máximo(lista):
    maximo=0
    pos=0
    for i in range(len(lista)):
        if maximo<=int(lista[i]):
            maximo=int(lista[i])
            pos=i
    return pos
            
            
#*********************************************


altura=leer_alturas()
if len(altura)>1:
    print("Lista de alturas:",altura)

    desnivell=calcular_desniveles(altura)    
    print("Lista de desniveles:",desnivell)
    
    maxim=posición_máximo(desnivell)
    if int(desnivell[maxim])>0:
        print("Kilómetro con mayor desnivel de subida:")
        print(" Entre los puntos kilométricos {0} y {1}".format(maxim,maxim+1))
        print(" Desnivel de {0} m".format(desnivell[maxim]))
    else:
        print("Ningún kilómetro es de subida")
else:
    print("Recorrido no válido, con menos de dos puntos")
