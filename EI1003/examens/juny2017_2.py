class Contenedor:
	def __init__(self, lugar,kg_recogidos):
		self.lugar=lugar
		self.kg_recogidos=kg_recogidos
		
def leer_contenedores(fitxer):
	fichero=open(fitxer,"r")
	peso=fichero.readline()
	lista=[]
	
	for linea in fichero:
		datos=linea.rstrip().split("#")
		if len(datos)>1:
			contenedor=Contenedor(datos[0],int(datos[1])-int(peso))
			#print(contenedor)
			peso=datos[1]
			lista.append(contenedor)
	return lista

def lista_contenedores_bajo_uso(lista):
	lista_bajo=[]
	num=len(lista)
	maxim=lista[0].kg_recogidos
	
	for i in range(num):
		if lista[i].kg_recogidos>maxim:
			maxim=lista[i].kg_recogidos
	
	for i in range(num):
		if lista[i].kg_recogidos<(maxim/2):
			lista_bajo.append(lista[i].lugar)
	return lista_bajo

def mostrar_secuencias_alta_recogida(lista,umbral):
	calle=[]
	cont=0
	
	for i in range(len(lista)):
		if lista[i].kg_recogidos>=umbral:
			calle.append(lista[i].lugar)
			cont+=1
		else:
			if cont>1:
				print("Secuencia alta recogida desde {0} a {1}".format(calle[0],calle[-1]))
			cont=0
			calle=[]
	if cont>1:
		print("Secuencia alta recogida desde {0} a {1}".format(calle[0],calle[-1]))

		
				
#***************************************************************************
print("----------------------")

print("Llistat de contenidors")
print("----------------------")
contenidors=leer_contenedores("basura.txt")
for i in range(len(contenidors)):
	print(contenidors[i].lugar,contenidors[i].kg_recogidos)

print("-----------------------")
print("Contenidors de baix us")
print("-----------------------")
print(lista_contenedores_bajo_uso(contenidors))
print("-------------------------------------------------------------")
mostrar_secuencias_alta_recogida(contenidors,70)

