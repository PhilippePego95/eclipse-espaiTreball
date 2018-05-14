#autor Philippe Gonzalez Miralles                      {2 Novembre 2017}                                  UJI

cadena=input("Introduce un texto (vacío para acabar): ")
tot=1

while tot>0:
    tot=0
    
    for i in cadena:
        tot+=1
    if tot>0:
        print("Su longitud es",tot)
        cadena=input("Introduce otro texto (vacío para acabar): ")
print("¡Adiós!")