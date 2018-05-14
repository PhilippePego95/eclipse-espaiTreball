#autor: Philippe Gonzalez Miralles                        [16 Novembre]                            UJI

print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")

cadena=input("Nueva cadena: ")
lista=[]
while len(cadena)>0:
    lista.append(cadena)
    cadena=input("Nueva cadena: ")

print("Cadenas leídas:")
for i in range (len(lista)):
    tamany=len(lista[i])
    print("  Cadena de longitud {0}: =>{1}<=".format(tamany,lista[i]))