#autor: Philippe Gonzalez Miralles                        [22 Novembre]                            UJI
def evaluación_test(plantilla ,respostes):
    examen=[]
    be=0
    mal=0
    ns=0
    if len(plantilla)==len(respostes):
        for i in range(0,len(plantilla)):
            if respostes[i]==plantilla[i]:
                be+=1
            elif respostes[i]=="*":
                ns+=1
            else:
                mal+=1
        examen.append(be)
        examen.append(mal)
        examen.append(ns)
        return examen

#*******************************************

respostes=input("Introduce la plantilla de respuestas correctas: ")

print("Ve introduciendo respuestas de alumnos, o vacío para acabar...")

resp="**"
cont=0
while len(resp)>0:
    resp=input("Nuevas respuestas: ")

    if len(resp)==len(respostes):
        examen=evaluación_test(respostes,resp)
        print("Resultados: {0} BIEN; {1} MAL; {2} NS/NC".format(examen[0],examen[1],examen[2]))
        cont+=1
    elif len(resp)==0:
        res=""
    else:
        print("La cadena introducida es de longitud {0} (se esperaba {1})".format(len(resp),len(respostes)))

print("Alumnos corregidos:",cont)