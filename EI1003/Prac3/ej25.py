#autor Philippe Gonzalez Miralles                      {25 Novembre 2017}                                  UJI

def contar_secuencias_dígitos(cadena):
    cadena = " "+ cadena
    digitos = 0
    for caracter in range(len(cadena)):
        if (cadena[caracter-1]) not in"0123456789" and cadena[caracter].isdigit():
            digitos+=1
            
    return (digitos)    

#*************PROGRAMA***********************
print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")

cadena=input("Nueva cadena: ")

while cadena!="":
    print("secuencias de dígitos encontradas: ",contar_secuencias_dígitos(cadena))
    cadena=input("Nueva cadena: ")
    
print ("¡Adiós!")