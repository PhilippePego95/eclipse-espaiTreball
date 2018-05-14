#autor: Philippe Gonzalez Miralles                        [22 Novembre]                            UJI

def es_dígito(caracter):
    return caracter.isdigit()

def secuencias_dígitos(cadena):
    llista=[]
    numero=""
    cadena+="d"
    for i in range(len(cadena)):
        if es_dígito(cadena[i])==True:
            numero+=cadena[i]
            
        else:
            if len(numero)>0:
                llista.append(numero)
            numero=""
    return llista
            
cadena=input("Introduce una cadena: ")
llista=secuencias_dígitos(cadena)
print("La lista de secuencias obtenida es",llista)

