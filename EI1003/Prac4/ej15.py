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

def mostrar_tramos_subida(lista):

    subida=False
    dalt=[]
    for i in range(len(lista)-1):
        if subida==False:
            if lista[i]<lista[i+1]:
                dalt.append(i)
                subida=True
        if subida ==True:
            if lista[i]>=lista[i+1]:
                subida=False
                dalt.append(i)
    if subida==True:
        dalt.append(len(lista)-1)
    tram=0
    if len(dalt)>0:
        for i in range(0,len(dalt)-1,2):
            tram+=1
            inici=dalt[i]
            longitut=dalt[i+1]
            desnivell=lista[dalt[i+1]]-lista[dalt[i]]
            mostrar_tramo(tram,inici,longitut,desnivell)
    else:
        print("Ningún kilómetro es de subida")

            
        
def mostrar_tramo(nTramo,inici,longitud,desnivel):
    
    print("Tramo de subida número {0}:".format(nTramo))
    print(" Entre los puntos kilométricos {0} y {1}".format(inici,longitud))
    print(" Longitud de {0} km".format(longitud-inici))
    print(" Desnivel de {0} m".format(desnivel))
    
#***********************************
altures=leer_alturas()
#altures=[1000, 1000, 950, 1025, 1050, 1100, 975, 1025, 1075, 1125, 1175, 1175, 1200]
if len(altures)>=2:
    print("Lista de alturas:",altures)
    mostrar_tramos_subida(altures)
else:
    print("Recorrido no válido, con menos de dos puntos")






   

    

           
        
        