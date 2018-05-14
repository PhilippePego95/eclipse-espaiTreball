reservas=[[4,None,0,0,None,None,1,1,1,None],[2,2,2,None,None,None,2,None,None,None],[1,1,3,3,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None]]

def mostrar_ocupación_por_dia(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    
    for i in range(columnas):
        cont=0
        for j in range(filas):
            if matriz[j][i] !=None:
                cont+=1
        if cont>0:
            operacio=100*cont/filas
        else:
            operacio=0
        print("Dia {0}: {1:.2f} %".format(i,operacio))

def habitación_libre_periodo(matriz,habitacion,ndias):
    libre=False
    numero=0
    for i in range(len(matriz[0])):
        
        if matriz[habitacion][i]==None:
            numero+=1
        else:
            if numero==ndias:
                libre=True
                break
            numero=0            
    if numero>=ndias:
        libre=True
    return libre
def lista_habitaciones_libres_periodo(matriz,ndias):

    lista=[]
    for i in range(len(matriz)):
        cont=0
        for j in range(len(matriz[0])):
            if matriz[i][j]==None:
                cont+=1
                if cont==ndias:
                    lista.append(i)
                    cont=0
                    break
            else:
                cont=0
    if cont==ndias:
        lista.append(i)
    return lista
def cantidad_estancias(matriz,cliente):
    cantidad=0
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==cliente:
                cantidad+=1
            else:
                if cantidad>0:
                    total+=1
                cantidad=0
    if cantidad>0:
        total+=1
    return total
print("---Ocupación por dia-----------------")
mostrar_ocupación_por_dia(reservas)
print("---Habitacion libre en un periodo----")
print(habitación_libre_periodo(reservas,2,5))
print("---Listado de habitaciones libres----")
print(lista_habitaciones_libres_periodo(reservas,5))
print("---Cantidad de estancias-------------")
print(cantidad_estancias(reservas,1))




