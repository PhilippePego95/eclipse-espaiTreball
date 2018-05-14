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
    if len(lista)-1>=pos and pos>=0:
        del lista[pos]
        return True
    else:
        return False
    
lista=leer_lista_enteros()   
 
while len(lista)>0:
    num=int(input("¿Qué posición debo eliminar de {0}? ".format(lista)))
    if borrar_elemento(lista, num)==False:
        print("Posición incorrecta")


print("La lista ha quedado vacía")
    
    
