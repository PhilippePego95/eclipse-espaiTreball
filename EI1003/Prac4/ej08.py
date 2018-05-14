#autor: Philippe Gonzalez Miralles                        [16 Novembre]                            UJI

def leer_lista_enteros():    
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    lista=[]

    num=input("Nuevo número: ")
    while len(num)!=0:
        num=int(num)
        lista.append(num)   
    
        num=input("Nuevo número: ")
    return lista


def borrar_elemento(lista,num):
    #for i in range (0,len(lista)):
    a=0
    b=0
    while a<len(lista):
        #print(a)
        if lista[a]==num:
            del lista[a]
            b=1
        else:
            a+=1
    return b==1
            




lista=leer_lista_enteros()   
 
while len(lista)>0:
    num=int(input("¿Qué número debo eliminar de {0}? ".format(lista)))
    if borrar_elemento(lista, num)==False:
        print("Número no encontrado")


print("La lista ha quedado vacía")