#autor: Philippe Gonzalez Miralles                        [16 Novembre]                            UJI

print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")

cadena=input("Nueva cadena: ")
lista=[]
while len(cadena)>0:
    lista.append(cadena)
    cadena=input("Nueva cadena: ")

print("Cadenas leídas (desde la última hasta la primera):")
tam=len(lista)
for i in range (0,len(lista)):
    pos=tam-i-1
    tamany=len(lista[pos])
    #print(pos)
    print("  Cadena de longitud {0}: =>{1}<=".format(tamany,lista[pos]))