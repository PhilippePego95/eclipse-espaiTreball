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
def suma_lista(lista):
    suma=0
    for i in range(len(lista)):
        suma+=int(lista[i])
    return suma

def repetidos_lista(lista):
    nou=[]
    for i in range (len(lista)):
        cont=0
        for j in range (len(lista)):
            if lista[i]==lista[j]:
                cont+=1

        if cont>1 and not lista[i] in nou:
            nou.append(lista[i]) 
    return nou

lista=[]
llista_repetida=[]

lista=leer_lista_enteros()
llista_repetida=repetidos_lista(lista)

suma=suma_lista(llista_repetida)

print("Números leídos más de una vez (suman {0}): {1}".format(suma,llista_repetida))
print("Todos los números leídos:",lista)

        