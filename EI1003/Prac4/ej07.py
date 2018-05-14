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

def borrar_elemento(lista,pos):
    tamany=len(lista)
    for i in range (0,len(lista)):
        tamany-=1
        if lista[tamany]==pos:
            del lista[tamany]
            
            return True
            break
    return False



lista=leer_lista_enteros()   
 
while len(lista)>0:
    num=int(input("¿Qué número debo eliminar de {0}? ".format(lista)))
    if borrar_elemento(lista, num)==False:
        print("Número no encontrado")


print("La lista ha quedado vacía")
    
    
