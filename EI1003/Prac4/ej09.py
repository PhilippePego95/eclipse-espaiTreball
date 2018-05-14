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

lista=leer_lista_enteros()
print("Lista leída:",lista)
print("Ve contestando con números enteros, o con una cadena vacía para acabar...")

numero= input("¿Qué suma he de buscar en dos posiciones consecutivas? ")
while len(numero)>0:
    for i in range(0 ,len(lista)-1):
        if int(numero)== int(lista[i])+int(lista[i+1]):
            print("{0} + {1} = {2}".format(lista[i],lista[i+1],numero))
    numero= input("¿Qué suma he de buscar en dos posiciones consecutivas? ")
    
    
print("¡Adiós!")
    