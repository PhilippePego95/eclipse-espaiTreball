#autor: Philippe Gonzalez Miralles                        [18 Desembre]                            UJI

def evaluación_test(plantilla ,respostes):
    examen=[]
    be=0
    mal=0
    ns=0
    if len(plantilla)==len(respostes):
        for i in range(0,len(plantilla)):
            if respostes[i]==plantilla[i] and len(respostes[i])>0:
                be+=1
            elif respostes[i]=="*":
                ns+=1
            else:
                mal+=1
        examen.append(be)
        examen.append(mal)
        examen.append(ns)
        return examen
#**********************************************

nombre_fichero = input('Introduce el nombre de un fichero de test: ')
fichero = open(nombre_fichero, 'r') # Abrir en modo lectura

plantilla=fichero.readline().rstrip()

    
for linea in fichero:  
          
    cadena=linea.rstrip().split("#")
    
    if len(cadena)>1:
        respostes=evaluación_test(plantilla, cadena[1])
        nota=10*((respostes[0])-respostes[1])/(len(plantilla))

        
        if nota<0:
            nota=0
        print("El alumno con DNI {0} ha obtenido una nota de {1:.2f} puntos".format(cadena[0],nota))

    
fichero.close() # Cerrar el fichero



