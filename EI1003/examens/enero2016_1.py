class SMS:
    def __init__(self, remitente, fecha, hora, mensaje):
        self.remitente = remitente
        self.fecha = fecha
        self.hora = hora
        self.mensaje = mensaje
    
def crear_lista_sms(fitxer):
    fichero=open(fitxer,"r")
    lista=[]
    for linea in fichero:
        datos=linea.rstrip().split("|")
        mensaje=SMS(datos[0],datos[1],datos[2],datos[3])
        lista.append(mensaje)
    fichero.close()
    return lista
def mostrar_porcentajes(lista):
    lista_horas=[0]*24
    for i in range(len(lista)):
        hora=lista[i].hora
        time=hora.split(":")
        lista_horas[int(time[0])]+=1
        
    for i in range(len(lista_horas)-1):
        if lista_horas[i]>0:
            cantidad=lista_horas[i]
            print("En la franja de {0}:00 a {1}:00 se recibió el {2} % de los pensajes".format(i,i+1,cantidad*100/len(lista)))
        
        
def crear_lista_remitentes_publicitarias(lista,frases):
    numeros=[]
    for i in range(len(lista)):
        for j in range(len(frases)):
            if frases[j] in lista[i].mensaje :
                if not lista[i].remitente in numeros:
                    numeros.append(lista[i].remitente)
                
    return numeros      
 
def eliminar_sms_remitentes(lista,telf):   
    i=0
    while i<len(lista):
        if lista[i].remitente in telf:
            del lista[i]
        else:
            i+=1
            
    
lista=crear_lista_sms("telefono.txt")
frases=["IKEA","El Corte Inglés","Decathlon","Leroy Merlin"]
print("------------------------------------------")

for i in range(len(lista)):
    print(lista[i].remitente,lista[i].mensaje)
print("------------------------------------------")
mostrar_porcentajes(lista)
print("------------------------------------------")
tel=crear_lista_remitentes_publicitarias(lista,frases)
print(tel)
print("------------------------------------------")
eliminar_sms_remitentes(lista,tel)
for i in range(len(lista)):
    print(lista[i].remitente,lista[i].mensaje)
print("------------------------------------------")
    
    