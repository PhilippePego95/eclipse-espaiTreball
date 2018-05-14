#autor Philippe Gonzalez Miralles

def mostrar_cadena_repetida(c,n,s):
    cadena=c
    #print(((c+s)*(c-1))+c)
    if n<2:
        print(cadena)
    else:
        for numero in range(1,n):
            cadena+=s+c
        print(cadena)
        
        

cadena=input("Introduce una cadena: ")
separador=input("Introduce un separador: ")
n=int(input("Introduce un máximo de repeticiones: "))

for i in range(1,n+1):
    mostrar_cadena_repetida(cadena,i,separador)

