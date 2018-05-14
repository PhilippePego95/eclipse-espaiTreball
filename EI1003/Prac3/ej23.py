respostes=input("Introduce la plantilla de respuestas correctas: ")
print("Ve introduciendo respuestas de alumnos, o vacío para acabar...")

resp="**"
cont=0
while len(resp)>0:
    
    resp=input("Nuevas respuestas: ")
    be=0
    mal=0
    ns=0
    if len(resp)==len(respostes):
        for i in range(0,len(resp)):
            if respostes[i]==resp[i]:
                be+=1
            elif resp[i]=="*":
                ns+=1
            else:
                mal+=1
        print("Resultados: {0} BIEN; {1} MAL; {2} NS/NC".format(be,mal,ns))
        cont+=1
    elif len(resp)==0:
        res=""
    else:
        print("La cadena introducida es de longitud {0} (se esperaba {1})".format(len(resp),len(respostes)))

print("Alumnos corregidos:",cont)