#autor: Philippe Gonzalez Miralles                        [18 Desembre]                            UJI

def posición_menor(llista,inici):
   
    minim =llista[inici]
    po=inici
    for i in range(inici,len(llista)):
        if minim>llista[i]:
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
#******************************************************

nombre_fichero = input('Introduce el nombre de un fichero de test: ')
fichero = open(nombre_fichero, 'r') # Abrir en modo lectura       
dni=[]
for linea in fichero:    
    cadena=linea.split("#")
    if len(cadena)>1:
        dni.append(cadena[0])

ordenar_lista(dni)

for num in dni:
    print(num)
        
fichero.close() # Cerrar el fichero
        