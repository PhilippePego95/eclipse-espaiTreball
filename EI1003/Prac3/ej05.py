#autor Philippe Gonzalez Miralles

def calcular_cadena_repetida(c,n,s):
    cadena=c
    #return(((c+s)*(c-1))+c)

    if n<2:
        return cadena
    else:
        for i in range(1,n):
            cadena+=s+c
        return cadena
        

cadena=input("Introduce una cadena: ")
separador=input("Introduce un separador: ")
n=int(input("Introduce un máximo de repeticiones: "))

for i in range(1,n+1):
    print(calcular_cadena_repetida(cadena,i,separador))

