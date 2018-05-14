#autor: Philippe Gonzalez Miralles                        [21 Novembre]                            UJI


def leer_lista_enteros():    
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    lista=[]

    num=input("Nuevo número: ")
    while len(num)!=0:
        num=int(num)
        lista.append(num)   
    
        num=input("Nuevo número: ")
    return lista

def posición_menor(llista,inici):
   
    minim =int(llista[inici])
    po=inici
    for i in range(inici,len(llista)):
        if int(minim)>int(llista[i]):
            minim=llista[i]
            po =i
    return po


def intercambiar(lista,i,j):
    if i !=j:
    #if primer!=pos:
        aux= lista[i]
        lista[i]= lista[j]
        lista[j]=aux
        
    
def ordenar_lista(lista):
    
    for i in range (0,len(lista)):
        #menor=posición_menor(i, lista)
        menor=posición_menor(lista,i)

        intercambiar(lista, i, menor)
        

#********_PROGRAMA_*******************
#lista=[]
lista=leer_lista_enteros()
if len(lista)>0: 
       
    print("Lista leída:",lista)
    ordenar_lista(lista)
    # print(posición_menor(2, lista))
    print("Lista ordenada:",lista)

else:
    
    print("Lista leída:",lista)
    print("Lista ordenada:",lista)
    
