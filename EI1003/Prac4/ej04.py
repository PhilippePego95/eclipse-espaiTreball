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
cuadrat=[]
lista=leer_lista_enteros()

for i in range (len(lista)):
    cuadrat.append(lista[i]**2)

print("Cuadrados de los números leídos: {0}".format(cuadrat))
print("Números leídos: {0}".format(lista))
