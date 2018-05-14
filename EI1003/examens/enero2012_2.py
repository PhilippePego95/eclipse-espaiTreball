class Empleado:
    def __init__(self,dni):
        self.dni=dni
        self.horas=[0]*12
    def actualizar(self,mes,hora):
        self.horas[mes]+=hora
        
def crear_lista(fitxer):
    fichero=open(fitxer,"r")
    primer=True
    lista=[]
    for linea in fichero:
        datos=linea.rstrip().split("#")
        dni=datos[0]
        mes=int(datos[2])-1
        time=float(datos[3])
        noesta=True
        if primer:
            treballador=Empleado(dni)
            treballador.actualizar(mes, time)
            lista.append(treballador)
            primer=False
        else:
            
            for i in range(len(lista)):
                if dni==lista[i].dni:
                    lista[i].actualizar(mes, time)
                    noesta=False
                    break
            if noesta:
                treballador=Empleado(dni)
                treballador.actualizar(mes, time)
                lista.append(treballador)
                noesta=True                
            
    fichero.close()
    return lista

def dni_más_horas(lista):
    dni_mas=0
    maxim=0
    for i in range(len(lista)):
        temps=sumar_horas(lista[i].horas)
        
        if temps>maxim:
            maxim=temps
            dni_mas=lista[i].dni
    return dni_mas
        
    
    
    
    
def sumar_horas(lista_mes):
    hores=0    
    for i in range(12):
        hores+=lista_mes[i]
    return hores
        

def mes_más_horas(lista):
    list_mes=[0]*12
    
    for i in range(len(lista)):
        meses=lista[i].horas
        for j in range(len(meses)):
            list_mes[j]+=meses[j]
    mes_hores=0
    mess=0
    for i in range(12):
        if list_mes[i]>mes_hores:
            mes_hores=list_mes[i]
            mess=i+1
    return mess
        
print("--------------------TREBALLADORS--------------------------")

lista =crear_lista("dni.txt")
for i in range(len(lista)): 
    print(lista[i].dni,lista[i].horas)
print("-----------------------------------------------------------")
dnis=dni_más_horas(lista)
print("El treballador en més hores es:",dni_más_horas(lista))
print("-----------------------------------------------------------")
print("El mes en més faena és:",mes_más_horas(lista))




