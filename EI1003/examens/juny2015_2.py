#llegir el fitxer i buscar en quin mes
#hi han mes matriculacions de eixe vehicle
#SOLS ES POT LLEGIR UNA VOLTA EL FITXER
class Matriculaciones:
    def __init__(self,provincia,tipo):
        self.provincia=provincia
        self.tipo=tipo
        self.total=0
    def actualizar(self):
        self.total+=1

def crear_lista(fitxer):
    fichero=open(fitxer,"r")
    lista=[]
    ltipo=[]
    lprov=[]
    primer=True
    for linea in fichero:
        datos=linea.rstrip().split("|")
        existe=True
        tipo=datos[0]
        provincia=datos[3]
        if primer:
            vehicle=Matriculaciones(provincia,tipo)
            vehicle.actualizar()
            lista.append(vehicle)
            ltipo.append(tipo)
            lprov.append(provincia)

            primer=False
        else:
            for i in range(len(lista)):
                if  tipo in ltipo[i]  and provincia in lprov[i]:
                    lista[i].actualizar()
                    existe=False
            if existe:
                vehicle=Matriculaciones(provincia,tipo)
                vehicle.actualizar()
                lista.append(vehicle)
                ltipo.append(tipo)
                lprov.append(provincia)
                existe=False           
            
    return lista

def mes_más_matriculaciones(fitxer,tipo_vehiculo,lista_provincias):
    fichero=open(fitxer,"r")
    lista_mes=[0]*13
    for linea in fichero:
        datos=linea.rstrip().split("|")
        if tipo_vehiculo==datos[0]and datos[3] in lista_provincias:
            mes=int(datos[-1])
            lista_mes[mes]+=1
    fichero.close()
    maxim=0
    mes=1
    for i in range(1,len(lista_mes)):
        if lista_mes[i]>maxim:
            maxim=lista_mes[i]
            mes=i
    return mes

def prov_más_matriculaciones(listaObj,tipoVehiculo,provincias):
    lista_mas=""
    maximo=0
    for i in range(len(provincias)):
        maxim=numero_matriculados(listaObj,tipoVehiculo,provincias[i])
        if maxim>maximo:
            maximo=maxim
            lista_mas=provincias[i]
    print("La provincia en major matriculacions és:",lista_mas)
            
        

def numero_matriculados(lista,tipo,provincia):
    total=0

    for i in range(len(lista)):
 
        if lista[i].tipo==tipo and lista[i].provincia==provincia:
            total=lista[i].total
    return total
    

provincies=["Alacant","Castelló","Valencia"]

print("-------------------------------")

print("El mes en més matriculacions:",mes_más_matriculaciones("vehicles.txt","moto",provincies) )
print("-------------------------------")
print("Llista de vehicles matriculats")
print("-------------------------------")

lista=crear_lista("vehicles.txt")
for i in range(len(lista)):
    print(lista[i].provincia,lista[i].tipo,lista[i].total)

print("-------------------------------")

prov_más_matriculaciones(lista,"tractor",provincies)
