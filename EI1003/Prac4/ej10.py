#autor: Philippe Gonzalez Miralles                        [20 Novembre]                            UJI


def leer_lista_enteros():    
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    lista=[]

    num=input("Nuevo número: ")
    while len(num)!=0:
        num=int(num)
        lista.append(num)   
    
        num=input("Nuevo número: ")
    return lista

def posición_menor(llista):
    minim =llista[0]
    po=0
    for i in range(len(llista)):
        if minim>int(llista[i]):
            minim=llista[i]
            po =i
    return po


def intercambiar(lista,primer,pos):

    aux= lista[primer]
    lista[primer]= lista[pos]
    lista[pos]=aux

lista=[]
lista=leer_lista_enteros()

if len(lista)>0: 


    pos=posición_menor(lista)
    
    print("Lista leída:",lista)
    
    
    if intercambiar(lista,0,pos)==None:
        print("Modificada:",lista)  
    else:
        lista=intercambiar(lista,0,pos)

        print("Modificada*:",lista)  

else:    
    print("Lista leída:",lista)
    print("Modificada:",lista)   


    
    